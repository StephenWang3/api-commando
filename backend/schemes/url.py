from pydantic import BaseModel
from typing import Optional, Dict

class GetParams(BaseModel):
    url: str
    params: Optional[Dict]


class PostParams(BaseModel):
    url: str
    params: Optional[Dict]
    headers: Optional[Dict]
    data: Optional[Dict]


class PutParams(BaseModel):
    url: str
    params: Optional[Dict]
    headers: Optional[Dict]
    data: Optional[Dict]


class DeleteParams(BaseModel):
    url: str
    params: Optional[Dict]
    headers: Optional[Dict]
    data: Optional[Dict]