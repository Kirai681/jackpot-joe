import asyncpg
from asyncpg.connection import Connection
from typing import Any
from typing import Optional


class Database:
    """ """

    def __init__(self, url: str) -> None:
        """ """
        self.url = url
        self.pool = None

    async def connect(self) -> None:
        """ """
        if self.pool is not None:
            return
        self.pool = await asyncpg.create_pool(self.url, min_size=1, max_size=10)

    async def execute(self, query: str, *args: Any) -> None:
        """ """
        assert self.pool is not None
        async with self.pool.acquire() as connection:
            assert isinstance(connection, Connection)
            await connection.execute(query, *args)

    async def fetchone(self, query: str, *args: Any) -> Optional[Any]:
        """ """
        assert self.pool is not None
        async with self.pool.acquire() as connection:
            assert isinstance(connection, Connection)
            return await connection.fetchrow(query, *args)
