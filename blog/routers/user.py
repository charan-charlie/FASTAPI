from fastapi import APIRouter,Depends,HTTPException, status
from blog import schema,models
from blog import database
from sqlalchemy.orm import Session
from ..repositroy import user

get_db = database.get_db

userouter = APIRouter(
    prefix="/user",
    tags = ["User"]
)

@userouter.post('/',response_model=schema.ShowUser)

def create_user(request: schema.User, db: Session = Depends(get_db)): 
    return user.create(request,db)


@userouter.get('/{id}',response_model = schema.ShowUser)

def get_user(id:int, db: Session = Depends(get_db)):
    return user.get(id,db)
