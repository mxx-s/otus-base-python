import asyncio
from jsonplaceholder_requests import (get_users, get_posts)

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


async def async_main():
    users_dict, post_dict = await asyncio.gather(get_users(), get_posts())
    
    for elem in users_dict:
      print(elem.name, elem.username, elem.email)
    
    for elem in post_dict:
      print(elem.__dict__)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
