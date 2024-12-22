from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_files, output_path):
    """
    合并多个 PDF 文件为一个 PDF 文件
    :param pdf_files: 待合并的 PDF 文件路径列表
    :param output_path: 合并后 PDF 文件的保存路径
    :return: None
    """
    try:
        # 创建 PdfWriter 对象
        writer = PdfWriter()

        # 读取并合并每个 PDF 文件
        for file in pdf_files:
            try:
                # 尝试打开 PDF 文件
                reader = PdfReader(file)
                for page in reader.pages:
                    writer.add_page(page)
                print(f"成功合并: {file}")
            except Exception as e:
                print(f"读取文件 {file} 时出错: {e}")
        
        # 保存合并后的 PDF
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        
        print(f"合并完成！合并文件已保存为: {output_path}")

    except Exception as e:
        print(f"合并过程中发生错误: {e}")

# 示例调用
pdf_files = ["1729_ftp.pdf", "9422_ftp.pdf", "9436_ftp.pdf"]
output_path = "merged.pdf"
merge_pdfs(pdf_files, output_path)
