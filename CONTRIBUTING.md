# 贡献指南

感谢您考虑为这个项目做出贡献！

## 如何贡献

### 报告问题
- 使用 GitHub Issues 报告 bug 或提出功能请求
- 请提供详细的复现步骤和环境信息

### 提交代码
1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add some amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 创建 Pull Request

### 代码规范
- 遵循 PEP 8 Python 代码风格
- 添加适当的注释和文档字符串
- 确保代码通过基本测试

### 安全注意事项
- **永远不要**提交包含真实个人信息的文件
- 使用 `.env` 文件进行本地配置，不要提交到仓库
- 在提交前检查是否包含敏感信息

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/Bryan-WH/automatic_email_sending_script.git
cd automatic_email_sending_script

# 安装依赖
pip install -r requirements.txt
playwright install

# 创建本地配置
cp .env.example .env
# 编辑 .env 文件进行配置
```

## 测试
- 使用 `playwright_browser_test.py` 验证浏览器环境
- 确保所有脚本在测试环境中正常运行

感谢您的贡献！
