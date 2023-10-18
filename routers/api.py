from typing import Union
import urllib.request
import requests
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

@router.put("/put_items/")
def request_put(get_params: GetParams):
    r=requests.put(PutParams.url,PutParams.rbody,PutParams.headers)
    rj=r.json()
    rc=r.status_code
    print(rc)
    return rj,rc

@router.put("/delete_items/")
def request_put(get_params: GetParams):
    r=requests.delete(PutParams.url,PutParams.rbody,PutParams.headers)
    rj=r.json()
    rc=r.status_code
    print(rc)
    return rj,rc