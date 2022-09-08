from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def expirte_date(days: int):
    new_date = datetime.now() + timedelta(days)
    return new_date
    
def write_token(data: dict):
    token = encode(payload={
        **data, "exp": expirte_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, token=getenv("SECRET"), algorithms=["HS256"])
        decode(token, token=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expirted"}, status_code=401)
        
        