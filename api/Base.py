# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: 基本路由
"""
from fastapi import APIRouter


from api.login import index,login

Apirouter = APIRouter(prefix="/v1",tags=["api路由"])


@Apirouter.get('/input')
async def home(num: int):
    return {"num":num,"data":[]}

Apirouter.get("/index",tags=['api路由'],summary="注册入口")(index)
Apirouter.post("/login",tags=['api路由'],summary="登录入口")(login)