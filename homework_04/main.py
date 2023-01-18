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
from jsonplaceholder_requests import get_users, get_posts

from models import (
    AsyncSession,
    async_engine,
    Base,
    Session,
    User,
    Post,
)


async def recreate_all_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def create_user(
    session: AsyncSession, id: int, name: str, username: str, email: str
) -> User:
    user = User(
        id=id,
        name=name,
        username=username,
        email=email,
    )
    session.add(user)
    # session.commit()
    print("User created: ", user)

    return user


def create_post(
    session: AsyncSession,
    id: int,
    title: str,
    body: str,
    user: User,
) -> Post:
    post = Post(
        id=id,
        title=title,
        body=body,
        user=user,
    )
    session.add(post)
    # session.commit()
    print("Post created ", post)

    return post


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user: User | None = await session.get(User, user_id)

    print("user", user)
    return user


async def async_main():

    await recreate_all_tables()

    users_dicts, post_dicts = await asyncio.gather(get_users(), get_posts())

    async with Session() as session:
        for api_user in users_dicts:
            # print(api_user.name, api_user.username, api_user.email)
            create_user(
                session=session,
                id=api_user.id,
                name=api_user.name,
                username=api_user.username,
                email=api_user.email,
            )

        for api_post in post_dicts:
            # print(api_post.__dict__)
            user_post = await get_user_by_id(session, api_post.user_id)
            create_post(
                session=session,
                id=api_post.id,
                title=api_post.title,
                body=api_post.body,
                user=user_post,
            )
        await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
