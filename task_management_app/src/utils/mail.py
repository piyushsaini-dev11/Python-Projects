from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from typing import List
  
conf = ConnectionConfig(
    MAIL_USERNAME ="rajeshsaini11944@email.com",
    MAIL_PASSWORD = "**********",
    MAIL_FROM = "rajeshsaini11944@email.com",
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
    
    

async def send_email(emails:List[str]):
    html = """
<p>hi,thanks for registration. our team connect you soon!</p> 
"""

    message = MessageSchema(
        subject="Registration confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    print ({"message":"email has been sent"})