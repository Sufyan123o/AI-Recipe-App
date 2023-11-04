from taipy.gui import Gui, notify

text = "Original text"

# Definition of the page
page = """
# Ingredients Cart

<|layout|columns=1 1|
Ingredient

<|X|button|>
|>

<|Generate Reciples|button|on_action=generate_recipes_clicked|>
"""

def generate_recipes_clicked(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

Gui(page).run(use_reloader=True, port=8008)