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

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Hello to my FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# POST REQUEST
@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if post:
        return {"post_detail": post}
    return {"message": "post not found"}