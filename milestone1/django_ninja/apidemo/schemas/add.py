from pydantic import BaseModel

class AddRequest(BaseModel):
    a: int=1
    b: int=2

class AddResponse(BaseModel):
    result: int