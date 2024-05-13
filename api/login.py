from typing import  List
from pydantic import BaseModel


class login(BaseModel):
    username:str
    password:str
    user:list[int]

def index(age:int):
    return{"fun":"/index","age":age}


def login(data:login):
    return data