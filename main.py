from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette import requests
from enum import Enum
from typing import Optional

#RedirectResponse

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


# Query parameters
# 'GET http://127.0.0.1:8000/blog/all?page=2&page_size=5'

@app.get("/blog/all")
async def get_all_blogs(page:int, page_size:int):
    return {"message":f"All {page_size} blogs on page {page}"}

# Default query parameters
@app.get("/blog/onPage6/")
async def getPage6(page: int = 6, page_size: int = 100):
    return {"message":f"Returning all the blogs with page size of {page_size} on page {page}"}

# Optional query parameter
@app.get("/blog/optional")
async def getOptionalonPage7(page: int = 7, page_size: Optional[int] = None):
        return {"message": f"Returning blogs on page {page} with default {page_size} page size"}

# Both query and path parameters
@app.get("/blog/{id}/comments/{comment_id}")
async def getCombyId(id: int, comment_id: int, valid:bool = True, username: Optional[str] = None):
    return {"message":f"blog_id: {id}, comment_id: {comment_id}, valid: {valid}", username: {username}}

# The less specific ones should always be above from the generic one.
@app.get("/blog/{parameter}")
async def blogParameter(parameter: BlogTypes):
    return parameter