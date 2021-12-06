import time
import threading
import tkinter as tk
import random
import tkinter.scrolledtext
import tkinter.messagebox
import os
from sys import exit
import sys
from traceback import format_exc #用于精准的获取错误异常

begin_content = '''global data
global font
global color
global background
global toolwindow
global alpha
global transparentcolor
global topmost
global overrideredirect
global title_bar
global position
global sayings
'''
content = r'''# 我是储存设置数据的文件
# 建议修改前备份一下
data = (
# (enent,goal_time),   格式 例子：('距离2022年高考还有：\n', '2022-6-7 0:0:0'),
('\n距离2022年高考还有：\n', '2022-6-7 0:0:0'),
('\n距离外语听力高考还有：\n', '2022-1-8 0:0:0'),
)  # 添加事件"

sayings="""
把握现在，就是创造未来。
百尺高梧，撑得起一轮月色
数椽矮屋，锁不住五夜书声。
宝剑锋从磨砺出,梅花香自苦寒来。
不为失败找理由，要为成功找方法。
读书改变命运，刻苦成就事业，态度决定一切。
行动是成功的阶梯，行动越多，登得越高。
"""[1:-1]

# 是 True    否 False
font = ('黑体', 36)  # 字体 字号
color = '#ffffff'  # 字体颜色
background = '#000000'  # 背景色
toolwindow = True  # 是否使用工具窗口
alpha = 1.0  # 窗口透明度(0.0~1.0)  数值越小窗口透明度越高
transparentcolor = (True, '#7f7f7f') # 是否使用及设定透明色
topmost = False  # 是否把窗口置顶
overrideredirect = True  # 是否隐藏掉窗口边框和标题栏
title_bar = False    # 是否在鼠标悬停时显示窗口边框和标题栏
position = (0, 0)
'''[:-1]




# threading.Thread(target=self.show_window).start() # , args=(old_verson, ))
# event = '高考'
# goal_time = 1654556400  # 时间戳 2022-06-7 7:0:0 https://www.toolnb.com/tools/getTimestamp.html
version = '0.2.2'
f = '%Y-%m-%d %H:%M:%S'  # 格式
# time.mktime(time.strptime('2022-6-7 7:0:0', f))
data_file = 'count_down%s_data.txt' % version
moved = False

def read_data():
    try:
        with open(data_file, mode='r', encoding='utf-8') as file:
            new_content = file.read()
            exec(begin_content + new_content)
    except:
        exec(begin_content + content)
        with open(data_file, mode='w', encoding='utf-8') as file:
            file.write(content)
def save_exit():
    try:
        with open(data_file, mode='r', encoding='utf-8') as file:
            #new_content = file.read()
            #exec(begin_content + new_content)
            data_list = file.readlines()
        with open(data_file, mode='w', encoding='utf-8') as file:
            #new_content = file.read()
            #exec(begin_content + new_content)
            for data in data_list[:-1]:
                file.write(data)
            file.write("position = (%i, %i)" % (root.winfo_x(), root.winfo_y()))
    except:
        print("save error!")
        print(format_exc())
    exit()
"""
def get_information():
    information = ''  # 初始化
    for event,goal_time in data:
        # print(event)
        goal_time = time.mktime(time.strptime(goal_time, f))
        surplus = goal_time - time.time()  # 剩余
        # 60*60*24 = 86400
        # 60*60 = 3600
        information += '\n距' + event + '还有\n'
        information += '%.0f天\n' % (surplus / 86400)
        information += '%.0f小时\n' % (surplus / 3600)
        information += '%.0f分钟\n' % (surplus / 60)
        information += '%i秒\n' % round(surplus)
    return information[1:-1]
#print(get_information())
"""



def get_information():
    information = ''  # 初始化
    for event,goal_time in data:
        # print(event)
        goal_time = time.mktime(time.strptime(goal_time, f))
        surplus = goal_time - time.time()  # 剩余
        # 60*60*24 = 86400
        # 60*60 = 3600
        information +=  event
        day = int(surplus // 86400)
        hour = int((surplus % 86400) // 3600)
        minute = int((surplus % 3600) // 60)
        second =  int(surplus % 60)
        information += f"{day}天{hour:0>2d}小时{minute:0>2d}分钟{second:0>2d}秒\n"
    return information[:-1]

def change():
    global label
    global moved
    global title_bar
    # print(get_information())
    
    while True:
        try:
            label['text'] = get_information()
            # if overrideredirect:
            #     root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()) )
            # else:
            #     root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()-20) )
            if time.time() - enter_time > 1:
                # root.overrideredirect(overrideredirect)
                if overrideredirect:
                    if title_bar:
                        if moved:
                            moved = False
                            root.overrideredirect(True)
                            _x = root.winfo_x() + 0
                            _y = root.winfo_y() + 30
                            root.geometry("+%s+%s" % (_x, _y))
            time.sleep(1)
        except:
            print('error!')
            print(format_exc())
            break
    print('exit...')

def get_saying():
    global sayings
    saying_list = sayings.split("\n")
    saying = random.choice(saying_list)
    return saying

def show_help():
    """显示帮助"""
    global help_window
    global information_scrolledtext
    information = """帮助正在努力制作中……
当前为内测版
感谢2019级21班陈博提供的图标
制作者:小喾苦
邮箱:3434623263@qq.com"""
    print(information)
        
    try:
        help_window.deiconify()
    except:
        help_window = tk.Tk()
        help_window.title('倒计时-帮助')
        try:  # 尝试设置图标
            help_window.iconbitmap('.\\icon.ico')
        except:
            pass
        
        information_scrolledtext = tkinter.scrolledtext.ScrolledText(
            help_window,
            width=50,
            height=20,
            font=('宋体', 12)
            )  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        # scr.place(x=50, y=50) #滚动文本框在页面的位置
        information_scrolledtext.pack(fill=tk.BOTH, padx=5, pady=5)
        
        information_scrolledtext.insert(tk.INSERT, information)
        help_window.mainloop()

def startup():
    os.system("start shell:startup")
    tkinter.messagebox.showinfo("设置开机自启的方法", """设置开机自启的方法：
1、打开程序所在目录，对主程序右键“创建快捷方式”
2、点击“开机自启目录”打开开机自启目录
3、将创建的快捷方式放到开机自启目录中""")

def restart():
    # os.system('explorer '+ sys.argv[0] + '"')
    """
    def system_restart():
        os.system('"'+ sys.argv[0] + '"&&exit')
    t =  threading.Thread(target=system_restart) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    """
    python = sys.executable
    # os.execl(python, python, * sys.argv)
    os.execl(python, sys.argv[0], * sys.argv)
    save_exit()

def show_set_up():
    """设置窗口"""
    global set_up_window
    global root
    
    try:
        set_up_window.deiconify()
    except:
        # set_up_window = tk.Tk()
        set_up_window = tk.Toplevel(root)
        set_up_window.title('倒计时v%s' % version)
        set_up_window.resizable(0, 0)  # 锁定窗口大小不能改变
        try:  # 尝试设置图标
            set_up_window.iconbitmap('.\\icon.ico')
        except:
            pass
        # set_up_window.mainloop()
        # set_up_window.transient(root)
        frame = tk.Frame(set_up_window)
        frame.pack(padx=80, pady=15)
        button_exit = tk.Button(
            frame,
            text='退出程序',
            font=('宋体', 20),
            command=save_exit,
            )
        button_exit.pack(padx=10, pady=10)

        button_restart = tk.Button(
            frame,
            text='重启程序',
            font=('宋体', 20),
            command=restart,
            )
        button_restart.pack(padx=10, pady=10)
        
        button_show_help = tk.Button(
            frame,
            text='显示帮助',
            font=('宋体', 20),
            command=show_help,
            )
        button_show_help.pack(padx=10, pady=10)
    
        button_data_file = tk.Button(
            frame,
            text='打开数据文件',
            font=('宋体', 20),
            command=lambda : os.system("start " + data_file),
            )
        button_data_file.pack(padx=10, pady=10)
        """
        button_reload = tk.Button(
            frame,
            text='重新加载数据',
            font=('宋体', 20),
            command=read_data,
            )
        button_reload.pack(padx=10, pady=10)
        """
        button_open_path = tk.Button(
            frame,
            text='打开所在路径',
            font=('宋体', 20),
            command=lambda : os.system('explorer "' + os.getcwd() + '"'),
            )
        button_open_path.pack(padx=10, pady=10)

        button_startup = tk.Button(
            frame,
            text='开机自启目录',
            font=('宋体', 20),
            command=startup,
            )
        button_startup.pack(padx=10, pady=10)

def main():
    read_data()
    global root
    root = tk.Tk()
    root.title('珍惜时间·不留遗憾  by 小喾苦')
    root.resizable(0,0)  # 禁止调节窗口大小
    try:  # 尝试设置图标
        root.iconbitmap('.\\icon.ico')
    except:
        pass
    root["background"] = background
    # print(root.winfo_width(), root.winfo_height())
    # if not overrideredirect:
    #     root.geometry('+%i+0' % (root.winfo_screenwidth()-170) )
    # print(root.winfo_width(), root.winfo_height())
    # root.geometry('+%i+0' % (root.winfo_screenwidth()-580) )
    root.geometry("+%i+%i" % position)

    global Label
    try:
        background_img = tk.PhotoImage(file=".//background.png")
        Label = tk.Label(root,
                     image=background_img,
                     compound = tk.CENTER,#关键:设置为背景图片
                     bg="#7f7f7f",
                     )
    except:
        Label = tk.Label(root,
                     bg="#7f7f7f",
                     )
    
    global label
    label = tk.Label(
        Label,
        text=get_information(),  # '程序正在加载中...',
        font=font,
        fg=color,
        bg=background,
        justify=tk.LEFT,  # 字符串进行左对齐
        )
    label.place(x=60, y=50) # (padx=5, pady=5)


    Label.pack()
    global label_saying
    
    label_saying = tk.Label(Label,
                          text=get_saying(),
                          font=('宋体', 16),# 字体和字体大小
                          fg="#ffffff",
                            bg="black",
                          )

    label_saying.place(x=60, y=380)
    
    
    
    def start_move(event):
        global x, y
        x = event.x
        y = event.y
    '''
    def stop_move(event):
        x = None
        y = None
    '''
    def on_motion(event):
        global x, y
        deltax = event.x - x
        deltay = event.y - y
        _x = root.winfo_x() + deltax
        _y = root.winfo_y() + deltay
        root.geometry("+%s+%s" % (_x, _y))
    
    root.bind("<ButtonPress-1>", start_move)
    # root.bind("<ButtonRelease-1>", stop_move)
    root.bind("<B1-Motion>", on_motion)
    # root.bind('<Button-3>', lambda event:exit()) # 右键单击事件
    root.bind('<Button-3>', lambda event:show_set_up()) # 右键单击事件
    
    global enter_time # 鼠标进入窗口的时间
    enter_time = time.time()
    
    def enter(event):
        global enter_time
        global moved
        global title_bar
        # root.overrideredirect(False)
        if overrideredirect:
            if title_bar:
                if not moved:
                    moved = True
                    root.overrideredirect(False)
                    _x = root.winfo_x() + 0
                    _y = root.winfo_y() - 30
                    root.geometry("+%s+%s" % (_x, _y))
        enter_time = time.time()
    
    # def leave(event):
    #     pass
        # time.sleep(1)
        # root.overrideredirect(overrideredirect)
        # if time.time() - enter_time > 3:
        #     root.overrideredirect(overrideredirect)
    
    root.bind('<Enter>', enter) # 鼠标移动到区域 Enter
    # root.bind('<Leave>', leave) # 鼠标离开区域 Leave
    
    root.overrideredirect(overrideredirect)  # 隐藏掉窗口边框和标题栏
    root.attributes('-toolwindow', toolwindow)  # 置为工具窗口(没有最大最小按钮)
    root.attributes('-alpha', alpha)  # 透明度(0.0~1.0)
    root.attributes('-topmost', topmost)  # 永远处于顶层
    if transparentcolor[0]:
        # 这一行可以将所有的白色透明掉
        root.attributes("-transparentcolor", transparentcolor[1])
    
    #root.attributes('-transparentcolor', 'white')  # 使用白色作为透明色
    
    #root.wm_attributes("-toolwindow", toolwindow)  # 置为工具窗口(没有最大最小按钮)
    #root.wm_attributes("-alpha", alpha)  # 透明度(0.0~1.0)
    #root.wm_attributes("-topmost", topmost)  # 永远处于顶层
    
    t =  threading.Thread(target=change) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    
    root.mainloop()


if __name__ == '__main__':
    main()
