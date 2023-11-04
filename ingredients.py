from taipy.gui import Gui, notify

def display_ingredients(ingredientsArray):
    for ingredient in ingredientsArray:
        print(ingredient)

# Function to be called when the generate_recipes button is clicked
def generate_recipes_clicked(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

# Function to be called when the X button is clicked, it will delete the ingredient
def delete_ingredient(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"
    

Gui(page).run(use_reloader=True, port=8008)