from docx import Document

# 打开并读取 Word 文件
doc = Document('example.docx')

# 获取文档中的所有段落
for para in doc.paragraphs:
    print(para.text)
