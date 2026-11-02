from pydantic import BaseModel

class Taskschema(BaseModel):
    
    title : str
    description : str
    is_completed : bool = False
    
    
class Taskresponseschema(BaseModel):
    
    id : int
    title : str
    user_id : int | None = 0  
    

    
   