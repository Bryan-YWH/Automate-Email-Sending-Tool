from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://outlook.office.com/mail/")
    
    print("✅ 请手动登录 Outlook（包括验证器验证），登录成功后回到终端按 Enter 键继续…")
    input("⏸ 等待你登录完成（按 Enter 继续）")

    context.storage_state(path="state.json")  # 保存登录状态
    browser.close()
    print("✅ 登录状态已保存为 state.json")
