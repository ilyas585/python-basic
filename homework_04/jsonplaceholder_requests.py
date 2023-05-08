"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

BASE_URL = "https://jsonplaceholder.typicode.com/"
USERS_DATA_URL = BASE_URL + "users/"
POSTS_DATA_URL = BASE_URL + "posts/"


async def fetch_json(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
