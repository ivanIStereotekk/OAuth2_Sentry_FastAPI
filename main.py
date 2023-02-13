import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from orm.models import User, Picturepack
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from orm.models import User,Picturepack





Pydantic_User = sqlalchemy_to_pydantic(User)
Pydantic_Picturepack = sqlalchemy_to_pydantic(Picturepack)


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get_token")  # This refers to the token endpoint


# Returns user from DB - AUTH WORKS

# async def authenticate_user(username: str, password: str):
#     user = await User.query.filter_by(username=username).first()
#     if not user or not user.check_password(password):
#         return False
#     return user

@app.post("/get_token")
async def user_create(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


@app.get("/")
async def user_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}



@app.post("/create_user",response_model=Pydantic_User)
async def create_user(user: Pydantic_User):
    new_user = Pydantic_User(name=user.name, password=user.password, email=user.email,phone_number=user.phone_number)
    await new_user.save()


    return await {"new_user":Pydantic_User(new_user)}






if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
