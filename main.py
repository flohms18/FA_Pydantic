from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI

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

