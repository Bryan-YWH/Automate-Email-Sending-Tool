📘 使用说明：网页版 Outlook 群发邮件（支持 MFA）

1️⃣ 第一次运行，保存登录状态（打开浏览器手动登录）：
   python 1_login_and_save_state.py

2️⃣ 准备好 contacts.xlsx 和 attachments/（每人一个 PDF，命名为“姓名.pdf”）

3️⃣ 自动发送所有邮件：
   python 2_send_outlook_web_emails.py

📌 脚本会使用你之前保存的登录状态文件 state.json 自动登录。
📌 支持所有企业邮箱，只要能登录 https://outlook.office.com/
