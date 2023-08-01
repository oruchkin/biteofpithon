# start
# uvicorn app:app --reload

import fastapi
import fastapi.security as security
import sqlalchemy.orm as orm
import schemas
import services
from typing import List

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
        # form_data: schemas.UserRequest = fastapi.Depends(),
        db: orm.Session = fastapi.Depends(services.get_db)
):
    db_user = await services.login(email=form_data.username,
                                   password=form_data.password,
                                   db=db)

    if not db_user:
        raise fastapi.HTTPException(status_code=401, detail="Wrong login credentials")

    return await services.create_token(db_user)


@app.get("/api/users/current/current_user", response_model=schemas.UserResponse)
# TODO: почему fastapi.Depends(services.current_user) вызывается без скобок
async def current_user_api(user: schemas.UserResponse = fastapi.Depends(services.current_user)):
    return user


@app.post("/api/v1/posts", response_model=schemas.PostResponse)
async def create_post(
        post_request: schemas.PostRequest,
        user: schemas.UserResponse = fastapi.Depends(services.current_user),
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.create_post(user=user, db=db, post=post_request)


@app.get("/api/v1/posts/user", response_model=List[schemas.PostResponse])
async def get_posts_by_user_api(
        user: schemas.UserResponse = fastapi.Depends(services.current_user),
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.get_posts_by_user(user=user, db=db)


@app.get("/api/v1/posts/all", response_model=List[schemas.PostResponse])
async def get_posts_by_all_api(
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.get_posts_by_all(db=db)


@app.get("/api/v1/posts/{post_id}", response_model=schemas.PostResponse)
async def get_post_detail_api(
        post_id: int,
        db: orm.Session = fastapi.Depends(services.get_db),

):
    post = await services.get_post_detail(post_id, db=db)
    return post


@app.get("/api/v1/users/{user_id}", response_model=schemas.UserResponse)
async def get_user_detail_api(
        user_id: int,
        db: orm.Session = fastapi.Depends(services.get_db),
):
    user = await services.get_user_detail(user_id, db)
    return user


@app.delete("/api/v1/posts/{post_id}/")
async def delete_post_api(
        post_id: int,
        db: orm.Session = fastapi.Depends(services.get_db),
):
    post = await services.get_post_detail(post_id=post_id, db=db)
    await services.delete_post(post=post, db=db)
    return {"status": "Post deleted successfully"}


@app.put("/api/v1/posts/{post_id}/", response_model=schemas.PostResponse)
async def update_post_api(
        post_id: int,
        post_request: schemas.PostRequest,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    db_post = await services.get_post_detail(post_id, db)

    return await services.update_post(post_request, db_post, db)


