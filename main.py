
'''
In order to run a fast api app, go to the current folder using

cd foldername, here it is cd FastApi

then run python -m uvicorn main:app --reload

where main = file name

app = app name

due to some reason we can not run uvicorn first so we have to do it together
'''
from fastapi import FastAPI, Request

#  how we can get the response on website
from fastapi.responses import HTMLResponse

# how we can serve the static files
from fastapi.staticfiles import StaticFiles

# how we can use the template
from fastapi.templating import Jinja2Templates

# it is 
from pymongo import MongoClient

app = FastAPI()

# if you go here after running an application, http://127.0.0.1:8000/static/style.css it is working, cause i have created a css file in the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# create a index.html file to let it work on your host.
templates = Jinja2Templates(directory="templates")

# ctrl click on Mongoclient to check its detail, which is important to do
# else go to mongo db pymongo client, this will tell you how to work with it
conn = MongoClient


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


