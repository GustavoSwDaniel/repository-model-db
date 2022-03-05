from sqlalchemy import select

from src.repositories.irepository import IRepository
from src.models import Base

class SqlRepository(IRepository):
    model = Base

    async def get_all(self):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()