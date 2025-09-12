# Outlook Web 批量邮件发送工具

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

基于 Playwright 的自动化邮件发送解决方案，支持企业邮箱 MFA 认证，可批量发送个性化邮件与附件。

[快速开始](#快速开始) • [使用说明](#使用说明) • [安全注意事项](#安全注意事项) • [许可证](#许可证)

</div>

---

## 主要特性

| 特性 | 描述 |
|------|------|
| **安全认证** | 支持企业邮箱 MFA 多因子认证 |
| **Excel 集成** | 从 Excel 文件读取联系人信息 |
| **附件支持** | 自动上传按姓名命名的 PDF 附件 |
| **模板化** | 可配置邮件主题和正文模板 |
| **灵活日志** | 支持详细/最小化日志模式 |
| **隐私保护** | 默认不记录敏感个人信息 |
| **环境配置** | 通过 .env 文件管理配置 |

---

## 快速开始

### 前置要求

- Python 3.8 或更高版本
- 企业邮箱账户（支持 MFA）
- Excel 格式的联系人文件

### 1. 安装依赖

```bash
# 克隆项目
git clone git@github.com:Bryan-WH/automatic_email_sending_script.git
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
nano .env  # 或使用您喜欢的编辑器
```

#### 配置说明

| 配置项 | 描述 | 示例 |
|--------|------|------|
| `SUBJECT_TEMPLATE` | 邮件主题模板，支持 `{name}` 占位符 | `"您好 {name}，请查收重要文件"` |
| `BODY_TEMPLATE` | 邮件正文模板，支持 `{name}` 占位符 | `"尊敬的 {name}，附件是您的专属文件..."` |
| `LOG_MODE` | 日志模式 | `minimal` 或 `detailed` |

### 3. 准备数据

> ⚠️ **重要提醒**：请勿将真实数据提交到公共仓库

#### 文件结构
```
project/
├── contacts.xlsx          # 联系人文件
├── attachments/           # 附件目录
│   ├── 张三.pdf
│   ├── 李四.pdf
│   └── ...
└── master.pdf            # 原始PDF文件（可选）
```

#### 联系人文件格式

创建 `contacts.xlsx`，包含以下列：

| 列名 | 说明 | 示例 |
|------|------|------|
| `姓名` | 收件人姓名 | 张三 |
| `邮箱地址` | 收件人邮箱 | zhangsan@company.com |

### 4. 登录认证

```bash
python 1_login_and_save_state_WAIT.py
```

1. 脚本将自动打开浏览器
2. 按提示完成 Outlook 登录
3. 完成 MFA 验证
4. 完成后按回车保存登录状态

### 5. 发送邮件

```bash
python send_script_final.py
```

脚本将自动：
- 读取联系人信息
- 匹配对应附件
- 批量发送个性化邮件

---

## 使用说明

### 日志模式

| 模式 | 描述 | 记录内容 |
|------|------|----------|
| `minimal` | 最小化模式（默认） | 序号、状态、时间戳 |
| `detailed` | 详细模式 | 姓名、邮箱、附件路径、状态 |

**日志文件格式**：`send_log_final_{mode}_{timestamp}.csv`

### PDF 拆分工具

```bash
python split_pdf_by_contacts.py
```

按 `contacts.xlsx` 的行序将 `master.pdf` 拆分为个人 PDF 文件。

---

## 安全注意事项

<div align="center">

🛡️ **安全第一** 🛡️

</div>

- ✅ 使用 `.env` 文件管理配置，不提交到仓库
- ✅ `.gitignore` 已配置忽略敏感文件
- ✅ 默认使用最小化日志模式
- ❌ 不要提交包含真实个人信息的文件
- ❌ 不要在代码中硬编码敏感信息

---

## 项目结构

```
automatic_email_sending_script/
├── 📄 README.md                    # 项目说明文档
├── 📄 requirements.txt             # Python 依赖
├── 📄 LICENSE                      # MIT 许可证
├── 📄 CONTRIBUTING.md              # 贡献指南
├── 📄 CONTACTS_SCHEMA.md           # 联系人文件格式说明
├── 🐍 1_login_and_save_state_WAIT.py    # 登录认证脚本
├── 🐍 send_script_final.py              # 主发送脚本
├── 🐍 split_pdf_by_contacts.py          # PDF 拆分工具
├── 🐍 verify_login_identity.py          # 登录验证工具
└── 🐍 playwright_browser_test.py        # 浏览器测试脚本
```

---

## 贡献

我们欢迎各种形式的贡献！

- 报告 Bug
- 提出新功能建议
- 改进文档
- 提交代码修复

详见 [贡献指南](CONTRIBUTING.md)

---

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个星标！**

Made with ❤️ by [Bryan-WH](https://github.com/Bryan-WH)

</div>
