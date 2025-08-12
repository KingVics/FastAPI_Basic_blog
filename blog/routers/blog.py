from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, database
from .controllers import blog
from . import oauth2


router = APIRouter(
    tags=['Blogs'],
    prefix="/blog",
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.get('/', response_model=List[schemas.ShowBlog],)
def get_blogs(limit=10, published: bool = True, db: Session = Depends(database.get_db) ):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(db, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.delete(db, id)


@router.put('/{id}', status_code=status.HTTP_200_OK,)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
   return blog.update(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def getBlogById(id: int, response: Response, db: Session = Depends(database.get_db)):
    return blog.getById(db, id)