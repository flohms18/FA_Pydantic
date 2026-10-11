from fastapi import FastAPI, Request
from pydantic import BaseModel, ConfigDict
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class User:
    FirstName : str
    LastName : str
    Age : int
    Consultant : False

    model_config = {
            ConfigDict(
                str_max_length=10
            )


    }


@app.get('/', response_class=HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse(
        request=request, name='home.html'
    )



@app.put('User/{user_id}')
async def update_item(user_id : int, user : User):
    results = {
        {
            "user_id" : user_id,
            "user" : user
        }
    }



