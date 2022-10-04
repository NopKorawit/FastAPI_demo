import base64
from typing import Optional
from fastapi import FastAPI, File, UploadFile,Body,Form
import io
from starlette.responses import StreamingResponse
import cv2
from service import ReadImg ,BytetoImg,stringToRGB
from matplotlib import pyplot as plt

#run app
#uvicorn main:app --reload --port 8080

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", 
            "author": "Korawit"}

@app.get("/hi")
def hi(name:str, Age:Optional[str] = 0):
    message = "{} is {} years old."
    return {"Hello": name, "message": message.format(name,Age)}

@app.get("/items/{item_id}")
def read_item(item_id: int, price: Optional[int] = None):
    return {"item_id": item_id, 
            "price": price}

@app.post("/files/")
async def create_file(file: bytes = File()):
    file_type = str(type(file))
    cv2img = BytetoImg(file)
    res, base64 = cv2.imencode(".png", cv2img)
    return {"file_size": len(file),
            "type":file_type,
            "base64":str(base64)}

# Upload file to byte convert to base64 and show picture form base64 
@app.post("/Image/")
async def create_file(file: bytes = File()):
    cv2img = BytetoImg(file)
    res, im_png = cv2.imencode(".png", cv2img)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(type(file))
    return {"filename": file.filename}

@app.post("/My_Img")
def MyImg(*, vector):
    # Returns a image from my computer
    cv2img = ReadImg(vector)
    res, im_png = cv2.imencode(".png", cv2img)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

@app.post("/uploadImg")
def uploadImg(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}

@app.post("/uploadBase64save")
def uploadBase64save(filename: str = Form(...), filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = base64.b64decode(image_as_bytes)  # decode base64string
    try:
        with open("uploaded_" + filename, "wb") as f:
            f.write(img_recovered)
    except Exception:
        return {"message": "There was an error uploading the file"}
        
    return {"message": f"Successfuly uploaded {filename}"} 

@app.post("/uploadBase64")
def uploadBase64(filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = stringToRGB(image_as_bytes)  # decode base64string
    print(img_recovered)
    plt.imshow(img_recovered, 'gray'),plt.show()
    return {"message": "Successfuly uploaded",
            "type": str(type(img_recovered))} 