from recipe_db import *

# Connect to the recipe database
connect_to_recipe_db = ConnectMsS('Passw0rd2018')

#print(add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN"))

#connect_to_recipe_db.add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")

print(connect_to_recipe_db.read_all_recipes())

print(connect_to_recipe_db.title_search("tasty Cookies"))