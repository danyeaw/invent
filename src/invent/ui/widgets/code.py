"""
A minimal area of the UI containing CODE content.
"""

from invent.ui.core import Widget, TextProperty
from pyscript import document


_default = """
def hello(name="world"):
    return f"Hello, {name}"
"""


class Code(Widget):
    code = TextProperty("The code to display.", default_value=_default)

    @classmethod
    def preview(cls):
        return '<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 256 256"><path fill="currentColor" d="M69.12 94.15L28.5 128l40.62 33.85a8 8 0 1 1-10.24 12.29l-48-40a8 8 0 0 1 0-12.29l48-40a8 8 0 0 1 10.24 12.3m176 27.7l-48-40a8 8 0 1 0-10.24 12.3L227.5 128l-40.62 33.85a8 8 0 1 0 10.24 12.29l48-40a8 8 0 0 0 0-12.29m-82.39-89.37a8 8 0 0 0-10.25 4.79l-64 176a8 8 0 0 0 4.79 10.26A8.14 8.14 0 0 0 96 224a8 8 0 0 0 7.52-5.27l64-176a8 8 0 0 0-4.79-10.25"/></svg>'  # noqa

    def on_code_changed(self):
        self.element.innerText = self.code

    def render(self):
        element = document.createElement("pre")
        element.id = self.id
        element.innerText = self.code
        return element
