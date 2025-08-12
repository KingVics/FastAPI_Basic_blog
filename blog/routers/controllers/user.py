from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ... import models, schemas, hash

def create(db: Session, request: schemas.User):
    password = hash.Hash.get_password_hash(request.password)
    user = models.User(name = request.name, email = request.email, password = password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users not found")
    return users

def showById(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found")
    return user