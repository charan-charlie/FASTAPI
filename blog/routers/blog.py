from fastapi import APIRouter, Depends, status, HTTPException
from blog import schema, database, models, oauth
from typing import List
from sqlalchemy.orm import Session
from ..repositroy import blog

router = APIRouter(
    prefix = "/blog",
    tags = ["Blogs"]
)
get_db = database.get_db



@router.get("/", response_model = List[schema.ShowBlog])

def all(db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth.get_current_user)): # for getting the all blogs
    return blog.get_all(db)





@router.post('/', status_code = status.HTTP_201_CREATED) # status_code , we have list status coide in http codes 

def create(request: schema.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request,db)



@router.delete("/{id}",status_code = status.HTTP_204_NO_CONTENT)

def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destory(id,db)



@router.get("/{id}",status_code = 200, response_model = schema.ShowBlog)

def show(id: int, db: Session = Depends(get_db)):
    return blog.show(id,db)



@router.put("/{id}",status_code = status.HTTP_202_ACCEPTED,tags= ['Blogs'])

def update(id: int, request: schema.Blog, db: Session = Depends(get_db)):
    return blog.update(id,request,db)
    
