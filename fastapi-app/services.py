import database
import models
import sqlalchemy.orm as orm
import schemas
import email_validator
import fastapi
import passlib.hash as hash
import jwt
import fastapi.security as security

SECRET_KEY = "secret_key"
# TODO: выяснить че это за херня
oauth2schema = security.OAuth2PasswordBearer("/api/v1/login")


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


async def current_user(db: orm.Session = fastapi.Depends(get_db),
                       token: str = fastapi.Depends(oauth2schema)):
    try:
        # print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        # get user by Id
        db_user = db.query(models.UserModel).get(payload["id"])
    except:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    # if all okay return DTO/Schema version User
    return schemas.UserResponse.from_orm(db_user)


async def create_post(user: schemas.UserResponse,
                      db: orm.Session,
                      post: schemas.PostRequest):
    post = models.PostModel(**post.dict(), user_id=user.id)
    db.add(post)
    db.commit()
    db.refresh(post)

    # convert Post model to Post DTO/schema and return to API layer
    return schemas.PostResponse.from_orm(post)


async def get_posts_by_user(user: schemas.UserResponse, db: orm.Session):
    posts = db.query(models.PostModel).filter_by(user_id=user.id)

    # convert each post model to post schema and make a list to be returned
    data = list(map(schemas.PostResponse.from_orm, posts))
    return data


async def get_post_detail(post_id: int, db: orm.Session):
    db_post = db.query(models.PostModel).filter_by(id=post_id).first()
    if not db_post:
        raise fastapi.HTTPException(status_code=404, detail="Post not found")
    # return schemas.PostResponse.from_orm(db_post)
    return db_post


async def get_user_detail(user_id: int, db: orm.Session) -> schemas.UserResponse:
    db_user = db.query(models.UserModel).filter_by(id=user_id).first()
    if not db_user:
        raise fastapi.HTTPException(status_code=404, detail="User not found")
    return schemas.UserResponse.from_orm(db_user)
    # return db_user


async def delete_post(post: models.PostModel, db: orm.Session):
    db.delete(post)
    db.commit()


async def update_post(post_request: schemas.PostRequest,
                      post: models.PostModel,
                      db: orm.Session):
    post.post_title = post_request.post_title
    post.post_description = post_request.post_description
    post.image = post_request.image
    db.commit()
    db.refresh(post)

    return schemas.PostResponse.from_orm(post)


async def get_posts_by_all(db: orm.Session):
    posts = db.query(models.PostModel)

    # convert each post model to post schema and make a list to be returned
    data = list(map(schemas.PostResponse.from_orm, posts))
    return data
