from .base import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import relationship
from .mixins import createdAtMixin, intPkMixin
from .database import db


class Post(db.Model, Base, intPkMixin, createdAtMixin):
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)

    user = relationship("User", back_populates="posts", uselist=False)
