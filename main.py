from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request body validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: float = None

# Define my_post outside the Post class
my_post = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite food", "content": "I love Burger", "id": 2}
]

@app.get("/")
async def root():
    return {"message": "Hello to my FastAPI"}

@app.get("/post")
def get_post():
    return {"data": my_post}

# POST REQUEST
@app.post("/createpost")
def createpost(post: Post):
    print(post.dict())
    return {"data": "new_post"}