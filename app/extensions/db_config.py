from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, Integer, func
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()
migrate = Migrate()


class Base(db.Model):  # type: ignore
    """
    Base class with the fields to a database entity

    Attributes:
        id (int): Entity's primary key
        uuid (uuid4): Entity's unique identifier to be used on endpoints
        date_created (datetime): The creation date of the entity
        date_modified (datetime): Last time the entity was modified
        active (bool): Indicates if the entity is active
    """

    __abstract__ = True

    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    uuid = db.Column(UUID(), unique=True, default=func.uuid_generate_v4())
    date_created = Column(DateTime, default=func.current_timestamp())
    date_modified = Column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )

    active = Column(Boolean, nullable=False, default=True)
