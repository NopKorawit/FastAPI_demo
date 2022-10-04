from PIL import Image
import io
import cv2
import numpy as np
import base64

image = "E:\CPE\CDG\Programing\yolov5\DataSet\THAI_ID_CARD\Label-images\Temp ({}).jpg"

def ReadImg(a):
    print("readImg :"+a)
    img = cv2.imread(image.format(a), cv2.IMREAD_COLOR)
    return img

# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(imgdata))
    # opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    opencv_img= cv2.cvtColor(np.array(img), cv2.IMREAD_COLOR)
    return opencv_img 

def BytetoImg(byte):
    base64EncodedStr = base64.b64encode(byte)
    Image = cv2.imdecode(np.fromstring(base64.b64decode(
                base64EncodedStr, validate=True), np.uint8), cv2.IMREAD_COLOR)
    return Image