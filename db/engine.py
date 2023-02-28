from typing import AsyncGenerator, List
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from settings.setting import PG_HOST, PG_PORT, PG_USER, PG_PASS, PG_DB_NAME
from orm.models import Base, AuthUser, Picture

# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"

DATABASE_URL = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# METHODS - with async connection
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, AuthUser)


async def get_picture_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Picture)
