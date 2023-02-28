import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from orm.models import User, Picturepack
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from orm.models import User,Picturepack
import sentry_sdk


sentry_sdk.init(
    dsn="https://a88e354a8b174c99b924ddb76202335f@o4504662790307840.ingest.sentry.io/4504671874711552",
    traces_sample_rate=1.0
)



Pydantic_User = sqlalchemy_to_pydantic(User)
Pydantic_Picturepack = sqlalchemy_to_pydantic(Picturepack)


app = FastAPI(title="API OAuth2 and Senrty_SDK logging", description="Something like test pack for two technologies that are mentioned in the title.")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get_token")  # This refers to the token endpoint


# Returns user from DB - AUTH WORKS

# async def authenticate_user(username: str, password: str):
#     user = await User.query.filter_by(username=username).first()
#     if not user or not user.check_password(password):
#         return False
#     return user

@app.post("/get_token",tags=["Get Token - POST"])
async def user_create(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


@app.get("/",tags=["User Token"])
async def user_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}



@app.post("/create_user",response_model=Pydantic_User,tags=["User Creation Method - POST"])
async def create_user(user: Pydantic_User):
    new_user = Pydantic_User(name=user.name, password=user.password, email=user.email,phone_number=user.phone_number)
    await new_user.save()


    return await {"new_user":Pydantic_User(new_user)}






if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
