# type:ignore  -- customtkinter has no stubfile
"""Simple GUI to allow the user to try out various conversion paradigms."""

from tkinter import ttk
from customtkinter import (CTk,
                           CTkTextbox,
                           CTkOptionMenu)

from src.bases.converter import TextConverter
from src.languages import greek_polytonic, latin


__all__ = ["ConverterGUI"]


class ConverterGUI(CTk):
    """Basic GUI for text entry and conversion."""

    def __init__(self):
        super().__init__()

        self.converters: dict[str, TextConverter] = {
            "Polytonic Greek": greek_polytonic.greek_converter,
            "Latin": latin.latin_converter
        }
        self.selected_converter: str = list(self.converters)[0]

        # Interface Layout
        #
        #       +----+----------------+
        #       |    |      B         |
        #       | A  +----------------+ D
        #       |    |      C         |
        #       +----+----------------+

        # A: Dropdown menu
        self.option_menu = CTkOptionMenu(
            self, values=list(self.converters), command=self.change_state)
        self.option_menu.grid(column=0, row=0, rowspan=3, sticky='N')

        # B: Text entry box
        self.input = CTkTextbox(self, width=600)
        self.input.bind("<KeyRelease>", self.update_text)
        self.input.configure(font=("times new roman", 26))
        self.input.grid(column=1, row=0)

        # C: Converted text display box
        self.output = CTkTextbox(self, wrap="word", width=600, state="disabled")
        self.output.configure(font=("times new roman", 26))
        self.output.grid(column=1, row=2)

        # D: Input/Output divider
        self.sep = ttk.Separator(self)
        self.sep.grid(column=1, row=1, sticky="NSEW")

    def change_state(self, converter_name: str) -> None:
        """Change which converter to use."""
        self.selected_converter = converter_name
        self.update_text()

    def update_text(self, *args) -> None:
        """Replace the current text with a newly parsed conversion."""
        converter: TextConverter = self.converters[self.selected_converter]
        text: str = self.input.get("1.0", "end")
        conversion = str(converter.convert(text))
        self.output.configure(state="normal")
        self.output.delete("0.0", "end")
        self.output.insert("0.0", conversion)
        self.output.configure(state="disabled")

