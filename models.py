import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
from database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("full_name", String),
    Column("age", Integer)
)


tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("task_name", String),
    Column("status", Boolean, default=False),
    Column("priority", Integer, nullable=False)
)
