from fastapi import APIRouter, Header
from models.user import UserAuth
from config.jwt import validate_token, write_token
from fastapi.responses import JSONResponse

auth_routes = APIRouter()


@auth_routes.post("/login", tags=["login"])
def login(user: UserAuth):
    """
    Api para loguearse
    """
    if user.username == 'Nelson hernandez':
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_routes.post("/verify/token", tags=["login"])
def verify_token(Authorization: str = Header(None)):
    """
    Api para verifición de token de usuario
    """
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
