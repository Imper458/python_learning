from fastapi import APIRouter

router = APIRouter(prefix="/api/news",tags=["新闻"])

@router.get("/categories")
async def get_categories():
    return {'msg':'hello'}