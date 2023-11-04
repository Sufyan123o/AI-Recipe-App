from taipy.gui import Gui, navigate
from pages.home import home_md
from pages.temperature import temperature_md

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "home": home_md,
    "temperature": temperature_md,
}
page_names = [page for page in pages.keys() if page != "/"]

def menu_action(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

gui = Gui(pages=pages)
gui.run(run_browser=False, use_reloader=True)
