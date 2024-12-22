# # pip install pywin32

# import win32com.client as win32

# # 启动Word应用
# word = win32.Dispatch("Word.Application")
# word.Visible = False  # 设置为False避免显示Word界面

# # 创建一个新的文档
# doc = word.Documents.Add()

# # 插入普通文本
# selection = word.Selection
# selection.TypeText("这是一个插入的公式：")
# selection.TypeParagraph()

# # 使用Range.Formula插入LaTeX格式的公式
# selection.Formula = r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}'

# # 保存文档
# doc.SaveAs(r'example5.docx')
# doc.Close()

# # 退出Word应用
# word.Quit()
