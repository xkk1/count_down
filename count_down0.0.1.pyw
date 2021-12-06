import time
import threading
import tkinter as tk


# threading.Thread(target=self.show_window).start() # , args=(old_verson, ))
event = '高考'
goal_time = 1654556400  # 时间戳 2022-06-7 7:0:0 https://www.toolnb.com/tools/getTimestamp.html


def get_information():
    surplus = goal_time - time.time()  # 剩余
    # 60*60*24 = 86400
    # 60*60 = 3600
    information = '距' + event + '还有\n'
    information += '%.0f天\n' % (surplus / 86400)
    information += '%.0f小时\n' % (surplus / 3600)
    information += '%.0f分钟\n' % (surplus / 60)
    information += '%.0f秒' % surplus
    return information

def change():
    global label
    # print(get_information())
    
    while True:
        try:
            label['text'] = get_information()
            time.sleep(1)
        except:
            print('error!')
            break
    print('exit...')

def main():
    root = tk.Tk()
    root.title('珍惜时间·不留遗憾')
    root.resizable(0,0)  # 禁止调节窗口大小
    root.geometry('+%i+0' % (root.winfo_screenwidth()-170) )
    
    global label
    label = tk.Label(
        root,
        text='程序正在加载中...',
        font=('宋体', 20),
        )
    label.pack(padx=5, pady=5)
    
    root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    
    t =  threading.Thread(target=change) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    
    root.mainloop()


if __name__ == '__main__':
    main()
