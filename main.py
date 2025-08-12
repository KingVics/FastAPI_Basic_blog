from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogd from db"}
    return {"data": f"{limit} blogs from db"}

@app.post('/blog')
def create_blog(blog: Blog):
    return {"data": f"blog is created with {blog.title}"}


@app.get('/blog/{id}')
def about(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comment(id):
    return {"data": {'1', '2'}}

@app.get('/blog/unplished')
def unpublished():
    return {"data": "all unpublished"}


if __name__ == "__main__":
    uvicorn.run(app, host= "127.0.0.1", port=5000)