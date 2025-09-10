import os
import pandas as pd
from playwright.sync_api import sync_playwright
import time
from datetime import datetime
from tqdm import tqdm
from typing import Dict


def load_env_file(env_path: str = ".env") -> Dict[str, str]:
    """Minimal .env loader to avoid external deps."""
    env: Dict[str, str] = {}
    if not os.path.exists(env_path):
        return env
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


# Load env from file (if exists) then os.environ as fallback
_file_env = load_env_file()
SUBJECT_TEMPLATE = _file_env.get("SUBJECT_TEMPLATE") or os.getenv("SUBJECT_TEMPLATE") or "通知"
BODY_TEMPLATE = _file_env.get("BODY_TEMPLATE") or os.getenv("BODY_TEMPLATE") or "{name} 您好，附件为您的文件，请查收。"
LOG_MODE = (_file_env.get("LOG_MODE") or os.getenv("LOG_MODE") or "minimal").lower()  # minimal|detailed

print("🚀 邮件批量发送任务启动，直接读取 contacts.xlsx 所有联系人")

contacts_df = pd.read_excel("contacts.xlsx")
names = contacts_df["姓名"].tolist()
emails = contacts_df["邮箱地址"].tolist()

log_entries = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://outlook.office.com/mail/")
    page.wait_for_timeout(5000)

    for idx, (name, email) in enumerate(tqdm(zip(names, emails), total=len(names), desc="📤 发送中")):
        attachment_path = os.path.abspath(os.path.join("attachments", f"{name}.pdf"))
        status = "✅ 成功"

        try:
            page.goto("https://outlook.office.com/mail/inbox")
            page.wait_for_timeout(2000)
            page.locator("button:has-text('New mail')").first.click()
            page.wait_for_timeout(2000)

            page.get_by_label("To", exact=True).fill(email)
            page.keyboard.press("Enter")
            page.wait_for_timeout(800)

            subject = SUBJECT_TEMPLATE.format(name=name)
            page.get_by_placeholder("Add a subject").fill(subject)
            page.wait_for_timeout(500)

            body = BODY_TEMPLATE.format(name=name)
            page.locator("div[aria-label*='Message body']").click()
            page.keyboard.type(body)
            page.wait_for_timeout(1000)

            # 明确指定第2个input[type='file']元素上传，确保稳定性
            file_input = page.locator("input[type='file']").nth(1)
            file_input.set_input_files(attachment_path)
            print(f"✅ 附件上传成功：{name}")
            page.wait_for_timeout(3000)

            # 发送邮件
            page.locator("button:has-text('Send')").first.click()
            status = "✅ 邮件已发送"
            page.wait_for_timeout(3000)

        except Exception as e:
            status = f"❌ 邮件发送失败：{e}"
            print(status)

        if LOG_MODE == "detailed":
            log_entries.append([name, email, attachment_path, status])
        else:
            # minimal 模式不记录个人信息，仅记录索引与状态
            log_entries.append([idx, status])

    browser.close()

    if LOG_MODE == "detailed":
        log_df = pd.DataFrame(log_entries, columns=["姓名", "邮箱", "附件路径", "状态"])
        suffix = "detailed"
    else:
        log_df = pd.DataFrame(log_entries, columns=["序号", "状态"])
        suffix = "minimal"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name = f"send_log_final_{suffix}_{timestamp}.csv"
    log_df.to_csv(log_name, index=False)
    print(f"📄 邮件发送日志已保存为 {log_name}")
