# type:ignore  -- customtkinter has no stubfile
"""Simple GUI to allow the user to try out various conversion paradigms."""

from tkinter import ttk
from customtkinter import (CTk,
                           CTkTextbox,
                           CTkOptionMenu)
from src.bases.converter import TextConverter
from src.languages import greek_polytonic, latin


class ConverterGUI(CTk):
    """Basic GUI for text entry and conversion."""

    def __init__(self):
        super().__init__()
        self.title = "Diakritikos"
        self.converters: dict[str, TextConverter] = {
            "Polytonic Greek": greek_polytonic.greek_converter,
            "Latin": latin.latin_converter
        }
        self.selected_converter: str = list(self.converters)[0]

        # A: Dropdown alphabet selector
        self.option_menu = CTkOptionMenu(
            self, values=list(self.converters), command=self.__change_converter)
        self.option_menu.grid(column=0, row=0, sticky='W')

        # B: Unconverted text input box
        self.input = CTkTextbox(self, width=self.winfo_screenwidth(
        ) / 2, height=self.winfo_screenheight() / 8)
        self.input.bind("<KeyRelease>", self.__update_text)
        self.input.configure(font=("times new roman", 26))
        self.input.grid(column=0, row=1)

        # C: Converted text output box
        self.output = CTkTextbox(self, wrap="word", width=self.winfo_screenwidth(
        ) / 2, height=self.winfo_screenheight() / 8, state="disabled")
        self.output.configure(font=("times new roman", 26))
        self.output.grid(column=0, row=3)

        # D: Input/Output divider
        self.sep = ttk.Separator(self)
        self.sep.grid(column=0, row=2, sticky="NSEW")

    def __change_converter(self, converter_name: str) -> None:
        """Change which converter to use."""
        self.selected_converter = converter_name
        self.__update_text()

    def __update_text(self, *args) -> None:
        """Replace the current text with a newly parsed conversion."""
        converter: TextConverter = self.converters[self.selected_converter]
        text: str = self.input.get("1.0", "end")
        conversion = str(converter.convert(text))
        self.output.configure(state="normal")
        self.output.delete("0.0", "end")
        self.output.insert("0.0", conversion)
        self.output.configure(state="disabled")

    def run(self) -> None:
        '''Start the app.'''
        self.mainloop()
