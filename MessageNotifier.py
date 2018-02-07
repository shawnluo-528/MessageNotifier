# coding: utf-8
# Author: Luo Shawn <shawnluo528@outlook.com>
import win32serviceutil
import win32service
import win32event
from socket import *
import Tkinter

NOTIFIER_PORT = 58008


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    # print(size)
    root.geometry(size)


def show_msg(title, msg):
    root = Tkinter.Tk()
    root.wm_attributes('-topmost', 1)
    center_window(root, 300, 200)
    l = Tkinter.Label(root, text=title, bg="pink", font=("Arial", 12), width=40, height=5)
    l.pack(side=Tkinter.TOP)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    l = Tkinter.Label(root, text=msg, bg="pink", font=("Arial", 12), width=40, height=5)
    l.pack(side=Tkinter.TOP)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    root.mainloop()


class MessageNotifier(object):
    def __init__(self):
        self.ADDR = ('', NOTIFIER_PORT)
        self.udpServer = socket(AF_INET, SOCK_DGRAM)
        self.udpServer.bind(self.ADDR)
        self.run()

    def __del__(self):
        self.udpServer.close()

    def run(self):
        import time
        print('Start Message Notifier Service.')
        while True:
            data, addr = self.udpServer.recvfrom(1024)
            if data:
                show_msg(addr, data)
            else:
                time.sleep(1)


def notify(message, ip='localhost'):
    try:
        udpClient = socket(AF_INET, SOCK_DGRAM)
        udpClient.sendto(message, (ip, NOTIFIER_PORT))
        udpClient.close()
    except:
        print('Notify Failed.')


if __name__ == '__main__':
    MessageNotifier()
