from api.Base import Apirouter
from views.Base import ViewsRouter
from fastapi import  APIRouter

ALLRouter=APIRouter()

ALLRouter.include_router(Apirouter)
ALLRouter.include_router(ViewsRouter)