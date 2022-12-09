import tkinter as tk
import random

# 创建应用程序窗口
root = tk.Tk()

# 定义按钮点击处理函数
def on_button_click(event):
    global buttons
    global size

    # 获取点击的按钮
    btn = event.widget

    # 获取按钮的文本（数字）
    num = int(btn['text'])

    # 移除原有的按钮
    for b in buttons:
        b.pack_forget()

    # 创建新的按钮
    buttons = []
    for i in range(num * num):
        b = tk.Button(root, width=10, height=5, font=('Arial', 24),
                      text=str(random.randint(1, num * num)))
        b.bind('<Button-1>', on_button_click)
        buttons.append(b)

    # 按钮按行排列
    for i in range(num):
        for j in range(num):
            buttons[i * num + j].grid(row=i, column=j)

    # 更新按钮组的大小
    size = num


# 初始化按钮组
buttons = []
size = 3

# 创建按钮
for i in range(size * size):
    b = tk.Button(root, width=10, height=5, font=('Arial', 24),
                  text=str(i + 1))
    b.bind('<Button-1>', on_button_click)
    buttons.append(b)

# 按钮按行排列
for i in range(size):
    for j in range(size):
        buttons[i * size + j].grid(row=i, column=j)

# 运行应用程序
root.mainloop()
