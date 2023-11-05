from taipy.gui import Markdown
from taipy import Gui
import cv2
import base64

# Create a global variable to store the uploaded image
uploaded_image = None

def camera():
    pass

def submit_scenario(state):
    global uploaded_image
    state.scenario.input_name.write(state.input_name)

    # Assuming 'file_selector' is the name of the file input field
    uploaded_file = state.scenario.file_selector.files[0]

    if uploaded_file:
        # Process the uploaded image (you can save it or perform other operations)
        uploaded_image = uploaded_file.read()

    state.scenario.submit(wait=True)

def accessibility_mode(state):
    state.scenario.accessibility_mode.click()

# Define the 'text' and 'content' variables
text = "Show Your Ingredients:"
content = "your_content_here"  # You should replace this with the actual content

# Create the Markdown component
home_md = Markdown(f"""
# Home
<|{text}|>
                                      
<|{content}|file_selector|label=Upload Images|on_action=function_name|extensions=.jpg,.png|drop_message=Drop Message|>
                   
<|{content}|image|label=this is an image|on_action=function_name|>
                   
<|{content}|image|>
                   
<|submit|button|on_action=submit_scenario|>
<|Accesibility Mode|button|on_action=accessibility_mode|>

<|✓|button|>
<|X|button|>
""")
