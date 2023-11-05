from taipy.gui import Gui, navigate
from home import home_md
from ingredients import ingredients_md
from recipes import recipes_md

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "Home": home_md,
    "Ingredients": ingredients_md,
    "Recipes": recipes_md
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)
    
stylekit = {
    "color_primary": "#D6FD05",
    "color_secondary": "#5ED179",
    "spacing": "50px",
}


gui = Gui(pages=pages)
gui.run(run_browser=False, use_reloader=True, stylekit=stylekit, port = 8008)