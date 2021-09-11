from scan_qr import*
from stream_parse import*
from take_ss import*

from PIL import Image
from pyzbar.pyzbar import decode
import win32gui
import pyscreenshot as ImageGrab

def main(name):
    x,y=find_window(name)
    handle = win32gui.FindWindow(None, x)

    win32gui.SetForegroundWindow(y)
    im = ImageGrab.grab()

    # save image file
    im.save("fullscreen.png")
    image = "fullscreen.png"
    scan_data = scan(image)
    data_out = parse_string(scan_data)
    return data_out

out = main("WhatsApp")
print(out)
