from os import name
from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            'data': f'blog list with limit {limit} and published {published} '
        }
    else:
        return {
            'data': f'blog list with limit {limit} and published false '
        }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'unpublished blogs'
    }

@app.get('/blog/{id}')
def show(id : int):
    return {
        'data': id
    }

@app.get('/blog/{id}/comments')
def comments(id, limit = 10):
    return {
        'data': f'comments of id {id} with limit {limit}'
    }


from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {
        'data': f'blog created with title {blog.title}'
    }

# if __name__ == '__main__':
#     uvicorn.run(app, host = "127.0.0.1", port = 9000)