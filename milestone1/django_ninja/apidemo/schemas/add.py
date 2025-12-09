from pydantic import BaseModel

class AddRequest(BaseModel):
    a: int
    b: int

class AddResponse(BaseModel):
    result: int