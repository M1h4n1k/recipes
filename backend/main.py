from fastapi import Depends, FastAPI, Response, Cookie
from starlette.middleware.cors import CORSMiddleware
import os
import uvicorn

import crud
import schemas

ADMIN_KEY = os.getenv('ADMIN_KEY') or '1aEQw41ENGwEcr0s'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_user_id(response: Response, user_id: str | None = Cookie(default=None)) -> str:
    """
    Function to get user_id from cookie, or generate a new one if it's not present. Used to track user's recipes.
    I don't want to implement a complete login system, cuz imho it's an overkill in current situation
    :param response: response object
    :param user_id: user_id from cookie or none
    :return: user_id
    """
    if user_id is None:
        user_id = os.urandom(16).hex()
        response.set_cookie(key="user_id", value=user_id)
    return user_id


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recipes")
async def get_recipes(user_id: str = Depends(get_user_id)):
    recipes = await crud.get_recipes()
    fridge = await crud.get_fridge(user_id)
    fridge = [ingredient['name'] for ingredient in fridge]
    for recipe in recipes:
        recipe['completeness'] = sum([ing['name'] in fridge for ing in recipe['ingredients']]) / len(recipe['ingredients'])
        recipe['completeness'] = round(recipe['completeness'] * 100)
    return recipes


@app.get("/recipe/{recipe_id}")
async def get_recipe(recipe_id: str):
    return await crud.get_recipe(recipe_id)


@app.post("/recipe")
async def create_recipe(recipe: schemas.Recipe, user_id: str = Depends(get_user_id)):
    recipe.author = user_id
    return await crud.create_recipe(recipe)


@app.get("/fridge")
async def get_fridge(user_id: str = Depends(get_user_id)):
    return await crud.get_fridge(user_id)


@app.post("/fridge")
async def add_to_fridge(ingredient: schemas.FridgeIngredient, user_id: str = Depends(get_user_id)):
    ingredient.owner = user_id
    return await crud.add_to_fridge(ingredient)


@app.patch("/fridge")
async def update_fridge(ingredient: schemas.FridgeIngredient, user_id: str = Depends(get_user_id)):
    ingredient.owner = user_id
    return await crud.update_fridge(ingredient)


@app.delete("/fridge")
async def delete_from_fridge(_id: str, user_id: str = Depends(get_user_id)):
    return await crud.delete_from_fridge(_id, user_id)


@app.post("/ingredients")
async def add_known_ingredient(ingredient: schemas.KnownIngredient, admin_key: str):
    if admin_key != ADMIN_KEY:
        return {'message': 'Not authorized'}
    return await crud.add_known_ingredient(ingredient)


@app.get("/ingredients")
async def get_known_ingredients():
    return await crud.get_known_ingredients()

