from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_pages(input_file, pages_per_split):
    """
    按指定页数拆分 PDF 文件。
    """
    # 读取 PDF 文件
    reader = PdfReader(input_file)
    total_pages = len(reader.pages)
    print(f"总页数: {total_pages}")
    
    # 创建输出文件名的模板
    base_name = input_file.replace('.pdf', '')
    
    # 按指定页数进行拆分
    for start_page in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        end_page = min(start_page + pages_per_split, total_pages)
        
        # 添加页数范围内的页面到新文件
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 生成拆分后的文件名
        output_file = f"{base_name}_part_{start_page // pages_per_split + 1}.pdf"
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"生成文件: {output_file}，包含页数: {start_page + 1} - {end_page}")
    
    print("PDF 拆分完成！")

# 使用示例
split_pdf_by_pages("example.pdf", pages_per_split=2)
