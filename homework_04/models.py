from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
                declarative_base, 
                declared_attr,
                sessionmaker,
                relationship,
)
from sqlalchemy import ( 
                       Column,
                       Integer,
                       String,
                       Boolean,
)
"""
создайте асинхронный алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session на основе класса AsyncSession
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

PG_URI = "postgresql+pg8000://usr:qwerty@0.0.0.0:5432/homework4"
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://usr:qwerty@0.0.0.0:5432/homework4"
PG_DB_ECHO = True

async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=PG_DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base :

    @declared_attr
    def __tablename__(cls) :
        """
        User -> users
        Author -> authors
        """
        return f"{cls.__name__.lower()}s"

    def __repr__(self):
        return str(self)

Base = declarative_base(bind=async_engine, cls=Base)
# Session = None


class IntPkMixin() :
    id = Column(Integer, primary_key=True)


class User(IntPkMixin, Base) :
# class User(Base) :
    name = Column(String(50), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    is_staff = Column(Boolean, default=False, server_default="FALSE")

    # author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self)->str :
        return (f"{self.__class__.__name__}("
                f"id={self.id},"
                f"username={self.username!r},"
                f"email={self.email!r},"
                # f"is_staff={self.is_staff},"
                # f"created_at={self.created_at},"
                ")"
        )