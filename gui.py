# 导入内置GUI库tkinter（Python3自带，无需额外安装）
import tkinter as tk
from tkinter import Label, Button

# 1. 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("Hello GUI")
# 设置窗口初始大小（宽x高）
root.geometry("300x150")

# 2. 添加Hello World文本标签
label = Label(root, text="Hello World!", font=("Arial", 14))
# 让标签在窗口中居中显示（grid是简单的布局方式）
label.grid(row=0, column=0, padx=50, pady=30)

# 3. 定义按钮点击事件（关闭窗口=结束程序）
def close_window():
    root.destroy()  # 销毁主窗口，程序终止

# 4. 添加按钮，绑定点击事件
close_btn = Button(root, text="close", command=close_window, font=("Arial", 12))
close_btn.grid(row=1, column=0)

# 5. 启动GUI循环（让窗口持续显示，等待用户操作）
root.mainloop()
