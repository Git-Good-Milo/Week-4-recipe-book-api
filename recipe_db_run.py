from recipe_db import *
from recipe_class import *
from postcode_request_for_recipe import *



# Set variables for a user to manuipulate recipes
recipe_name = " "
ingredients = " "
postcode = " "

# Connect to the recipe database
connect_to_recipe_db = ConnectMsS('Passw0rd2018')
recipe1 = Recipe("Milo Spag Bowel", "Spagetti, beef mince, canned tomatoes, beef stock, onions, garlic, thyme, rosmery", "N85 9LN")
recipe2 = Recipe("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N169LN")
recipe3 = Recipe("American Pancakes", "Freedom", "90210")
#user_recipe = Recipe(f"'{recipe_name}', '{ingredients}', '{postcode}'")


# Use methods to add a recipe to the database

#connect_to_recipe_db.add_recipe_to_db("tasty Cookies", "chocolate, milk, eggs, flour, butter", "N16 9LN")
#connect_to_recipe_db.add_recipe_to_db(recipe3.recipe_name, recipe3.ingredients, recipe3.post_code)

# Use methods to remove a recipe from the database

#connect_to_recipe_db.delete_recipe_from_db("American Pancakes")

# Use Methods to view all recipes, or a specific recipe

# print(connect_to_recipe_db.read_all_recipes())
# print(connect_to_recipe_db.title_search("tasty Cookies"))

# Use methods to add a recipe to a txt file

# recipe1_to_txt = recipe1.append_a_recipe_to_file()
# recipe2_to_txt = recipe2.append_a_recipe_to_file()
# recipe3_to_txt = recipe3.append_a_recipe_to_file()

# Use method to pull more postcode information from API

#info_recipe2 = get_post_code(recipe2.post_code)
# print(info_recipe2)


#print(recipe2.post_code)
#print(get_post_code("N16 9LN"))

welcome_statement = print("Good morning and welcome to the best recipe website in the Universe! Here are your options:")

option_1 = print("Would you like to add a recipe to our ilustrious database?")
option_2 = print("Would you like to view all recipes or just one?")
option_3 = print("Would you like to delete a shoddy recipe from our database?")
option_4 = print("Would you like to export a recipe to a .txt file?")
user_input = input("Enter your choice:  ")

while True:
    if user_input == "1":
        get_recipe = input("'Please enter your recipe name: '")
        get_ingridiant = input("'Please enter your ingreiants: '")
        get_postCode = input("'Please enter your postcode: '")
        user_recipe = connect_to_recipe_db.add_recipe_to_db(get_recipe,get_ingridiant,get_postCode)
        print(f"{user_recipe.recipe_name} has been added to the database :)")

    elif user_input == "2":
        view_recipe_s = input("Would you like to view one recipe or all of them?")
        if view_recipe_s == "1":
            view_by_title = connect_to_recipe_db.title_search
        elif view_recipe_s == "all":
            view_all = connect_to_recipe_db.read_all_recipes()
        else:
            print("Sorry, I didnt quite get that")
            break

    elif user_input == "3":
        print("Which recipe would you like to delete?")
        delete_recipe = connect_to_recipe_db.delete_recipe_from_db
        print("That recipe has been deleted")

    # elif user_input == "4":
    #     input_recipe_for_txt = input("Which recipe would you like to export?")
    #
    #     if input_recipe_for_txt == user_recipe.recipe_name:
    #         recipe_to_export = user_recipe.append_a_recipe_to_file()
    #
    #     elif input_recipe_for_txt == "I'd like to choose a recipe":
    #         recipe_to_choose = input("Which recipe will it be then?")
    #
    #         if recipe_to_choose ==

    elif user_input == "exit":
        break











