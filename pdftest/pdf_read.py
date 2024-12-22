from PyPDF2 import PdfReader

# 打开PDF文件
file_path = "1729_ftp.pdf"
reader = PdfReader(file_path)

# 获取总页数
print(f"总页数: {len(reader.pages)}")

# 提取某一页的文本
page = reader.pages[0]  # 第1页（索引从0开始）
print(f"第一页文本:\n{page.extract_text()}")
