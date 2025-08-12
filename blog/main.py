from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, auth

app = FastAPI()
# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = sessionLocal()
    
#     try:
#         yield db
#     finally:
#         db.close()
        

# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blog'])
# def get_blogs(limit=10, published: bool = True, db: Session = Depends(get_db) ):
#     all_blog = db.query(models.Blog).all()
#     return all_blog





