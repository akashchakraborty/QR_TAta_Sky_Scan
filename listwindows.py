import win32gui
import pyscreenshot as ImageGrab


def find_window():
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
    
    return appwindows


windows = find_window()
print(windows)