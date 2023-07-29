# -*- coding: utf-8 -*-
'''
@Time    : 2022/11/30 11:56
@Author  : Celeste
@File    : exe_tool.py

'''

# 导入tkinter包，定义别名为tk
import os.path
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import messagebox
from xmindparser import xmind_to_dict
# -*- coding: utf-8 -*-
'''
@Time    : 2022/11/30 11:54
@Author  : Celeste
@File    : count_xmind.py

'''

# 读取xmind文件

# pyinstaller -F -w F:\AtoTool_file\xmExc\xmExc_tool.py -i F:\AtoTool_file\xmExc\xmie.ico

class func():

    def __init__(self, xmindfile):
        self.count1 = 0
        self.xmindfile = xmindfile

    # 单独对story进行返回
    def get_story(self):
        out = xmind_to_dict(self.xmindfile)
        story = out[0]['topic']['topics']
        return story


# 定义Application类表示应用/窗口，继承Frame类
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.path = tk.StringVar()  # 获取xmind文件路径
        self.count1 = tk.StringVar()  # 计算xmind文件的用例数
        # 创建控件，调用后面定义的createWidgets方法
        self.createWidgets()
    def selectPath(self):

        # 从本地选择一个xmind文件，并返回文件的目录
        self.filename = tk.filedialog.askopenfilename()
        if self.filename.endswith('xmind'):
            self.path.set(self.filename)
        else:
            showinfo(title="提示", message="请选择正确的xmind文件")

    # 创建控件
    def createWidgets(self):
        """生成gui界面"""

        self.clickButton = tk.Button(self, text="请选择xmind文件路径：", width=18,height=1,bg='orange',fg='white',command=self.selectPath)
        # 设定使用grid布局
        self.clickButton.grid(row=1, column=3)
        # 创建一个输入框
        self.firstEntry = tk.Entry(self, textvariable=self.path)
        self.firstEntry.grid(row=1, column=4)
        # 创建提交按钮
        self.clickButton = tk.Button(self, text="点击获取总用例数：", width=18,height=1,bg='orange',fg='white',command=self.getvalue)
        # 设定使用grid布局
        self.clickButton.grid(row=5, column=3)
        # 创建一个输入框
        self.firstEntry = tk.Entry(self, textvariable=self.count1)
        self.firstEntry.grid(row=5, column=4)

    def getvalue(self):
        """执行转换excel函数"""

        xmindPath = self.path.get()
        # 获取文件名
        # xmindName = os.path.join(os.path.dirname(__file__),'xmind_excel.xmind')
        self.func = func(xmindPath)
        self.case_count = self.func.count_case(self.func.get_story())
        self.count1.set(self.case_count)
if __name__ == '__main__':

    # 创建一个Application对象app
    app = Application()
    # 设置窗口标题
    app.master.title('xmind用例统计')
    # 设置窗口大小
    app.master.geometry("500x400")

    def QueryWindow():
        # 显示一个警告信息，点击确认，销毁窗口
        if messagebox.showwarning("二次确认", "确认关闭吗？"):
            # 这里必须使用destory()关闭窗口
            # root_window.destory()
            app.master.quit()
            # 使用协议机制与窗口交互，并回调用户自定义的函数
    # 定义回调函数，当用户点击窗口×退出时，执行用户自定义的函数
    app.master.protocol('WM_DELETE_WINDOW', QueryWindow)

    # 主循环开始
    app.mainloop()
