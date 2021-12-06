import time
import threading
import tkinter as tk


data = (
# (enent,goal_time),   格式
('高考1', '2022-6-7 0:0:0'),
('高考2', '2023-6-7 0:0:0'),
)  # 添加事件
toolwindow = True  # 是否使用工具窗口
alpha = 0.9  # 透明度(0.0~1.0)  数值越小窗口透明度越高
topmost = False  # 是否把窗口置顶
overrideredirect = False  # 是否删除标题栏




# threading.Thread(target=self.show_window).start() # , args=(old_verson, ))
event = '高考'
goal_time = 1654556400  # 时间戳 2022-06-7 7:0:0 https://www.toolnb.com/tools/getTimestamp.html

f = '%Y-%m-%d %H:%M:%S'  # 格式
# time.mktime(time.strptime('2022-6-7 7:0:0', f))


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
            if overrideredirect:
                root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()) )
            # else:
            #     root.geometry('+%i+0' % (root.winfo_screenwidth()-root.winfo_width()-20) )
            time.sleep(1)
        except:
            print('error!')
            break
    print('exit...')

def main():
    global root
    root = tk.Tk()
    root.title('珍惜时间·不留遗憾')
    root.resizable(0,0)  # 禁止调节窗口大小
    # print(root.winfo_width(), root.winfo_height())
    if not overrideredirect:
        root.geometry('+%i+0' % (root.winfo_screenwidth()-170) )
    # print(root.winfo_width(), root.winfo_height())
    
    global label
    label = tk.Label(
        root,
        text=get_information(),  # '程序正在加载中...',
        font=('宋体', 20),
        fg='black',
        )
    label.pack(padx=5, pady=5)
    
    root.overrideredirect(overrideredirect)  # 删除标题栏
    root.attributes('-toolwindow', toolwindow)  # 置为工具窗口(没有最大最小按钮)
    root.attributes('-alpha', alpha)  # 透明度(0.0~1.0)
    root.attributes('-topmost', topmost)  # 永远处于顶层
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
