from pydantic import BaseModel


class GetParams(BaseModel):
    url: str
    
class PutParams(BaseModel):
    url: str
    rbody: dict
    hearders:dict