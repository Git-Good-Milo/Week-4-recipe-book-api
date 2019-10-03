# Define a class recipe
import json
import requests
class Recipe():

    def __init__(self, recipe_name, ingredients, post_code):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.post_code = post_code

    def append_a_recipe_to_file(self):
        try:
            with open('recipe.txt', 'a') as opened_file:
                opened_file.write(self.recipe_name + self.ingredients + self.post_code + '\n' )

        except FileNotFoundError:
            print("File not found")


















    # Give it the need attributes

    # defining methods

    # new()
        # create a recipe object

    # save()
        # saves a recipe object to the DB (make persistant)

    # read()
        # reads one object

    # all() # have this on the class db
        # gets all the the instances from a DB
        # get each record and create individual instances of recipes
        # creat individual instances of recipe
        # store them in a list
        # return a list

    # Destroy
        # one object
