import taipy
from taipy.gui import Gui, notify
import requests

query = 'burger'
api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)

api_key = 'MFks516zCAAoxbvc84Cqvg==N7f2fH8PJzPLuF6k'

headers = {'X-Api-Key': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == requests.codes.ok:
    # Parse the JSON response content
    data = response.json()
    
    # Check if the response is a list with at least three elements
    if isinstance(data, list) and len(data) >= 3:
        title1 = data[0]['title']
        title2 = data[1]['title']
        title3 = data[2]['title']
        
        titles = [title1, title2, title3]
        print(titles)
    else:
        print("API response does not contain at least three recipes.")
else:
    print("Error:", response.status_code, response.text)


# Function to be called when a recipe is clicked, displays the recipe
def display_recipe_names(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    
def display_full_recipe(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    
def generate_more_recipes(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"


recipe_blocks = "\n\n".join('<|"{}"|button|on_action=display_full_recipe|>'.format(title) for title in titles)

recipes_md = """
# Your Personalised Recipes

{}

<|Generate More Reciples|button|on_action=generate_more_recipes|>

""".format(recipe_blocks)