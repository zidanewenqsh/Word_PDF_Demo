import re
from PyPDF2 import PdfReader, PdfWriter

def sanitize_filename(filename):
    """
    清理文件名中的非法字符，确保文件名符合 Windows 的命名规则。
    :param filename: 原始文件名
    :return: 清理后的文件名
    """
    # 定义 Windows 系统中非法的字符
    illegal_characters = r'[\/:*?"<>|]'
    # 用下划线替换非法字符
    sanitized_filename = re.sub(illegal_characters, "_", filename)
    return sanitized_filename

def split_pdf_by_bookmarks(input_file):
    """
    按书签拆分 PDF 文件（仅处理主书签）。
    :param input_file: 输入 PDF 文件路径
    """
    # 读取 PDF 文件
    reader = PdfReader(input_file)
    bookmarks = reader.outline  # 获取书签列表
    
    # 检查书签是否存在
    if not bookmarks:
        print("此 PDF 文件没有书签，无法按书签拆分。")
        return
    
    # 过滤掉子书签，只保留一级书签
    main_bookmarks = [bookmark for bookmark in bookmarks if not isinstance(bookmark, list)]
    
    print(f"发现一级书签数量: {len(main_bookmarks)}")
    
    # 遍历一级书签，按书签拆分 PDF
    for i, bookmark in enumerate(main_bookmarks):
        # 获取书签的起始页（注意页数从 0 开始）
        start_page = reader.get_destination_page_number(bookmark)
        print(f"书签 {i+1}: {bookmark.title}, 起始页: {start_page + 1}")
        
        # 确定结束页
        end_page = (
            reader.get_destination_page_number(main_bookmarks[i + 1])  # 下一个书签的起始页
            if i + 1 < len(main_bookmarks) else len(reader.pages)  # 如果是最后一个书签，则到文档末尾
        )
        
        # 创建新 PDF
        writer = PdfWriter()
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 清理书签标题，生成合法的文件名
        safe_title = sanitize_filename(bookmark.title)
        
        # 保存拆分的 PDF
        output_file = f"{input_file.replace('.pdf', '')}_part_{i+1}_{safe_title}.pdf"
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"生成文件: {output_file}，包含页数: {start_page + 1} - {end_page}")
    
    print("PDF 按书签拆分完成！")

# 示例调用
input_pdf = "C++ Primer Plus (5th Edition).pdf"
split_pdf_by_bookmarks(input_pdf)


# 示例：按书签拆分
# split_pdf_by_bookmarks("9436_ftp.pdf")