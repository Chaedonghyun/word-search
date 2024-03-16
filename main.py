from fastapi import FastAPI,UploadFile,Form,Response, Depends # form이나 uploadfile, Response 사용하기 위해 import
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
import sqlite3 #sqllite를 사용하기 위해 import

app=FastAPI()

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

