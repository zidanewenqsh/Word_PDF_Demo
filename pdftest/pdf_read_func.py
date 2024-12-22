from PyPDF2 import PdfReader

def get_pdf_page_count(file_path):
    """
    获取 PDF 文件的总页数
    :param file_path: PDF 文件路径
    :return: 总页数
    """
    try:
        # 打开 PDF 文件
        reader = PdfReader(file_path)

        # 获取总页数
        total_pages = len(reader.pages)
        return total_pages
    except Exception as e:
        print(f"读取 PDF 文件时出错: {e}")
        return None

# 示例调用
# file_path = "1729_ftp.pdf"
# page_count = get_pdf_page_count(file_path)
# if page_count is not None:
#     print(f"PDF 文件的总页数是: {page_count}")
# pdf_files = ["1729_ftp.pdf", "2869_ftp.pdf", "9422_ftp.pdf", "9436_ftp.pdf"]
pdf_files = ["1729_ftp.pdf", "9422_ftp.pdf", "9436_ftp.pdf"]
for file in pdf_files:
    page_count = get_pdf_page_count(file)
    if page_count is not None:
        print(f"{file} 的总页数是: {page_count}")
