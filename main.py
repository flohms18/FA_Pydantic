from fastapi import FastAPI, Request, Form
from pydantic import BaseModel, ConfigDict, Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class User (BaseModel):
    FirstName : Annotated[str, Field(min_length=2)]
    LastName : str
    Age : Annotated[int, Field(ge=18, le=99)]
    Consultant : bool = False

    model_config = ConfigDict()
    


@app.get('/', response_class=HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse(
        request=request, name='home.html'
    )

@app.post('/create_user')
async def create_item(user: Annotated[User, Form()]):
    return user

@app.put('/User/{user_id}')
async def update_item(user_id : int, user : User):
    results = {
        {
            "user_id" : user_id,
            "user" : user
        }
    }



