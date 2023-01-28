from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, func


class intPkMixin:
    id = Column(Integer, primary_key=True)


class createdAtMixin:
    created_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, server_default=func.now()
    )
