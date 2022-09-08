def userEntity(user) -> dict:
    """    
    Entidad con la información de un usuario
    """
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


def usersEntity(users) -> list:
    """    
    Entidad con la información de varios usuarios
    """
    return [userEntity(item) for item in users]
