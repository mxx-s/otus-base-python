import asyncio
import json
import aiohttp
from dataclasses import dataclass, asdict
from abc import ABC

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class ApiUser :
    name: str
    username: str
    email: str

@dataclass
class ApiPost :
    title : str
    body : str
    user_id : int


async def get_request_json(url: str, entity_id: int) -> "json":
    async with aiohttp.ClientSession() as session:
        responce = await session.get(f"{url}/{entity_id}")
        data = await responce.json()
    return data

async def get_users() :
    tasks = {asyncio.create_task(get_request_json(USERS_DATA_URL, user_id)) 
             for user_id in range(1,11)}
    done, pending = await asyncio.wait(tasks)
    result = []
    for item in done :
        name, username, email = item.result().get('name'), item.result().get('username'), item.result().get('email')
        # result.append(asdict(ApiUser(name=name, username=username, email=email)))
        result.append(ApiUser(name=name, username=username, email=email))
        t_err = item.exception()
        if t_err :
            print("Something get wrong", t_err)
    return result

async def get_posts() :
    tasks = {asyncio.create_task(get_request_json(POSTS_DATA_URL, post_id)) 
             for post_id in range(1,101)}
    done, pending = await asyncio.wait(tasks)
    result = []
    for item in done :
        title, body, user_id = item.result().get('title'), item.result().get('body'), item.result().get('userId')
        # result.append(asdict(ApiPost(title=title, body=body, user_id=user_id)))
        result.append(ApiPost(title=title, body=body, user_id=user_id))
        t_err = item.exception()
        if t_err :
            print("Something get wrong", t_err)
    return result