from typing import Optional

from fastapi import FastAPI

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
