"""
Домашнее задание №3
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

from homework_04.models import create_tables, add_users, add_posts
from jsonplaceholder_requests import fetch_json, POSTS_DATA_URL, USERS_DATA_URL


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL))
    await add_users(users_data)
    await add_posts(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
