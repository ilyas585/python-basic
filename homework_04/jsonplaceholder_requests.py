
"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from typing import List

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[dict]:
    async with session.get(url) as response:
        data: List = await response.json()
        return data

