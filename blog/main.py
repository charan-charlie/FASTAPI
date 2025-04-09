from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog import schema, models
from blog   .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session 
from typing import List
from .hashing import Hash
from .routers import blog,user,authentication


app = FastAPI()

models.Base.metadata.create_all(engine)



app.include_router(blog.router)
app.include_router(user.userouter)
app.include_router(authentication.router)
# def get_db():
#     db = SessionLocal()
#     try: 
#         yield db
#     finally:

#         db.close()



# @app.post('/blog', status_code = status.HTTP_201_CREATED,tags= ['Blogs']) # status_code , we have list status coide in http codes 

# # 200 ok
# # 201 created
# # 202 Accepted


# def create(request: schema.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get("/blog", response_model = List[schema.ShowBlog],tags= ['Blogs'])
# def all(db: Session = Depends(get_db)): # for getting the all blogs
#     blogs = db.query(models.Blog).all()

#     return blogs

# @app.get("/blog/{id}",status_code = 200, response_model = schema.ShowBlog,tags= ['Blogs'])
# def show(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog :
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
#     return blog


# # respones code for creating the data is 201 

# # resonse status code 

# @app.delete("/blog/{id}",status_code = status.HTTP_204_NO_CONTENT,tags= ['Blogs'])

# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog wit hid {id}")
#     blog.delete()
#     db.commit() # after deleting the blog we have to commit 
#     return {"done"}

# @app.put("/blog/{id}",status_code = status.HTTP_202_ACCEPTED,tags= ['Blogs'])

# def update(id, request: schema.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog wit hid {id}")
#     blog.update(request.dict())
#     db.commit()
#     return 'updated'
    
# @app.post('/user',response_model=schema.ShowUser,tags = ["Users"])

# def create_user(request: schema.User, db: Session = Depends(get_db)): 
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password)) # here we have to manually give the arguments, instead of giving the request for the model to create
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/User/{id}',response_model = schema.ShowUser,tags = ["Users"])

# def get_user(id:int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"User wit hid {id}")
    
#     return user
