import cv2
import numpy as np
import base64

image = "E:\CPE\CDG\Programing\yolov5\DataSet\THAI_ID_CARD\Label-images\Temp ({}).jpg"

def ReadImg(a):
    print("readImg :"+a)
    img = cv2.imread(image.format(a), cv2.IMREAD_COLOR)
    return img
    
def BytetoImg(byte):
    base64EncodedStr = base64.b64encode(byte)
    Image = cv2.imdecode(np.fromstring(base64.b64decode(
                base64EncodedStr, validate=True), np.uint8), cv2.IMREAD_COLOR)
    return Image