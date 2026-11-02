from sqlalchemy import Column,Integer,String,Boolean,DateTime
from src.utils.db import base

class Usermodel(base):
    __tablename__ = "user_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String)
    