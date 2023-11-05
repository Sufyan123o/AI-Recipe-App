from taipy.gui import Gui, navigate
from home import home_md
from ingredients import ingredients_md
from recipes import recipes_md

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "home": home_md,
    "ingredients": ingredients_md,
    "recipes": recipes_md
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)


stylekit = {
  "color_primary": "#BADA55",
  "color_secondary": "#C0FFE",
}

gui = Gui(pages=pages)
gui.run(run_browser=False, use_reloader=True, port = 8008)
