from pyzbar import pyzbar
import cv2
from Breader import Breader

if __name__ == "__main__":
    from glob import glob
    reader = Breader('')
    
    barcodes = glob("./img/barcode_*.png")
    for barcode_file in barcodes:
        img = cv2.imread(barcode_file)
        img = reader.decode(img)
        print(reader.scan_data)
        cv2.imshow("img", img)
        cv2.waitKey(0)