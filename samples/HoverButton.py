from src.Stylehandler import Stylehandler
from tkinter import *


class HoverButton(Button):
    """A TK Button that changes styles when you hover over it (utilises Stylehandler)"""

    def __init__(self, parent, regular_style: str, hover_style: str, *args, **kwargs):
        """
        :param parent: parent widget
        :param regular_style: the style to be applied normally
        :param hover_style: the style to be applied when hovering over the button
        :param args: args for the button
        :param kwargs: kwargs for the button
        """

        super().__init__(parent, *args, **kwargs)
        Stylehandler.apply(self, regular_style)
        self.bind("<Enter>", lambda _: Stylehandler.apply(self, hover_style))
        self.bind("<Leave>", lambda _: Stylehandler.apply(self, regular_style))


if __name__ == "__main__":
    root = Tk()

    Stylehandler.styles = {
        "HoverButtonActive": {
            "background": "Pink",
            "foreground": "Black",
        },
        "HoverButtonInactive": {
            "background": "Purple",
            "foreground": "White"
        }
    }

    button = HoverButton(root, "HoverButtonInactive", "HoverButtonActive", text="Click me")
    button.pack()

    root.mainloop()
