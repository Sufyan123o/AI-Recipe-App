from taipy.gui import Markdown



def camera():
    pass

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)

    state.scenario.submit(wait=True)

def accessibility_mode(state):
    state.scenario.accessibility_mode.click()
    
text = "Show Your Ingredients:"
home_md = Markdown("""
# Cookaid
## Home

<|{text}|>

<|submit|button|on_action=submit_scenario|>
<|Accesibility Mode|button|on_action=accessibility_mode|>

<|✓|button|>
<|X|button|>

""")
