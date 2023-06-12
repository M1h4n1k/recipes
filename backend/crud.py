from fastapi.encoders import jsonable_encoder

import schemas
from schemas import db


async def get_recipes():
    return await db['recipes'].find().to_list(100)


async def get_recipe(recipe_id: str):
    return await db['recipes'].find_one({"_id": recipe_id})


async def create_recipe(recipe: schemas.Recipe):
    recipe = jsonable_encoder(recipe)
    new_recipe = await db['recipes'].insert_one(recipe)
    return await db['recipes'].find_one({"_id": new_recipe.inserted_id})


async def get_fridge(user_id: str):
    return await db['fridges'].find({"owner": user_id}).to_list(1000)


async def add_to_fridge(ingredient: schemas.FridgeIngredient):
    ingredient = jsonable_encoder(ingredient)
    new_ingredient = await db['fridges'].insert_one(ingredient)
    return await db['fridges'].find_one({"_id": new_ingredient.inserted_id})


async def update_fridge(ingredient: schemas.FridgeIngredient):
    ingredient = jsonable_encoder(ingredient)
    await db['fridges'].update_one({"_id": ingredient['_id']}, {"$set": ingredient})
    return await db['fridges'].find_one({"_id": ingredient['_id']})


async def delete_from_fridge(ingredient_id: str, user_id: str):
    await db['fridges'].delete_one({"_id": ingredient_id, 'owner': user_id})
    return 'OK'


async def add_known_ingredient(ingredient: schemas.KnownIngredient):
    ingredient = jsonable_encoder(ingredient)
    new_ingredient = await db['ingredients'].insert_one(ingredient)
    return await db['ingredients'].find_one({"_id": new_ingredient.inserted_id})


async def get_known_ingredients():
    return await db['ingredients'].find().to_list(1000)
