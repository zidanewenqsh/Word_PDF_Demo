from PyPDF2 import PdfReader, PdfWriter

# 打开PDF文件
file_path = "1729_ftp.pdf"
reader = PdfReader(file_path)

# 拆分PDF
for page_number in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[page_number])
    
    # 保存每页为单独的PDF文件
    output_file = f"page_{page_number + 1}.pdf"
    with open(output_file, "wb") as output:
        writer.write(output)
    print(f"已保存：{output_file}")
