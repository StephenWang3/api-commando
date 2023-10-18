from fastapi import APIRouter
from . import api, test_api

router = APIRouter()
router.include_router(api.router)
router.include_router(test_api.router)