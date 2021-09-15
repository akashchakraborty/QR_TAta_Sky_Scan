from scan_qr import*
from stream_parse import*
from take_ss import*

from PIL import Image
from pyzbar.pyzbar import decode
import win32gui
import pyscreenshot as ImageGrab
import time

def main(name):
    x,y=find_window(name)
    image = "test.png"
    scan_data = scan(image)
    data_out = parse_string(scan_data)
    return data_out


banner ="""

# ╦ ╦┌─┐┬  ┬  ┌─┐┬  ┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗ ╦═╗  ╔═╗┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐  ╦┬─┐┌┬┐┌─┐┌┬┐┌─┐
# ╠═╣├┤ │  │  │ ││  │││├┤ │  │  │ ││││├┤    │ │ │  ║═╬╗╠╦╝  ╚═╗│  ├─┤││││││├┤ ├┬┘  ║├┬┘ ││├┤  │ │ │
# ╩ ╩└─┘┴─┘┴─┘└─┘o  └┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╚═╝╚╩╚═  ╚═╝└─┘┴ ┴┘└┘┘└┘└─┘┴└─  ╩┴└──┴┘└─┘ ┴ └─┘

# PLEASE DONT KEEP THE QR CONTAINING WINDOW MINIMIZED
"""
print(banner)
time.sleep(2)

out = main("Storm")
print(out)



# CHOOSE THE CORRECT NUMBER:

# 1. STORM
# 2. ZOOM
# 3. WHATS APP
# 4. OTHERS



# """

# print(banner)
# choice = str(input())

# if choice == "1":
#     out = main("storm")
# elif choice == "2":
#     out = main("Zoom")   
# if choice == "3":
#     out = main("WhatsApp")
# else:
#     print("WRITE THE NAME IF NONE OF THE ABOVE")
#     cc = input()
#     out = main(cc)
    
# print(out)
