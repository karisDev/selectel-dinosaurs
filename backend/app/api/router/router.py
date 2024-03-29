from fastapi import APIRouter, Depends

from ...db import Database
from .user import router as user_router
from .auth import router as auth_router
from .bank import router as bank_router
from .blood_donation import router as blood_donation_router
from .blood_request import router as blood_request_router
from .vaccine import router as vaccine_router
from .social import router as social_router
from .bank_request import router as bank_request_router
from .bank_donation import router as bank_donation_router

from .pet import router as pet_router


# from .user import router as user_router


def create_api_router(db: Database, prefix: str = "/api") -> APIRouter:
    router = APIRouter(
        prefix=prefix,
    )

    router.include_router(user_router, tags=["user"])

    router.include_router(auth_router, tags=["auth"])

    router.include_router(bank_router, tags=["bank"])

    router.include_router(blood_donation_router, tags=["blood_donation"])

    router.include_router(blood_request_router, tags=["blood_request"])

    router.include_router(pet_router, tags=["pet"])

    router.include_router(vaccine_router, tags=["vaccine"])
    router.include_router(social_router, tags=["social"])

    router.include_router(bank_request_router, tags=["bank_request"])
    router.include_router(bank_donation_router, tags=["bank_donation"])
    return router
