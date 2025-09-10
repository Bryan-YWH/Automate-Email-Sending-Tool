from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    input("✅ 浏览器已打开 example.com，请确认是否弹出窗口，按 Enter 关闭浏览器…")
    browser.close()
