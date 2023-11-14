from pydantic import BaseModel


class GetParams(BaseModel):
    url: str
    params: dict | None


class PostParams(BaseModel):
    url: str
    params: dict | None
    headers: dict | None
    data: dict | None   

class PutParams(BaseModel):
    url: str
    params: dict | None
    headers: dict | None
    data: dict | None


class DeleteParams(BaseModel):
    url: str

    params: dict | None
    headers: dict | None
    data: dict | None