import database
import models
import sqlalchemy.orm as orm
import schemas
import email_validator
import fastapi
import passlib.hash as hash
import jwt

SECRET_KEY = "secret_key"


def create_db():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: orm.Session) -> models.UserModel:
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()


async def create_user(user: schemas.UserRequest, db: orm.Session):
    # check for valid email
    try:
        is_valid = email_validator.validate_email(email=user.email)
        email = is_valid.email
    except email_validator.EmailNotValidError:
        raise fastapi.HTTPException(status_code=400, detail="provide valid Email")

    hashed_password = hash.bcrypt.hash(user.password)
    user_obj = models.UserModel(
        email=email,
        name=user.name,
        phone=user.phone,
        password_hash=hashed_password,
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def create_token(user: models.UserModel):
    # convert user model to user schema
    # user_schema = schemas.UserBase.from_orm(user)
    user_schema = schemas.UserResponse.from_orm(user)

    # convert obj to dictionary
    user_dict = user_schema.dict()
    del user_dict["created_at"]

    token = jwt.encode(user_dict, SECRET_KEY)
    return dict(access_token=token, token_type="bearer")


async def login(email: str, password: str, db: orm.Session):
    db_user = await get_user_by_email(email=email, db=db)

    if not db_user:
        return False

    if not db_user.password_verification(password):
        return False

    return db_user
