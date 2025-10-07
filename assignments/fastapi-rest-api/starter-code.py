from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

users = []

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users")
def list_users():
    return users

@app.get("/users/{email}")
def get_user(email: str):
    for user in users:
        if user.email == email:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
