from pydantic import BaseModel

class Userschema(BaseModel):
    
    name : str
    username : str
    password : str
    phone_number : str
    email : str
    
    
class Userresponseschema(BaseModel):
    
    name : str
    username : str
    phone_number : str
    email : str
    
        
class Userloginschema(BaseModel):
    
    username : str
    password : str
