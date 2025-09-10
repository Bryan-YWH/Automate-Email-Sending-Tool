import os
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

# 文件路径配置
contacts_path = "contacts.xlsx"
master_pdf_path = "master.pdf"
attachments_dir = "attachments"

# 读取联系人（可选 .head(3) 做测试）
df = pd.read_excel(contacts_path)
names = df["姓名"].tolist()

# 读取 master.pdf
reader = PdfReader(master_pdf_path)

# 检查页数是否匹配
assert len(reader.pages) >= len(names), "❌ PDF 页数不足，无法为每位联系人生成对应附件"

# 确保输出目录存在
os.makedirs(attachments_dir, exist_ok=True)

# 拆分 PDF：每页保存为 {姓名}.pdf
for i, name in enumerate(names):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])
    output_path = os.path.join(attachments_dir, f"{name}.pdf")
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

print(f"✅ 已成功为 {len(names)} 位联系人生成 PDF，保存在 {attachments_dir}/ 文件夹中")
