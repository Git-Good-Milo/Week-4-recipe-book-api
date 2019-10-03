import pyodbc

# Define a class as a recipe database
class ConnectMsS():

    # have the characteristcs to access the db
    def __init__(self, password, server = 'localhost,1433', database = 'recipe_db', username = 'SA'):
        self.server = server
        self.database = database
        self.username =username
        self.password = password
        self.conn_rep_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_rep_db.cursor()

    # defining methods
    def filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.filter_query(query)


    # def return_all_product_details(self):
    #     query_rows = self.filter_query()

    def sql_query_fetchone(self, query):
        return self.filter_query(query).fetchone()

    def title_search(self, input_title):
        title = self.sql_query_fetchone(f"SELECT * FROM recipe_list WHERE [Recipe Name] = '{input_title}'")
        return title

    # Add a recipe to the existing database
    def add_recipe_to_db(self, recipe_name, ingredients, post_code):
            self.filter_query(f"INSERT INTO recipe_list VALUES ('{recipe_name}', '{ingredients}', '{post_code}')")
            self.conn_rep_db.commit()

    # Delete a recipe from the database
    def delete_recipe_from_db(self, recipe_to_remove):
        self.filter_query(f"DELETE FROM recipe_list WHERE [Recipe Name] = '{recipe_to_remove}'")
        self.conn_rep_db.commit()

        # View all of the recipe details
        def read_all_recipes(self):
            query_rows = self.filter_query("SELECT * FROM recipe_list")
            while True:
                record = query_rows.fetchone()
                if record is None:
                    break
                return record

    # all() # Have this on the db_class
        # gets al the other instances form db
        # get each record
        # create individual instances of recipe




