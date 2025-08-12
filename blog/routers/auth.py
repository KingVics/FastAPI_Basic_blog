from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, hash
from . import token
from typing import Annotated
router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)

@router.post("/login")
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(database.get_db)):
    print(request)
    user = db.query(models.User).filter(models.User.email == request.username).first()
    password = hash.Hash.verify_password(request.password, user.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid email or password")
    if not hash.Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid email or password")
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
