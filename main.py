from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.v1.routes_roles import router as roles_router
from api.v1.routes_users import router as users_router
from core.database import engine, AsyncSessionLocal
from core.init_db import create_tables
from core.seed import seed_database
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # cria tabelas sempre (ambiente de teste)
    await create_tables(engine)

    # popula banco apenas se configurado
    if settings.seed_database:
        async with AsyncSessionLocal() as session:
            await seed_database(session)

    yield


app = FastAPI(
    title="User & Roles API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(roles_router, prefix="/api/v1", tags=["Roles"])
app.include_router(users_router, prefix="/api/v1", tags=["Users"])
