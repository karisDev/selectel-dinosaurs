from pydantic import BaseModel, HttpUrl
from typing import TYPE_CHECKING
from datetime import datetime


class VaccineDto(BaseModel):
    id: int
    name: str
    date: datetime
    expire_date: datetime


class VaccineCreate(BaseModel):
    name: str
    date: datetime
