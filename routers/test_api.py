from fastapi import APIRouter

router = APIRouter(prefix="/test")

@router.get("/get/")
def test_get(url):
    return {"url": url}

@router.post("/post/")
def test_post():
    return {'foo': 'bar'}

@router.put("/put/")
def test_put(url):
    return {'foo': 'bar'}