from fastapi import FastAPI
from typing import Union
from fastapi.params import Body

app = FastAPI()
 

@app.get("/")
async def root():
    return {"message": "Hello to my FastAPI"}

   ## review this later on
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/post")
def get_post():
    return {"data": "This is your post"}


# POST REQUEST
@app.post("/createpost")
def createpost(payload: dict =Body(...)):
    print(payload)
    return {"new_post":  f"title {payload['title']} content {payload['content']}"}