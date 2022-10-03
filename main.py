from typing import Optional
from fastapi import FastAPI, File, UploadFile
import io
from starlette.responses import StreamingResponse
import cv2
from service import ReadImg ,BytetoImg

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
    print(type(file))
    return {"file_size": len(file)}

@app.post("/Image/")
async def create_file(file: bytes = File()):
    cv2img = BytetoImg(file)
    res, im_png = cv2.imencode(".png", cv2img)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(type(file))
    return {"filename": file.filename}

@app.post("/vector_image")
def MyImg(*, vector):
    # Returns a cv2 image array from the document vector
    cv2img = ReadImg(vector)
    res, im_png = cv2.imencode(".png", cv2img)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

