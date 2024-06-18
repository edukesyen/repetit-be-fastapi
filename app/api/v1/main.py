from fastapi import APIRouter

from app.api.v1.routes import test

api_router = APIRouter()

api_router.include_router(test.router, prefix="/test", tags=["labs"])

# api_router.include_router(login.router, tags=["login"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
# api_router.include_router(labs.router, prefix="/labs", tags=["labs"])