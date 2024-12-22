from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_size(input_file, max_size_kb):
    """
    按文件大小拆分 PDF。
    :param input_file: 输入 PDF 文件路径
    :param max_size_kb: 每个拆分文件的最大大小（KB）
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()
    part_number = 0
    current_size = 0

    for page_num, page in enumerate(reader.pages):
        writer.add_page(page)
        
        # 临时保存文件来计算大小
        temp_file = f"temp_part_{part_number}.pdf"
        with open(temp_file, "wb") as temp_pdf:
            writer.write(temp_pdf)
        
        # 检查文件大小
        current_size = os.path.getsize(temp_file) / 1024  # 转换为 KB
        if current_size > max_size_kb:
            # 保存当前部分
            output_file = f"{input_file.replace('.pdf', '')}_part_{part_number}.pdf"
            with open(output_file, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"生成文件: {output_file}，大小: {current_size:.2f} KB")

            # 重置 Writer
            writer = PdfWriter()
            part_number += 1

    # 保存最后一部分
    if writer.pages:
        output_file = f"{input_file.replace('.pdf', '')}_part_{part_number}.pdf"
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"生成文件: {output_file}")

    print("PDF 按大小拆分完成！")

# 示例：按大小拆分
import os
split_pdf_by_size("C++ Primer Plus (5th Edition).pdf", max_size_kb=1024)
