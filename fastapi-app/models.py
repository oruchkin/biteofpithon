import datetime
import sqlalchemy
import sqlalchemy.orm as orm
import passlib.hash as hash

import database


class UserModel(database.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DATETIME, default=datetime.datetime.now())
    posts = orm.relationship("PostModel", back_populates="user")

    class Config:
        orm_mode = True
        model_config = {
            "from_attributes": True
        }

    def password_verification(self, password: str) -> bool:
        return hash.bcrypt.verify(password, self.password_hash)



class PostModel(database.Base):
    __tablename__ = "posts"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    post_title = sqlalchemy.Column(sqlalchemy.String)
    post_description = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DATETIME, default=datetime.datetime.now())
    user = orm.relationship("UserModel", back_populates="posts")

    # # это для того чтобы использовать from_orm
    # class Config:
    #     orm_mode = True
    #     model_config = {
    #         "from_attributes": True
    #     }
