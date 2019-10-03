from recipe_db import *
from recipe_class import *

# Connect to the recipe database

connect_to_recipe_db = ConnectMsS('Passw0rd2018')
recipe1 = Recipe("Milo Spag Bowel", "Spagetti, beef mince, canned tomatoes, beef stock, onions, garlic, thyme, rosmery", "N85 9LN")
recipe2 = Recipe("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")
recipe3 = Recipe("American Pancakes", "Freedom", "90210")

# Use methods to add a recipe to the database

#connect_to_recipe_db.add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")
connect_to_recipe_db.add_recipe_to_db(recipe3.recipe_name, recipe3.ingredients, recipe3.post_code)

# Use methods to remove a recipe from the database

#connect_to_recipe_db.delete_recipe_from_db("American Pancakes")

# Use Methods to view all recipes, or a specific recipe

# print(connect_to_recipe_db.read_all_recipes())
# print(connect_to_recipe_db.title_search("tasty Cookies"))

# Use methods to add a recipe to a txt file

recipe1_to_txt = recipe1.append_a_recipe_to_file()
recipe2_to_txt = recipe2.append_a_recipe_to_file()
recipe3_to_txt = recipe3.append_a_recipe_to_file()