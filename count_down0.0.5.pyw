import time
import threading
import tkinter as tk

begin_content = '''global data
global font
global color
global background
global toolwindow
global alpha
global transparentcolor
global topmost
global overrideredirect
'''
content = '''data = (
# (enent,goal_time),   格式 例子：('高考', '2022-6-7 0:0:0'),
('高考', '2022-6-7 0:0:0'),
('高考2', '2023-6-7 0:0:0'),
)  # 添加事件

# 是 True    否 False
font = ('黑体', 20)  # 字体 字号
color = 'red'  # 字体颜色
background = 'white'  # 背景色
toolwindow = True  # 是否使用工具窗口
alpha = 0.75  # 窗口透明度(0.0~1.0)  数值越小窗口透明度越高
transparentcolor = (True, 'white') # 是否使用及设定透明色
topmost = True  # 是否把窗口置顶
overrideredirect = True  # 是否隐藏掉窗口边框和标题栏
'''





# threading.Thread(target=self.show_window).start() # , args=(old_verson, ))
# event = '高考'
# goal_time = 1654556400  # 时间戳 2022-06-7 7:0:0 https://www.toolnb.com/tools/getTimestamp.html
version = '0.0.5'
f = '%Y-%m-%d %H:%M:%S'  # 格式
# time.mktime(time.strptime('2022-6-7 7:0:0', f))
data_file = 'count_down%s_data.txt' % version

def read_data():
    try:
        with open(data_file, mode='r', encoding='utf-8') as file:
            new_content = file.read()
            exec(begin_content + new_content)
    except:
        exec(begin_content + content)
        with open(data_file, mode='w', encoding='utf-8') as file:
            file.write(content)

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

def change():
    global label
    # print(get_information())
    
    while True:
        try:
            label['text'] = get_information()
            # if overrideredirect:
            #     root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()) )
            # else:
            #     root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()-20) )
            if time.time() - enter_time > 1:
                root.overrideredirect(overrideredirect)
            time.sleep(1)
        except:
            print('error!')
            break
    print('exit...')

def main():
    read_data()
    global root
    root = tk.Tk()
    root.title('珍惜时间·不留遗憾')
    root.resizable(0,0)  # 禁止调节窗口大小
    root["background"] = 'white'
    # print(root.winfo_width(), root.winfo_height())
    # if not overrideredirect:
    #     root.geometry('+%i+0' % (root.winfo_screenwidth()-170) )
    # print(root.winfo_width(), root.winfo_height())
    root.geometry('+%i+0' % (root.winfo_screenwidth()-170) )
    
    global label
    label = tk.Label(
        root,
        text=get_information(),  # '程序正在加载中...',
        font=font,
        fg=color,
        bg=background,
        )
    label.pack(padx=5, pady=5)
    
    
    def StartMove(event):
        global x, y
        x = event.x
        y = event.y
    '''
    def StopMove(event):
        x = None
        y = None
    '''
    def OnMotion(event):
        global x, y
        deltax = event.x - x
        deltay = event.y - y
        _x = root.winfo_x() + deltax
        _y = root.winfo_y() + deltay
        root.geometry("+%s+%s" % (_x, _y))
    
    root.bind("<ButtonPress-1>", StartMove)
    # root.bind("<ButtonRelease-1>", StopMove)
    root.bind("<B1-Motion>", OnMotion)
    root.bind('<Button-3>', lambda event:exit()) # 右键单击事件
    
    global enter_time # 鼠标进入窗口的时间
    enter_time = time.time()
    
    def enter(event):
        global enter_time
        root.overrideredirect(False)
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
