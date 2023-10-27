from fastapi import APIRouter
from schemes.url import *

router = APIRouter(prefix="/test")

@router.get("/get/")
def test_get(**args):
    return {"args": args}

@router.post("/post/")
def test_post(post_params: PostParams):
    print(post_params)
    return {'post_params': post_params}