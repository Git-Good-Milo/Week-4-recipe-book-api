# Create a class to allow pulling of online APIs
import requests
import json

def get_post_code(input_post_code):
    try:
        request_post_code = requests.get('https://api.postcodes.io/postcodes/' + input_post_code)
        return_postcode = request_post_code.json()["result"]["postcode"]

        return return_postcode
    except ConnectionError:
