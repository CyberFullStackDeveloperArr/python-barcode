from pyzbar.pyzbar import decode
from PIL import Image

def read_barcode(image_path):
    img = Image.open(image_path)
    
    decoded_objects = decode(img)
    
    if not decoded_objects:
        print("Barcode tidak terdeteksi.")
        return None
    
    for obj in decoded_objects:
        print("Tipe:", obj.type)
        print("Data:", obj.data.decode("utf-8"))
        print("Rect:", obj.rect)
        print("====================================")

read_barcode('barcode.png')