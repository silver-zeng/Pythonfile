import os  # 关于操作系统的一个python标准库
import tkinter as tk  # gui图形界面化模块
import webbrowser  # 提供了一个高级接口，允许向用户显示基于Web的文档。
import requests
import tkinter.messagebox as mes_box
import PySimpleGUI as sg
from tkinter import ttk
from retrying import retry  # 对同一个操作进行多次尝试


class SetUI(object):
    """
    音乐弹框界面
    """

    def __init__(self, weight=1000, height=600):
        self.ui_weight = weight
        self.ui_height = height
        self.title = "音乐破解软件"
        self.ui_root = tk.Tk(className=self.title)  # 建立主窗口并设置窗口名
        self.ui_url = tk.StringVar()  # StringVar()跟踪变量值的变化，把最新的值显示到界面上
        self.ui_var = tk.IntVar()  # 记录数值.get()获取值， .set()设置值
        self.ui_var.set(1)  # 1为选中，0未选中
        self.show_result = None
        self.song_num = None
        self.response_data = None
        self.song_url = None
        self.song_name = None
        self.song_author = None

    def set_ui(self):
        """
        设置简易ui界面
        :return:
        """
        # Frame空间
        frame_1 = tk.Frame(self.ui_root)  # 可作为其他组件的容器，常用来对组件进行分组Label 标 签，常用来显示单行文本
        frame_2 = tk.Frame(self.ui_root)
        frame_3 = tk.Frame(self.ui_root)
        frame_4 = tk.Frame(self.ui_root)

        # ui界面中菜单设计
        ui_menu = tk.Menu(self.ui_root)  # 创建菜单栏
        # 显示菜单
        self.ui_root.config(menu=ui_menu)
        # 创建子菜单
        file_menu = tk.Menu(ui_menu, tearoff=0)  # Tearoff  默认情况下（tearoff=1 或 True）显示“撕掉元素（‘------------’）
        ui_menu.add_cascade(label='菜单', menu=file_menu)  # 添加子菜单，设置子菜单名称
        # 添加子菜单选项触发单元，command设置触发事件
        file_menu.add_command(label='使用说明', command=lambda: webbrowser.open('www.baidu.com'))
        file_menu.add_command(label='关于作者', command=lambda: webbrowser.open('www.baidu.com'))
        file_menu.add_command(label='退出', command=self.ui_root.quit)  # 退出程序

        # 控件内容设置
        choice_passageway = tk.Label(frame_1, text='请选择音乐搜索通道', padx=10,
                                     pady=10)  # Label：标签组件。主要用																				#于显示文本，添加提示信息等。
        passageway_button1 = tk.Radiobutton(frame_1, text='酷我', variable=self.ui_var, value=1,
                                            width=10, height=3)  # 单选
        passageway_button2 = tk.Radiobutton(frame_1, text='网易云', variable=self.ui_var, value=2,
                                            width=10, height=3)
        passageway_button3 = tk.Radiobutton(frame_1, text='QQ音乐', variable=self.ui_var, value=3,
                                            width=10, height=3)
        passageway_button4 = tk.Radiobutton(frame_1, text='酷狗', variable=self.ui_var, value=4,
                                            width=10, height=3)
        input_link = tk.Label(frame_2, text="请输入歌曲名或歌手")
        # 文本框Entry用于接收输入的数据。文本框Entry的基本格式为：txt = tkinter.Entry(容器名称，width=宽度，文字字体、颜色等）
        entry_style = tk.Entry(frame_2, textvariable=self.ui_url, highlightcolor='Fuchsia',
                               highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play_button = tk.Button(frame_2, text='搜索', font=('楷体', 11), fg='Purple', width=2, height=1,
                                command=self.get_KuWoMusic)
        label3 = tk.Label(frame_2, text=" ")
        # 表格样式
        columns = ("序号", "歌手", "歌曲", "专辑")
        # 设置表格，headings表示显示在顶部，colums是要显示的数据
        self.show_result = ttk.Treeview(frame_3, height=20, show="headings", columns=columns)
        # 下载
        download_button = tk.Button(frame_4, text="下载", font=('楷体', 11), fg='Purple', width=6,
                                    height=1, padx=5, pady=5, command=self.download_music)

        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        choice_passageway.grid(row=0, column=0)
        passageway_button1.grid(row=0, column=1)
        passageway_button2.grid(row=0, column=2)
        passageway_button3.grid(row=0, column=3)
        passageway_button4.grid(row=0, column=4)
        input_link.grid(row=0, column=0)
        entry_style.grid(row=0, column=0)
        label2.grid(row=0, column=2)
        play_button.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        self.show_result.grid(row=0, column=4)
        download_button.grid(row=0, column=4)

        # 设置表头
        self.show_result.heading("序号", text="序号")
        self.show_result.heading("歌曲", text="歌曲")
        self.show_result.heading("歌手", text="歌手")
        self.show_result.heading("专辑", text="专辑")
        # 设置列
        self.show_result.column("序号", width=100, anchor='center')
        self.show_result.column("歌曲", width=200, anchor='center')
        self.show_result.column("歌手", width=300, anchor='center')
        self.show_result.column("专辑", width=400, anchor='center')

        # 鼠标点击
        self.show_result.bind('<ButtonRelease-1>', self.get_song_url)  # 1代表左键，n为2代表中键，n为3代表右键

    @retry(stop_max_attempt_number=5)  # 停止最大尝试次数
    def get_KuWoMusic(self):
        """
        获取QQ音乐
        :return:
        """
        # 清空treeview表格数据
        for item in self.show_result.get_children():  # get_children()函数，其返回的是treeview中的记录号.
            self.show_result.delete(item)
        headers = {  # 传入必要请求头，反爬--------------------------------------------------------
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.2058800930.1642474837; _gid=GA1.2.1174281146.1642474837; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1642490265,1642490289,1642490402,1642498818; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1642499234; kw_token=YK4UZW2UPL",
            "csrf": "YK4UZW2UPL",
            "Host": "www.kuwo.cn",
            "Referer": "http://www.kuwo.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        }
        search_input = self.ui_url.get()  # 得到用户输入内容

        if len(search_input) > 0:
            search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
            """key携带的值，是我们要搜索的值；pn，按照常量，我们猜测，其为页数；rn，我们猜测其为一页显示的数量"""
            search_data = {
                'key': search_input,
                'pn': '1',
                'rn': '80',
                'httpsStatus': '1',
                'reqId': '858597c1-b18e-11ec-83e4-9d53d2ff08ff'
            }
            try:  # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
                self.response_data = requests.get(search_url, params=search_data, headers=headers,
                                                  timeout=20).json()
                songs_data = self.response_data['data']['list']
                if int(self.response_data['data']['total']) <= 0:
                    mes_box.showerror(title='错误', message='搜索:{} 不存在.'.format(search_input))
                else:
                    for i in range(len(songs_data)):
                        self.show_result.insert('', i, values=(i + 1, songs_data[i]['artist'],
                                                               songs_data[i]['name'],
                                                               songs_data[i]['album']))
                    """insert(parent, index, iid=None, **kw)
                        解释：
                        parent : 对于有树栏的Treeview，parent是父节点，对于只是列表栏的Treeview，parent一般为空。
                        index ：插入位置。可以是END或’end’ ，也可以是数字的，如果你想新插入的item(记录)成为第某节点的第一									个，index就设为0，以此类推。
                        iid : 每一行记录（item）的标识符，这个参数，我上面没有讲解，等下，我会专门讲解。
                        **kw ：设置插入的记录（item）所支持属性，"""
            except TimeoutError:
                mes_box.showerror(title='错误', message='搜索超时，请重新输入再搜索！')
        else:
            mes_box.showerror(title='错误', message='未输入需查询的歌曲或歌手，请输入后搜索！')

    def get_song_url(self, event):
        """
        获取下载歌曲的地址
        :param event:
        :return:
        """
        # treeview中的单击左键
        for item in self.show_result.selection():  # 取的选项，要下载的歌曲
            item_text = self.show_result.item(item, "value")  # item获得字典·
            # 获取
            self.song_num = int(item_text[0])
        # 获取下载歌曲的地址
        if self.song_num is not None:
            songs_data = self.response_data['data']['list']
            songs_req_id = self.response_data['reqId']
            songs_rid = songs_data[self.song_num - 1]['rid']
            music_url = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=convert_url3' \
                        '&httpsStatus=1&reqId={}'.format(songs_rid, songs_req_id)
            response_data = requests.get(music_url).json()
            self.song_url = response_data['data'].get('url')
            self.song_name = songs_data[self.song_num - 1]['name']
            self.song_author = songs_data[self.song_num - 1]['artist']
        else:
            mes_box.showerror(title='错误', message='未选择要下载的歌曲，请选择')

    def download_music(self):
        """
        下载音乐
        :return:
        """
        self.progress_bar(100)
        if not os.path.exists('./music'):
            os.mkdir("./music/")
        if self.song_num is not None:
            song_name = self.song_name + '--' + self.song_author + ".mp3"
            try:
                save_path = os.path.join('./music/{}'.format(song_name)) \
                    .replace('\\', '/')
                true_path = os.path.abspath(save_path)
                resp = requests.get(self.song_url)
                with open(save_path, 'wb') as file:
                    file.write(resp.content)
                    mes_box.showinfo(title='下载成功', message='歌曲：%s,保存地址为%s' % (self.song_name,
                                                                                         true_path))
            except Exception:
                mes_box.showerror(title='错误', message='未找到存放歌曲的文件夹')
        else:
            mes_box.showerror(title='错误', message='未选择要下载的歌曲，请选择后下载')

    def progress_bar(self, file_size):
        """
        任务加载进度条
        :param file_size:
        :return:
        """
        # orientation 表示 进度条是横向的或是纵向的。h横向 v纵向（默认）
        # size是窗口尺寸
        layout = [[sg.Text('任务完成进度')],
                  [sg.ProgressBar(file_size, orientation='h', size=(40, 20), key='progressbar')],
                  [sg.Cancel()]]  # 取消按钮

        # window只需将自定义的布局加载出来即可，第一个参数是窗口标题
        window = sg.Window('机器人执行进度', layout)
        # 根据key值获取到进度条
        _progress_bar = window['progressbar']
        for i in range(file_size):  # read读取窗口，返回两个值，一个是事件，一个是值
            event, value = window.read(timeout=10)
            if event == 'Cancel' or event is None:
                break
            _progress_bar.UpdateBar(i + 1)  # 更新进度条

    def ui_center(self):
        """
        UI界面窗口设置：居中
        :return:
        """
        ws = self.ui_root.winfo_screenwidth()  # 获取电脑屏幕的
        hs = self.ui_root.winfo_screenheight()
        x = int((ws / 2) - (self.ui_weight / 2))
        y = int((hs / 2) - (self.ui_height / 2))
        self.ui_root.geometry('{}x{}+{}+{}'.format(self.ui_weight, self.ui_height, x, y))
        # geometry设定主窗口的大小以及位置，当参数值为 None 时表示获取窗口的大小和位置信息。

    def loop(self):
        """
        函数说明：loop等待用户事件
        :return:
        """
        self.ui_root.resizable(False, False)  # 禁止修改窗口大小
        self.ui_center()  # 窗口居中
        self.set_ui()
        self.ui_root.mainloop()  # 进入等待与处理窗口事件


if __name__ == '__main__':
    a = SetUI()  # 定义一个实例
    a.loop()  # 调用函数