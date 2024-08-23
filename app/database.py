from datetime import datetime, timezone
from sqlalchemy import MetaData, text
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData()


class BaseModel(DeclarativeBase):
    metadata = metadata

    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.now(timezone.utc)
    )
