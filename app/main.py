from fastapi import FastAPI, Depends, HTTPException, status
from uuid import UUID

import model
from database import engine, create_session
from schema import TaskSchema, TaskSchemaExpanded
from sqlalchemy.orm import Session
from model import Task
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    model.Base.metadata.drop_all(bind=engine) #await
    model.Base.metadata.create_all(bind=engine)

@app.get("/tasks", response_model=List[TaskSchemaExpanded], status_code=200)
async def read_tasks(db: Session = Depends(create_session)):
   tasks = db.query(Task).all()
   return tasks

@app.post('/tasks/add',response_model = TaskSchemaExpanded, status_code=201)
async def create_task(task: TaskSchema, db: Session = Depends(create_session)):
   new_task = Task(**task.dict())
   db.add(new_task)
   db.commit()
   return new_task

@app.put("/tasks/{task_uuid}",response_model = TaskSchemaExpanded, status_code=200)
async def update_task(task_uuid: UUID, task: TaskSchema, db: Session = Depends(create_session)):
   updating_task = db.query(Task).get(task_uuid)
   if updating_task is not None:
      updating_task.task_description = task.task_description
      updating_task.task_params = task.task_params.dict()
      db.commit()
      db.refresh(updating_task)
   else:
      raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Task with UUID does not exist ")
   return updating_task