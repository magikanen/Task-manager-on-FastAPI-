from pydantic import BaseModel, Field
from uuid import uuid4, UUID

class task_params_model(BaseModel):
    task_param_1 : str
    task_param_2 : int
    class Config:
       orm_mode = True

class task_schema(BaseModel):
   task_description : str
   task_params : task_params_model
   class Config:
       orm_mode = True #.from_orm
       #The subclass config with orm_mode set to True will instruct the Pydantic model to read the data as a dictionary and attribute.

class task_schema_expanded(task_schema):
   task_uuid: UUID = uuid4()
   class Config:
       orm_mode = True