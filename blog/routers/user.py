from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from .controllers import user
from . import oauth2

router = APIRouter(
    tags=['Users'],
    prefix="/user",
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(db, request)


@router.get('/', response_model=List[schemas.ShowUser])
def get_user(db: Session = Depends(database.get_db)):
    return user.get(db)

@router.get("/{id}", response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.showById(db, id)
    