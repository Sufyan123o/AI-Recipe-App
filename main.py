from taipy.gui import Gui, navigate
from home import home_md
from ingredients import ingredients_md

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "home": home_md,
    "ingredients": ingredients_md,
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

gui = Gui(pages=pages)
gui.run(run_browser=False, use_reloader=True, port = 8008)
