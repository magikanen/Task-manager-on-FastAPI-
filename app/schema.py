from pydantic import BaseModel, Extra
from uuid import uuid4, UUID

class TaskParamsModel(BaseModel, extra=Extra.forbid):
    task_param_1: str
    task_param_2: int

class TaskSchema(BaseModel):
   task_description: str
   task_params: TaskParamsModel
   class Config:
       orm_mode = True

class TaskSchemaExpanded(TaskSchema):
   task_uuid: UUID = uuid4()
   class Config:
       orm_mode = True