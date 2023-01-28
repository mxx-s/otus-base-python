from .base import Base
from sqlalchemy import (
    Column,
    String,
    Boolean,
)

from sqlalchemy.orm import relationship
from .mixins import createdAtMixin, intPkMixin
from .database import db


class User(db.Model, Base, intPkMixin, createdAtMixin):
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    is_displayed = Column(Boolean, default=True, server_default="TRUE")

    posts = relationship("Post", back_populates="user")
