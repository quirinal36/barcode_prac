import urllib.parse
import urllib.request
import cv2
from Breader import Breader

def saveIntoServer(isbn):
    url = f'http://127.0.0.1:8000/buddy/barcode?data={isbn}'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    while True:
        reader = Breader('')
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        frame = reader.decode(frame)
        
        if len(reader.scan_data) > 1 :
            saveIntoServer(reader.scan_data)
            while cv2.waitKey(0) < 0:
                pass
        
        # show the image in the window
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break