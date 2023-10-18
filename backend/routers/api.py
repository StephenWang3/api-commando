from typing import Union
import urllib.request
from fastapi import APIRouter
from schemes.url import *

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
    request = urllib.request.Request(get_params.url, method="GET")
    reponse = urllib.request.urlopen(request).read()
    return {"content": reponse}
