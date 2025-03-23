from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette import requests
from enum import Enum


app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/")
async def readRoot(status=status.HTTP_200_OK, response_class=FileResponse):
    return FileResponse("templates/index.html")

@app.get("/print/{parameter}") # Path parameters.
async def printParam(parameter: str):
    return {"to be printed":{parameter}}

# Predefined Paths

class BlogTypes(str, Enum):
    story = "story"
    howto = "howto"
    journal = "journal"

@app.get("/blog/{parameter}")
async def blogParameter(parameter: BlogTypes):
    return parameter