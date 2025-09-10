from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://outlook.office.com/mail/")
    input("✅ 页面加载完成，请手动确认右上角显示的账号是否为目标账号，再回到终端按 Enter 退出 → ")
    browser.close()
