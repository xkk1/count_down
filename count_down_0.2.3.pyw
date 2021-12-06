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
这是您让我引以骄傲的之一！
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
version = '0.2.3'
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

try:
    import win32api, win32con, win32gui_struct, win32gui
    import os, tkinter as tk

    class SysTrayIcon (object):
        '''SysTrayIcon类用于显示任务栏图标'''
        QUIT = 'QUIT'
        SPECIAL_ACTIONS = [QUIT]
        FIRST_ID = 5320
        def __init__(s, icon, hover_text, menu_options, on_quit, tk_window = None, default_menu_index=None, window_class_name = None):
            '''
            icon         需要显示的图标文件路径
            hover_text   鼠标停留在图标上方时显示的文字
            menu_options 右键菜单，格式: (('a', None, callback), ('b', None, (('b1', None, callback),)))
            on_quit      传递退出函数，在执行退出时一并运行
            tk_window    传递Tk窗口，s.root，用于单击图标显示窗口
            default_menu_index 不显示的右键菜单序号
            window_class_name  窗口类名
            '''
            s.icon = icon
            s.hover_text = hover_text
            s.on_quit = on_quit
            s.root = tk_window

            menu_options = menu_options + (('退出', None, s.QUIT),)
            s._next_action_id = s.FIRST_ID
            s.menu_actions_by_id = set()
            s.menu_options = s._add_ids_to_menu_options(list(menu_options))
            s.menu_actions_by_id = dict(s.menu_actions_by_id)
            del s._next_action_id

            s.default_menu_index = (default_menu_index or 0)
            s.window_class_name = window_class_name or "SysTrayIconPy"

            message_map = {win32gui.RegisterWindowMessage("TaskbarCreated"): s.restart,
                           win32con.WM_DESTROY : s.destroy,
                           win32con.WM_COMMAND : s.command,
                           win32con.WM_USER+20 : s.notify ,}
            # 注册窗口类。
            wc = win32gui.WNDCLASS()
            wc.hInstance = win32gui.GetModuleHandle(None)
            wc.lpszClassName = s.window_class_name
            wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
            wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
            wc.hbrBackground = win32con.COLOR_WINDOW
            wc.lpfnWndProc = message_map #也可以指定wndproc.
            s.classAtom = win32gui.RegisterClass(wc)

        def activation(s):
            '''激活任务栏图标，不用每次都重新创建新的托盘图标'''
            hinst = win32gui.GetModuleHandle(None)# 创建窗口。
            style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
            s.hwnd = win32gui.CreateWindow(s.classAtom, 
                                           s.window_class_name, 
                                           style,
                                           0, 0, 
                                           win32con.CW_USEDEFAULT, 
                                           win32con.CW_USEDEFAULT,
                                           0, 0, hinst, None)
            win32gui.UpdateWindow(s.hwnd)
            s.notify_id = None
            s.refresh(title = '软件已后台！', msg = '点击重新打开', time = 500)
            
            win32gui.PumpMessages()
            s.destroy(exit = 0)
            

        def refresh(s, title = '', msg = '', time = 500):
            '''刷新托盘图标
               title 标题
               msg   内容，为空的话就不显示提示
               time  提示显示时间'''
            hinst = win32gui.GetModuleHandle(None)
            if os.path.isfile(s.icon):
                icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
                hicon = win32gui.LoadImage(hinst, s.icon, win32con.IMAGE_ICON,
                                           0, 0, icon_flags)
            else: # 找不到图标文件 - 使用默认值
                hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

            if s.notify_id: message = win32gui.NIM_MODIFY
            else: message = win32gui.NIM_ADD

            s.notify_id = (s.hwnd, 0, # 句柄、托盘图标ID
                   win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP | win32gui.NIF_INFO,  #托盘图标可以使用的功能的标识
                   win32con.WM_USER + 20, hicon, s.hover_text,  # 回调消息ID、托盘图标句柄、图标字符串
                   msg, time, title,   # 提示内容、提示显示时间、提示标题
                   win32gui.NIIF_INFO  # 提示用到的图标
                   )
            win32gui.Shell_NotifyIcon(message, s.notify_id)

        def show_menu(s):
            '''显示右键菜单'''
            menu = win32gui.CreatePopupMenu()
            s.create_menu(menu, s.menu_options)
            
            pos = win32gui.GetCursorPos()
            win32gui.SetForegroundWindow(s.hwnd)
            win32gui.TrackPopupMenu(menu,
                                    win32con.TPM_LEFTALIGN,
                                    pos[0],
                                    pos[1],
                                    0,
                                    s.hwnd,
                                    None)
            win32gui.PostMessage(s.hwnd, win32con.WM_NULL, 0, 0)

        def _add_ids_to_menu_options(s, menu_options):
            result = []
            for menu_option in menu_options:
                option_text, option_icon, option_action = menu_option
                if callable(option_action) or option_action in s.SPECIAL_ACTIONS:
                    s.menu_actions_by_id.add((s._next_action_id, option_action))
                    result.append(menu_option + (s._next_action_id,))
                else:
                    result.append((option_text,
                                   option_icon,
                                   s._add_ids_to_menu_options(option_action),
                                   s._next_action_id))
                s._next_action_id += 1
            return result

        def restart(s, hwnd, msg, wparam, lparam):
            s.refresh()

        def destroy(s, hwnd = None, msg = None, wparam = None, lparam = None, exit = 1):
            nid = (s.hwnd, 0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
            win32gui.PostQuitMessage(0) # 终止应用程序。
            if exit and s.on_quit: s.on_quit() #需要传递自身过去时用 s.on_quit(s)
            else: s.root.deiconify()  #显示tk窗口

        def notify(s, hwnd, msg, wparam, lparam):
            '''鼠标事件'''
            if lparam==win32con.WM_LBUTTONDBLCLK:# 双击左键
                pass
            elif lparam==win32con.WM_RBUTTONUP:  # 右键弹起
                s.show_menu()
            elif lparam==win32con.WM_LBUTTONUP:  # 左键弹起
                s.destroy(exit = 0)
            return True
            """
            可能的鼠标事件：
              WM_MOUSEMOVE      #光标经过图标
              WM_LBUTTONDOWN    #左键按下
              WM_LBUTTONUP      #左键弹起
              WM_LBUTTONDBLCLK  #双击左键
              WM_RBUTTONDOWN    #右键按下
              WM_RBUTTONUP      #右键弹起
              WM_RBUTTONDBLCLK  #双击右键
              WM_MBUTTONDOWN    #滚轮按下
              WM_MBUTTONUP      #滚轮弹起
              WM_MBUTTONDBLCLK  #双击滚轮
            """
        
        def create_menu(s, menu, menu_options):
            for option_text, option_icon, option_action, option_id in menu_options[::-1]:
                if option_icon:
                    option_icon = s.prep_menu_icon(option_icon)
                
                if option_id in s.menu_actions_by_id:                
                    item, extras = win32gui_struct.PackMENUITEMINFO(text = option_text,
                                                                    hbmpItem = option_icon,
                                                                    wID = option_id)
                    win32gui.InsertMenuItem(menu, 0, 1, item)
                else:
                    submenu = win32gui.CreatePopupMenu()
                    s.create_menu(submenu, option_action)
                    item, extras = win32gui_struct.PackMENUITEMINFO(text = option_text,
                                                                    hbmpItem = option_icon,
                                                                    hSubMenu = submenu)
                    win32gui.InsertMenuItem(menu, 0, 1, item)

        def prep_menu_icon(s, icon):
            #加载图标。
            ico_x = win32api.GetSystemMetrics(win32con.SM_CXSMICON)
            ico_y = win32api.GetSystemMetrics(win32con.SM_CYSMICON)
            hicon = win32gui.LoadImage(0, icon, win32con.IMAGE_ICON, ico_x, ico_y, win32con.LR_LOADFROMFILE)

            hdcBitmap = win32gui.CreateCompatibleDC(0)
            hdcScreen = win32gui.GetDC(0)
            hbm = win32gui.CreateCompatibleBitmap(hdcScreen, ico_x, ico_y)
            hbmOld = win32gui.SelectObject(hdcBitmap, hbm)
            brush = win32gui.GetSysColorBrush(win32con.COLOR_MENU)
            win32gui.FillRect(hdcBitmap, (0, 0, 16, 16), brush)
            win32gui.DrawIconEx(hdcBitmap, 0, 0, hicon, ico_x, ico_y, 0, 0, win32con.DI_NORMAL)
            win32gui.SelectObject(hdcBitmap, hbmOld)
            win32gui.DeleteDC(hdcBitmap)
            
            return hbm

        def command(s, hwnd, msg, wparam, lparam):
            id = win32gui.LOWORD(wparam)
            s.execute_menu_option(id)
            
        def execute_menu_option(s, id):
            menu_action = s.menu_actions_by_id[id]      
            if menu_action == s.QUIT:
                win32gui.DestroyWindow(s.hwnd)
            else:
                menu_action(s)
    
    class Icon:  #调用SysTrayIcon的Demo窗口
        def __init__(s):
            s.SysTrayIcon  = None  # 判断是否打开系统托盘图标

        def main(s):
            #tk窗口
            global root
            s.root = root
            # s.root = tk.Tk()
            # s.root.bind("<Unmap>", lambda event: s.Hidden_window() if s.root.state() == 'iconic' else False) #窗口最小化判断，可以说是调用最重要的一步
            # s.root.protocol('WM_DELETE_WINDOW', s.exit) #点击Tk窗口关闭时直接调用s.exit，不使用默认关闭
            # s.root.resizable(0,0)  #锁定窗口大小不能改变
            # s.root.mainloop()

        def switch_icon(s, _sysTrayIcon, icon = 'D:\\2.ico'):
            #点击右键菜单项目会传递SysTrayIcon自身给引用的函数，所以这里的_sysTrayIcon = s.sysTrayIcon
            #只是一个改图标的例子，不需要的可以删除此函数
            _sysTrayIcon.icon = icon
            _sysTrayIcon.refresh()
            
            #气泡提示的例子
            s.show_msg(title = '图标更换', msg = '图标更换成功！', time = 500)

        def show_msg(s, title = '标题', msg = '内容', time = 500):
            s.SysTrayIcon.refresh(title = title, msg = msg, time = time)

        def Hidden_window(s, icon = 'D:\\1.ico', hover_text = "倒计时"):
            '''隐藏窗口至托盘区，调用SysTrayIcon的重要函数'''

            #托盘图标右键菜单, 格式: ('name', None, callback),下面也是二级菜单的例子
            #24行有自动添加‘退出’，不需要的可删除
            menu_options = (('一级 菜单', None, s.switch_icon),  
                            ('二级 菜单', None, (('更改 图标', None, s.switch_icon), )))

            # s.root.withdraw()   #隐藏tk窗口
            if not s.SysTrayIcon: s.SysTrayIcon = SysTrayIcon(
                                            icon,               #图标
                                            hover_text,         #光标停留显示文字
                                            menu_options,       #右键菜单
                                            on_quit = s.exit,   #退出调用
                                            tk_window = s.root, #Tk窗口
                                            )
            s.SysTrayIcon.activation()
            # s.root.deiconify()

        def exit(s, _sysTrayIcon = None):
            save_exit()
            s.root.destroy()
            print ('exit...')
    ifIcon = True
except:
    ifIcon = False
    print("不支持系统托盘")

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

    if ifIcon:
        icon = Icon()
        icon.main()
        icon.Hidden_window()
        
        # root.deiconify()
    
    t =  threading.Thread(target=change) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    
    root.mainloop()


if __name__ == '__main__':
    main()
