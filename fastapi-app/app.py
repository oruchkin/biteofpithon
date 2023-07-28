import fastapi
import fastapi.security as security
import sqlalchemy.orm as orm
import schemas
import services

app = fastapi.FastAPI()


@app.post("/api/v1/users")
async def register_user(
        user: schemas.UserRequest,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    # call to check if user with email exists
    db_user = await services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail='user with this email already exists')

    # create the user and return a token
    db_user = await services.create_user(user=user, db=db)
    return await services.create_token(db_user)


@app.post("/api/v1/login")
async def login(
        form_data: security.OAuth2PasswordRequestForm = fastapi.Depends(),
        db: orm.Session = fastapi.Depends(services.get_db)
):
    db_user = await services.login(email=form_data.username,
                                   password=form_data.password,
                                   db=db)

    if not db_user:
        raise fastapi.HTTPException(status_code=401, detail="Wrong login credentials")

    return await services.create_token(db_user)






