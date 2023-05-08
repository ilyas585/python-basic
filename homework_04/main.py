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
import aiohttp

from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from models import (
    Session as async_session,
    engine,
    Base,
    User,
    Post,
)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_data():
    async with aiohttp.ClientSession() as client_session:
        fetched_data_user, fetched_data_post = await asyncio.gather(
            fetch_json(client_session, USERS_DATA_URL),
            fetch_json(client_session, POSTS_DATA_URL)
        )
        return fetched_data_user, fetched_data_post


async def load_users(session,fetched_users) -> list[User]:
    users = [
        User(
            username=fetched_user['username'],
            name=fetched_user['name'],
            email=fetched_user['email']
        )
        for fetched_user in fetched_users
    ]
    session.add_all(users)
    await session.commit()
    return users


async def load_posts(session, fetched_posts) -> list[Post]:
    posts = [
        Post(
            user_id=fetched_post['userId'],
            title=fetched_post['title'],
            body=fetched_post['body']
        )
        for fetched_post in fetched_posts
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def async_main():
    await create_tables()
    fetched_data_users, fetched_data_posts = await fetch_data()
    async with async_session() as session:
        await load_users(session, fetched_data_users)
        await load_posts(session, fetched_data_posts)


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
