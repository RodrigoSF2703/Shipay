import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import text
from models.base import Base  # ou onde está seu Base

MAX_RETRIES = 10
RETRY_DELAY = 1  # segundos


async def create_tables(engine: AsyncEngine) -> None:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with engine.begin() as conn:
                # testando conexão explicitamente
                await conn.execute(text("SELECT 1"))

                # cria tabelas
                await conn.run_sync(Base.metadata.create_all)

            print("Database conectado e tabelas criadas")
            return

        except Exception as e:
            print(f"Banco não pronto (tentativa {attempt}/{MAX_RETRIES})")
            await asyncio.sleep(RETRY_DELAY)

    raise RuntimeError("Banco não ficou disponível a tempo")
