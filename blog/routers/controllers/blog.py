from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ... import models, schemas

def get_all(db: Session):
    all_blog = db.query(models.Blog).all()
    return all_blog

def create(db: Session, request: schemas.Blog):
    print("Incoming blog data:", request)
    new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found to delete")
    return f'blog with {id} deleted'

def update(db: Session, request:schemas.Blog):
    print("Incoming blog data:", request)
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found to update")
    blog_query.update(request.dict())
    db.commit()
    return 'blog updated'

def getById(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "No blog found"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"blog with id of {id} not found")
    return blog