from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

@router.get("/hello-world")
def hello_world ():
    res = {
        "message": "Hello World"
    }
    return JSONResponse(content=jsonable_encoder(res))