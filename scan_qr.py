from PIL import Image
from pyzbar.pyzbar import decode
def scan(image):
    try:
        data = decode(Image.open(image))
        data = (data[0][0])
        data=data.decode("utf-8")
    except:
        pass
    return data
