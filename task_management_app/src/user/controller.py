from src.user.dtos import Userschema,Userloginschema
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException,status,Request,BackgroundTasks
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime, timedelta
from src.utils.mail import send_email

password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



async def register(body:Userschema, db:Session,bg_tasks:BackgroundTasks):
    is_user = db.query(Usermodel).filter(Usermodel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="username is already taken")
    
    
    is_user = db.query(Usermodel).filter(Usermodel.phone_number == body.phone_number).first()
    if is_user:
        raise HTTPException(400, detail="phone_number is already existed")
    
    
    is_user = db.query(Usermodel).filter(Usermodel.email == body.email).first()
    if is_user:
        raise HTTPException(400, detail="email is already existed")
    
    
    hash_password = get_password_hash(body.password)
    
    new_user = Usermodel( name = body.name,
                          username = body.username,
                          hash_password = hash_password,
                          phone_number = body.phone_number,
                          email = body.email
                        )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    ##send email confirmation
    
    bg_tasks.add_task(send_email, [new_user.email])
    
    return new_user


def login_user(body:Userloginschema, db:Session):
    user = db.query(Usermodel).filter(Usermodel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=" you entered wrong username ")
    
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you entered wrong password")
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    
    token = jwt.encode({"_id":user.id,"exp":exp_time.timestamp()}, settings.SECRET_KEY, settings.ALGORITHM)
    
    return{"token":token}

##token send
def is_authenticated(request:Request,db:Session):
    try:
        token = (request.headers.get("authorization"))
        if not token:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are authorized")
        
        token = token.split(" ")[-1]
    
        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")
        exp_time = int(data.get("exp"))
    
        current_time = datetime.now().timestamp()
        print(exp_time - current_time)
    
        if current_time > exp_time:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are authorized")
    
        user = db.query(Usermodel).filter(Usermodel.id == user_id).first()
        if not user:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are unauthorized")
    
        return user
    
    except InvalidTokenError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are unauthorized")
        
    
   