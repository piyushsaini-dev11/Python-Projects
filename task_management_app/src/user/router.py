from fastapi import APIRouter,Depends,status,Request,BackgroundTasks
from src.user.dtos import Userschema,Userresponseschema,Userloginschema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user import controller

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register",response_model=Userresponseschema, status_code=status.HTTP_201_CREATED)
async def register(body:Userschema,bg_tasks:BackgroundTasks,db:Session=Depends(get_db)):
    return await controller.register(body,db,bg_tasks)

@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login_user(body:Userloginschema, db:Session=Depends(get_db)):
    return controller.login_user(body, db)

@user_routes.get("/is_auth",response_model=Userresponseschema, status_code=status.HTTP_200_OK)
def is_authenticated(request:Request,db:Session=Depends(get_db)):
    return controller.is_authenticated(request,db)