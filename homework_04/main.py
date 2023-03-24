"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session as SessionType, joinedload

from homework_04.models import Base, Session, async_engine, User, Post


async def create_tables():
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: SessionType, users: list):
    for u in users:
        user = User(name=u['name'], username=u['username'], email=u['email'])
        session.add(user)
    await session.commit()


async def create_posts(session: SessionType, posts: list):
    for p in posts:
        post = Post(user_id=p['user_id'], title=p['title'], body=p['body'])
        session.add(post)
    await session.commit()


async def fetch_users_data():
    return [{"name": f"ivan{i}", "username": f"ivanov{i}", "email": f"ivan{i}@mail.ru"} for i in range(100)]


async def fetch_posts_data():
    return [{"user_id": i, "title": "about ivan", "body": "very very detail about ivan"} for i in range(100)]


async def async_main():
    async with Session() as session:
        users_data: List[dict]
        posts_data: List[dict]
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )
        await create_users(session, users_data)
        await create_posts(session, posts_data)


def main():
    asyncio.run(create_tables())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
