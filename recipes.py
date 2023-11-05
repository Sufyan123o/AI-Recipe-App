import taipy
from taipy.gui import Gui, notify
import requests


query = 'italian wedding soup'
api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)

api_key = 'MFks516zCAAoxbvc84Cqvg==N7f2fH8PJzPLuF6k'

headers = {'X-Api-Key': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == requests.codes.ok:
    # Parse the JSON response content
    data = response.json()
    print(data)
    # Check if the response is a list with at least three elements
    if isinstance(data, list) and len(data) >= 3:
        recipe1 = data[0]
        recipe2 = data[1]
        recipe3 = data[2]
        
        recipes = [recipe1, recipe2, recipe3]
    else:
        print("API response does not contain at least three recipes.")
else:
    print("Error:", response.status_code, response.text)



recipe_blocks = """
<|"{}"|button|on_action=display_recipe1|>

<|"{}"|button|on_action=display_recipe2|>

<|"{}"|button|on_action=display_recipe3|>
""".format(recipe1['title'], recipe2['title'], recipe3['title'])

recipes_md = """
# Your Personalised Recipes

{}

<|Generate More Recipes|button|on_action=generate_more_recipes|>

""".format(recipe_blocks)

# Function to be called when a recipe is clicked, displays the recipe
def display_recipe_names(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    
def generate_more_recipes(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed, still need to do this"

# recipe button 1 clicked
def display_recipe1(state):
    notify(state, 'info', f'The text is: {state.text}')
    print("display recipe 1")
    display_full_recipe(recipe1)

# recipe button 2 clicked
def display_recipe2(state):
    notify(state, 'info', f'The text is: {state.text}')
    print("display recipe 2")
    display_full_recipe(recipe2)

# recipe button 3 clicked
def display_recipe3(state):
    notify(state, 'info', f'The text is: {state.text}')
    print("display recipe 3")
    display_full_recipe(recipe3)

# Function to display the full recipe on another page
def display_full_recipe(recipe):
    notify(recipe['title'])
