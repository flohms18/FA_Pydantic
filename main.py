from fastapi import FastAPI, Request
from pydantic import BaseModel
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
        "json_schema_extra" : {
            "examples" : [
                "name"
            ]
        }
    }


@app.get('/', response_class=HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse(
        request=request, name='home.html'
    )



