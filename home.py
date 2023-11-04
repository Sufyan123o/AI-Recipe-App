from taipy.gui import Markdown

text = "Welcome to the Taipy multi-page tutorial app!"

home_md = Markdown("""
# Home

<|{text}|>
""")
