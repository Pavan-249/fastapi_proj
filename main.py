from fastapi import FastAPI,status,HTTPException

import models
from typing import Optional,List



app=FastAPI()

@app.get('/')
def index():
    return {"message":"Hello world"}


@app.get('/greet/{name}')

def greet_name(name:str):
    return {"greeting":f"Hello {name}"}


from pydantic import BaseModel

class baby(BaseModel):
    id:int
    gender:str
    babyName:str
    category:str
    meaning:str

    class Config:
        orm_mode=True

from database import SessionLocal

db=SessionLocal()


@app.get('/baby',response_model=List[baby],status_code=200)
def get_all_babies():
    babies=db.query(models.baby).all()
    return babies


@app.get('/baby/{baby_id}')
def get_a_baby(baby_id:int):
    baby=db.query(models.baby).filter(models.baby.id==baby_id).first()

    return baby

@app.post('/baby',response_model=baby, status_code=status.HTTP_201_CREATED)
def create_a_baaby(baby:baby):
    new_baby=models.baby(id=baby.id,gender=baby.gender,category=baby.category,babyName=baby.babyName,meaning=baby.meaning)


    db_baby=db.query(models.baby).filter(baby.babyName==new_baby.babyName).first()

    if db_baby is not None:
        raise HTTPException(status_code=400,detail="Item Already Exists")
    db.add(new_baby)
    db.commit()

    return new_baby



@app.put('/baby/{baby_id}',response_model=baby,status_code=status.HTTP_200_OK)
def update_a_baby(baby_id:int,baby:baby):
    baby_to_update=db.query(models.baby).filter(models.baby.id==baby_id).first()
    baby_to_update.babyName=baby.babyName
    baby_to_update.gender=baby.gender
    baby_to_update.category=baby.category
    baby_to_update.meaning=baby.meaning

    db.commit()
    return baby_to_update
    
@app.delete('/baby/{baby_id}')
def delete_a_baby(baby_id:int):
    item_to_delete=db.query(models.baby).filter(models.baby.id==baby_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource not found")
    
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete


# @app.put("/item/{item_id}")
# def update_item(item_id:str,item:baby):
#     return {"name":item.babyName,"gender":item.gender}




# @app.get("/great/")
# def greet_me(name:Optional[str]=None):
#     return {"Hey":f"{name}"}
