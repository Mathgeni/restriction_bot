import aiogram

from src.handlers.test import router as test_router


router = aiogram.Router()


router.include_router(test_router)



