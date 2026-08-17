# Fast API

'''
A basic program to rum as an example:

'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


'''
In order to run the command in terminal:

fastapi dev

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
'''

# Python types:
def add(firstname, lastname):
    return firstname + lastname

fname = 'bill'
lname = 'gates'

name =  add(fname.capitalize(), lname)
print(name)

#  or 
'''
we can say, if we use the support of types in the function just like below we can let the function know that the value it is getting is of a certain type.

and it can also recommend the method of that type in the function itself, generally it can not do it unless you provide a type here.

we can also use multiple types together and it will show all the methods of each type 

we can set a default value just like below, in case of no value finded  

we can also do : def add2(firstname: str | list[int, int, str, float]...
'''
def add2(firstname: str | list[int] | None, lastname: str = None):
    return firstname.capitalize() + lastname

fname1 = 'bill' #or lets say instead of bill it is [true], it will throw an error cause int type is listed in the list in the fucntion
lname1 = 'gates'

name =  add(fname1, lname1)
print(name)