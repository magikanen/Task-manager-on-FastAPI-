from fastapi import FastAPI, Depends
from uuid import UUID

import model
from database import Base, engine
from schema import task_schema, task_schema_expanded
from sqlalchemy.orm import Session
from model import Task
from session import create_session
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    model.Base.metadata.drop_all(bind=engine) #await
    model.Base.metadata.create_all(bind=engine)

@app.get("/tasks", response_model=List[task_schema_expanded], status_code=200)
async def read_tasks(db: Session = Depends(create_session)):
   tasks = db.query(Task).all()
   return tasks

@app.post('/tasks/add',response_model = task_schema_expanded, status_code=201)
async def create_task(task: task_schema, db: Session = Depends(create_session)):
   new_task = Task(**task.dict())
   db.add(new_task)
   db.commit()
   return new_task

@app.put("/tasks/{task_uuid}",response_model = task_schema_expanded, status_code=200)
async def update_task(task_uuid: UUID, task: task_schema, db: Session = Depends(create_session)):
   updating_task = db.query(Task).get(task_uuid)
   updating_task.task_description = task.task_description
   updating_task.task_params = task.task_params.dict()
   db.commit()
   db.refresh(updating_task)
   return updating_task