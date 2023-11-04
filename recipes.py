from taipy.gui import Gui, notify


# Function to be called when a recipe is clicked, displays the recipe
def display_recipe(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    
def generate_more_recipes_clicked(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def favourite_recipe(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    
# Definition of the page
page = """
# Your Personalised Recipes

<|layout|columns=1 1|
<|Recipe|button|on_action=display_recipe|>

<|Favourite|button|on_action=favourite_recipe|>
|>

<|Generate More Reciples|button|on_action=generate_more_recipes|>
"""

