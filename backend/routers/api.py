from typing import Union
from fastapi import APIRouter
from schemes.url import *
from models import get_method, post_method

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(item_id)
    return {"item_id": item_id, "q": q}

@router.post("/get/")
def request_get(get_params: GetParams):
    return get_method.mock_get(get_params)

@router.post("/post/")
def request_post(post_params: PostParams):
    return post_method.mock_post(post_params)