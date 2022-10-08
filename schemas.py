from pydantic import BaseModel

class EventRequest(BaseModel):
    name: str
    completed: bool

class EventResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        orm_mode = True
            