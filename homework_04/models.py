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
from datetime import datetime
from typing import List

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    """
    Класс (модель таблицы в базе данных) Пользователь
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    username = Column(String(32), nullable=False)
    email = Column(String(32), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name = {self.name!r}, username = {self.username!r},' \
               f' email={self.email}, created_at={self.created_at!r})'

    def __repr__(self):
        return str(self)


class Post(Base):
    """
    Класс (модель таблицы в базе данных) Пост
    """
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title!r}, body = {self.body!r}'

    def __repr__(self):
        return str(self)


async def create_tables():
    """
    Функция пересоздания таблиц в базе данных на основании объявленных моделей
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users(data: List[dict]):
    """
    Функция записи пользователей в базу данных
    """
    async with Session() as session:
        async with session.begin():
            for user_details in data:
                user = User(id=user_details['id'], name=user_details['name'], username=user_details['username'], email=user_details['email'])
                session.add(user)


async def add_posts(data: List[dict]):
    """
    Функция записи постов в базу данных
    """
    async with Session() as session:
        async with session.begin():
            for post_details in data:
                post = Post(title=post_details['title'], body=post_details['body'], user_id=post_details['userId'])
                session.add(post)
