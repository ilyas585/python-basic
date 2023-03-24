"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def get_users():
    return await fetch_json(USERS_DATA_URL)


async def get_posts():
    return await fetch_json(POSTS_DATA_URL)


async def main():
    await get_users()
    await get_posts()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
