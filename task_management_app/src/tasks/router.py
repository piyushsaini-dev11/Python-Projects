from fastapi import APIRouter,Depends,status
from src.tasks import controller
from src.tasks.dtos import Taskschema,Taskresponseschema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import Usermodel


task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create", response_model=Taskresponseschema, status_code=status.HTTP_201_CREATED)
def create_task(body:Taskschema,db:Session = Depends(get_db),user:Usermodel = Depends(is_authenticated)):
    return controller.create_task(body,db,user)


@task_routes.get("/all_task", response_model=List[Taskresponseschema], status_code = status.HTTP_200_OK)
def get_all_task(db:Session = Depends(get_db),user:Usermodel = Depends(is_authenticated)):
    return controller.get_all_task(db, user)


@task_routes.get("/get_task/{task_id}",response_model=Taskresponseschema,status_code =status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session = Depends(get_db),user:Usermodel = Depends(is_authenticated)):
    return controller.get_one_task(task_id,db)


@task_routes.put("/update_task/{task_id}",response_model=Taskresponseschema,status_code =status.HTTP_201_CREATED)
def update_task(body:Taskschema,task_id:int,db:Session = Depends(get_db),user:Usermodel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)


@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code =status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session = Depends(get_db),user:Usermodel = Depends(is_authenticated)):
     return controller.delete_task(task_id,db,user)
