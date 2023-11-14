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

@router.put("/put/")
def test_put(put_params: PutParams):
    print(put_params)
    return {'put_params': put_params}

@router.delete("/delete/")
def test_delete(delete_params: DeleteParams):
    print(delete_params)
    return {'delete_params': delete_params}