from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import User
from schemas.user import userEntity, usersEntity
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from middlewares.verify_token_routes import VerifyTokenRoute

user = APIRouter(route_class=VerifyTokenRoute)


@user.get("/users", response_model=List[User], tags=["users"])
async def find_all_user():
    """
    Api para consultar todos los usuarios
    """
    return usersEntity(conn.local.user.find())


@user.post("/users", response_model=User, tags=["users"])
async def create_user(user: User):
    """
    Api para la creación de los usuarios
    """
    new_user = user.dict()
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)


@user.get("/users/{id}", response_model=User, tags=["users"])
async def find_user(id: str):
    """
    Api para la consulta de un usuario
    """
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    """
    Api para la actualización de un usuario
    """
    conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": user.dict()})
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str):
    """
    Api para la eliminación de un usuario
    """
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
