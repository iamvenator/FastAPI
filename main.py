from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette import requests


app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/")
async def readRoot(status=status.HTTP_200_OK, response_class=FileResponse):
    return FileResponse("templates/index.html")
