from fastapi import Request,HTTPException,status,Depends
from sqlalchemy.orm import Session
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from src.user.models import Usermodel
from src.utils.db import get_db
from datetime import datetime, timedelta
from src.utils.db import get_db


def is_authenticated(request:Request,db:Session = Depends(get_db)):
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
        
    
   