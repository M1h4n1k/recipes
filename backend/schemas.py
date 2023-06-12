from pydantic import BaseModel, Field
from bson import ObjectId
import motor.motor_asyncio
import os
from datetime import datetime


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGODB_URL") or "mongodb://localhost:27017")
db = client.recipes


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Ingredient(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class FridgeIngredient(Ingredient):
    quantity: str = Field(...)
    owner: str = Field(None)
    unit: str = Field(None)


class RecipeIngredient(Ingredient):
    quantity: str = Field(...)
    unit: str = Field(None)


class KnownIngredient(Ingredient):
    unit: str = Field(...)


class Step(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    text: str = Field(...)
    # time: DateElement = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class Recipe(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    image: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    author: str | None = Field(None)
    ingredients: list[RecipeIngredient] = Field(...)
    steps: list[Step] = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

