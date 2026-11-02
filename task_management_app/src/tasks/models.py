from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from src.utils.db import base


class Taskmodels(base):
    __tablename__ = "user_task"
    
    id = Column(Integer, primary_key="True")
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default="False")
    
    user_id = Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"))