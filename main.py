from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Pydantic model for request body validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: float = None

# Define my_post outside the Post class
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite food", "content": "I love Burger", "id": 2}
]

@app.get("/")
async def root():
    return {"message": "Hello to my FastAPI"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

# POST REQUEST
@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": "post_dict"}