from src.tasks.dtos import Taskschema
from sqlalchemy.orm import Session
from src.tasks.models import Taskmodels
from fastapi import HTTPException
from src.user.models import Usermodel


def create_task(body:Taskschema, db:Session, user:Usermodel):
    data = body.model_dump()
    new_task = Taskmodels(title = data["title"],
                          description = data["description"],
                          is_completed = data["is_completed"],
                          user_id = user.id
                          )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task



def get_all_task(db:Session, user:Usermodel):
    tasks = db.query(Taskmodels).filter(Taskmodels.user_id == user.id).all()
    return tasks


def get_one_task(task_id:int,db:Session):
    one_task = db.query(Taskmodels).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incorrect")
    
    
    return  one_task


def update_task(body:Taskschema,task_id:int,db:Session,user:Usermodel):
    one_task = db.query(Taskmodels).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incorrect")
    if one_task.user_id != user.id:
        raise HTTPException(401, detail="you are not allowed to update the data")
        
    
    
    body = body.model_dump()
    for field,value in body.items():
        setattr(one_task,field,value)
       
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    
    
    return one_task


def delete_task(task_id:int,db:Session,user:Usermodel):
    one_task = db.query(Taskmodels).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incorrect")
    if one_task.user_id != user.id:
        raise HTTPException(401, detail="you are not allowed to update the data")
    
    
    db.delete(one_task)
    db.commit()
    
    return None

