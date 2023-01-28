import json
import aiohttp
from dataclasses import dataclass
from config import USERS_DATA_URL, POSTS_DATA_URL
import asyncio


@dataclass
class ApiUser:
    id: int
    name: str
    username: str
    email: str


@dataclass
class ApiPost:
    title: str
    body: str
    user_id: int


async def get_request_json(url: str) -> "json":
    async with aiohttp.ClientSession() as session:
        responce = await session.get(f"{url}")
        data = await responce.json()
    return data


async def get_users():
    data = await get_request_json(USERS_DATA_URL)

    result = []

    for item in data:
        result.append(
            ApiUser(
                id=item.get("id"),
                name=item.get("name"),
                username=item.get("username"),
                email=item.get("email"),
            )
        )

    return result


async def get_posts():
    data = await get_request_json(POSTS_DATA_URL)

    result = []

    for item in data:
        result.append(
            ApiPost(
                title=item.get("title"),
                body=item.get("body"),
                user_id=item.get("userId"),
            )
        )
    return result


async def async_run():
    users_list, post_list = await asyncio.gather(get_users(), get_posts())
    return users_list, post_list


users_list, post_list = asyncio.run(async_run())
