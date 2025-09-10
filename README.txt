📘 使用说明：基于 Playwright 的 Outlook Web 批量发送（支持 MFA）

本项目演示如何使用浏览器自动化从本地 Excel 通讯录与按人拆分的 PDF 附件，批量发送邮件。仓库不包含任何真实人员信息或凭证。

—

🔧 环境准备
- 安装依赖（Python 3.9+）：
  pip install pandas playwright tqdm PyPDF2
  playwright install

- 可选：创建并编辑 .env（不提交到仓库），也可参考 .env.example：
  SUBJECT_TEMPLATE=通知
  BODY_TEMPLATE={name} 您好，附件为您的文件，请查收。
  LOG_MODE=minimal

  说明：
  - SUBJECT_TEMPLATE、BODY_TEMPLATE 可使用 {name} 占位符
  - LOG_MODE：minimal（默认，不记录姓名/邮箱），detailed（记录姓名/邮箱/附件路径）

—

🗂️ 数据准备（请勿提交任何真实数据到公共仓库）
- Excel：contacts.xlsx，至少包含两列：
  - 姓名
  - 邮箱地址
- 附件目录：attachments/，每人的 PDF 命名为 姓名.pdf
- 如需从整份 PDF 拆分，可运行 split_pdf_by_contacts.py

—

🚪 第一次登录并保存会话
python 1_login_and_save_state_WAIT.py
按提示在浏览器内完成登录与验证，完成后回车保存 state.json（已在 .gitignore 中忽略）。

—

📤 发送邮件
python send_script_final.py
脚本读取 contacts.xlsx 与 attachments/，并使用 state.json 的登录状态在 Outlook Web 端发送邮件。

—

📄 日志
- minimal：仅记录序号与状态（默认，避免包含个人信息）
- detailed：记录姓名、邮箱、附件路径与状态
日志文件保存为 send_log_final_{minimal|detailed}_YYYYMMDD_HHMMSS.csv

—

📑 拆分 PDF（可选）
python split_pdf_by_contacts.py
按 contacts.xlsx 的行序将 master.pdf 拆分为 attachments/目录下的 姓名.pdf。

—

🔐 安全与合规
- 不要将 contacts.xlsx、attachments/、state.json、真实日志提交到公共仓库
- .gitignore 已忽略上述文件/目录，示例配置使用 .env.example
- 使用 .env 配置模板，不在代码中硬编码真实措辞或敏感数据
