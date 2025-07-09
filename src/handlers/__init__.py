import aiogram

from .restriction import router as restriction_router

router = aiogram.Router()


router.include_router(restriction_router)
