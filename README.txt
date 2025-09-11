# Outlook Web批量邮件发送工具

基于Playwright的自动化邮件发送解决方案，支持企业邮箱MFA认证，可批量发送个性化邮件与附件。

## 主要特性

- 安全认证：支持企业邮箱MFA多因子认证
- Excel 集成：从Excel文件读取联系人信息
- 附件支持：自动上传按姓名命名的PDF附件
- 模板化：可配置邮件主题和正文模板
- 灵活日志：支持详细/最小化日志模式
- 隐私保护：默认不记录敏感个人信息
- 环境配置：通过.env文件管理配置

## 快速开始

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/Bryan-WH/automatic_email_sending_script.git
cd automatic_email_sending_script

# 安装 Python 依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install
```

### 2. 配置环境

```bash
# 复制配置模板
cp .env.example .env

# 编辑配置文件
nano .env
```

配置说明：
- `SUBJECT_TEMPLATE`：邮件主题模板，支持 `{name}` 占位符
- `BODY_TEMPLATE`：邮件正文模板，支持 `{name}` 占位符  
- `LOG_MODE`：日志模式（`minimal` 或 `detailed`）

### 3. 准备数据

重要：请勿将真实数据提交到公共仓库

- 联系人文件：创建 `contacts.xlsx`，包含列：
  - `姓名`
  - `邮箱地址`
- 附件目录：创建 `attachments/` 文件夹，将 PDF 文件命名为 `姓名.pdf`
- PDF 拆分（可选）：使用 `split_pdf_by_contacts.py` 从 `master.pdf` 拆分

### 4. 登录认证

```bash
python 1_login_and_save_state_WAIT.py
```

按提示在浏览器中完成登录和 MFA 验证，完成后按回车保存登录状态。

### 5. 发送邮件

```bash
python send_script_final.py
```

脚本将自动读取联系人信息并批量发送邮件。

## 使用说明

### 日志模式

- minimal（默认）：仅记录序号和状态，保护隐私
- detailed：记录姓名、邮箱、附件路径和状态

日志文件格式：`send_log_final_{mode}_{timestamp}.csv`

### PDF 拆分工具

```bash
python split_pdf_by_contacts.py
```

按 `contacts.xlsx` 的行序将 `master.pdf` 拆分为个人 PDF 文件。

## 安全注意事项

- 使用`.env`文件管理配置，不提交到仓库
- `.gitignore`已配置忽略敏感文件
- 默认使用最小化日志模式
- 不要提交包含真实个人信息的文件
- 不要在代码中硬编码敏感信息

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 贡献

欢迎提交 Issue 和 Pull Request！详见 [贡献指南](CONTRIBUTING.md)。