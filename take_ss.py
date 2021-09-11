import win32gui
import pyscreenshot as ImageGrab


def find_window(name):
    def window_enum_handler(hwnd, resultList):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

    def get_app_list(handles=[]):
        mlst=[]
        win32gui.EnumWindows(window_enum_handler, handles)
        for handle in handles:
            mlst.append(handle)
        return mlst

    appwindows = get_app_list()
    flag = 0
    for i in range(len(appwindows)):
        for j in range(0,2):
            if name in str(appwindows[i][j]):
                windowTcap = appwindows[i]
                flag = 1
    windowName = windowTcap[1]
    windowNum = windowTcap[0]

    return windowName,windowNum

# x,y=find_window("WhatsApp")
# print(x,y)
# handle = win32gui.FindWindow(None, x)
# win32gui.SetForegroundWindow(y)
# im = ImageGrab.grab()
# # save image file
# im.save("fullscreen.png")
