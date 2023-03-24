"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> blog_users
        Post -> blog_posts
        """
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)

Base = declarative_base(cls=Base, bind=async_engine)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class User(Base):
    name = Column(
        String,
        unique=False,
        nullable=False
    )
    username = Column(
        String,
        unique=True,
        nullable=False
    )
    email = Column(
        String,
        unique=True,
        nullable=False
    )

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email})"


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id", name="fk_user_id"),
        unique=True,
        nullable=False
    )
    title = Column(
        String,
        unique=False,
        nullable=False
    )
    body = Column(
        String,
        unique=False,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return f"Post(id={self.id}, user_id={self.user_id}, title={self.title})"


