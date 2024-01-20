from pyzbar import pyzbar
import cv2

class Breader():
    
    def __init__(self, scan_data):
        self.scan_data = scan_data
        
    def draw_barcode(self, decoded, image):
        image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                                (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                                color=(0, 255, 0),
                                thickness=5)
        return image

    def decode(self, image):
        # decodes all barcodes from an image
        decoded_objects = pyzbar.decode(image)
        for obj in decoded_objects:
            # draw the barcode
            # image = self.draw_barcode(obj, image)
                        
            self.scan_data = obj.data.decode('utf-8')

        return image

        