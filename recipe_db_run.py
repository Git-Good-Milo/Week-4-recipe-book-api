from recipe_db import *
from recipe_class import *

# Connect to the recipe database

connect_to_recipe_db = ConnectMsS('Passw0rd2018')
recipe1 = Recipe("Milo Spag Bowel", "Spagetti, beef mince, canned tomatoes, beef stock, onions, garlic, thyme, rosmery", "N85 9LN")
recipe2 = Recipe("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")
db_recipe = Recipe(recipe.recipe_name, recipe.ingredients, recipe.post_code)
#print(add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN"))

# Use methods to add a recipe to the database

#connect_to_recipe_db.add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")
#connect_to_recipe_db.add_recipe_to_db(recipe.recipe_name, recipe.ingredients, recipe.post_code)

# Use methods to remove a database

#connect_to_recipe_db.delete_recipe_from_db("Milo Spag Bowel")

# Use Methods to view all recipes, or a specific recipe
# print(connect_to_recipe_db.read_all_recipes())
# print(connect_to_recipe_db.title_search("tasty Cookies"))

# Use methods to add a recipe to a txt file
recipe_to_txt = recipe.append_a_recipe_to_file()