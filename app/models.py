import datetime
from config import PG_DSN
from sqlalchemy import DECIMAL, DateTime, Integer, String, func
from sqlalchemy.ext.asyncio import (
    AsyncAttrs, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    PG_DSN,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):

    @property
    def id_dict(self):
        return {"id": self.id}


class Adv(Base):
    __tablename__ = "adv"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(DECIMAL, nullable=False)
    author: Mapped[int] = mapped_column(String, nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    recent_changes: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=True)

    @property
    def dict(self):
        if self.recent_changes is None:
            add_time = None
        else:
            add_time = self.recent_changes.isoformat()
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "author": self.author,
            "creation_date": self.creation_date.isoformat(),
            "recent_changes": add_time,
        }


ORM_OBJECT = Adv
ORM_CLS = type[Adv]
