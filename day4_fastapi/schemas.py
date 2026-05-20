from pydantic import BaseModel, ConfigDict

class STaskAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int