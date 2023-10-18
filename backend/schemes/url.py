from pydantic import BaseModel


class GetParams(BaseModel):
    url: str