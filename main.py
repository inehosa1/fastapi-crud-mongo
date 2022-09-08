from fastapi import FastAPI
from config.docs import tags_metadata
from dotenv import load_dotenv
from routes.user import user
from routes.auth import auth_routes

app = FastAPI(
    title="REST API with FastApi and Mongodb",
    description="esto es una aplicacion basica con fast y mongodb",
    version="0.0.1",
    openapi_tags=tags_metadata
)
app.include_router(user, prefix="/api")
app.include_router(auth_routes, prefix="/api")

load_dotenv()