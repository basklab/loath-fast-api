from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request

login_router = APIRouter(prefix="/login", tags=["users"])

templates = Jinja2Templates(directory="login")


@login_router.get("/me")
async def read_users(request: Request):
    return templates.TemplateResponse("me.j2", {"request": request})


@login_router.get("/other")
async def read_user_me(request: Request):
    return templates.TemplateResponse("basic-form.j2", {"request": request})
