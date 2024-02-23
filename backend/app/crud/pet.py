from sqlalchemy import Session
from ..models import Pet
from typing import Optional, List

from ..api.schemas import PetCreate


async def create_pet(owner_id: int, pet_create: PetCreate, db: Session) -> Pet:
    pet = Pet(
        type=pet_create.type,
        breed=pet_create.breed,
        avatar=pet_create.avatar,
        name=pet_create.name,
        age=pet_create.age,
        weight=pet_create.weight,
        able_to_donat=pet_create.able_to_donate,
        owner_id=owner_id
    )
    db.add(pet)
    await db.commit()
    await db.refresh(pet)

    return pet


async def update_pet(pet_id: int, pet_update: PetCreate, db: Session) -> Pet:
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet:
        for key, value in pet_update.dict().items():
            setattr(pet, key, value)
        await db.commit()
        await db.refresh(pet)
        return pet
    else:
        raise ValueError(f"Pet with id {pet_id} not found")


async def get_pet(pet_id: int, db: Session) -> Pet:
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet:
        return pet
    raise ValueError(f"Pet with id {pet_id} not found")


async def get_pets_by_params(db: Session) -> List[Pet]:
    return db.query(Pet).all()