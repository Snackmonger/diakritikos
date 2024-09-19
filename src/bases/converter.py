
import itertools
from typing import TypeAlias

BaseCharacter: TypeAlias = str
DiacriticalMarks: TypeAlias = tuple[str, ...]
MarkedCharacter: TypeAlias = tuple[BaseCharacter, DiacriticalMarks]

class TextConverter():
    '''Common parent of text converters used by the program.'''


class CombinationConverter(TextConverter):
    """
    A text converter that takes the basic form of a match and then looks for
    all permutations of the base symbol + following elements.

    E.g.

        "ᾅ": ("a", ("|", "(", "/")),

        This entry would match any of a|(/ or a(|/ or a/|(, etc.

    Thereby, diacritical marks can be added to a character in any order but
    they will always map to the same precomposed symbol.
    """
    def __init__(self, conversions: dict[str, MarkedCharacter]) -> None:
        '''
        Parameters
        ----------
        conversions : dict[str, tuple[str, tuple[str, ...]]]
            The target symbol serves as a key, and the value is a tuple 
            consisting of the starting symbol and a list of diacritics.
            All diacritics must be present to match the target, but they can 
            come in any order.
            
        '''
        conversions_: dict[str, str] = {}
        for target_char, source_char in conversions.items():
            variants = self.__summarize(source_char)
            for variant in variants:
                conversions_[variant] = target_char
        self.__conversions = conversions_

    def convert(self, text: str) -> str:
        '''
        Convert a block of text according to the initialized paradigms.

        Parameters
        ----------
        text : str
            The text to be converted.

        Returns
        -------
        str
            The converted text.
        '''
        text = " " + text + " "
        conversions: list[str] = list(self.__conversions.keys())
        conversions.sort(reverse=True)
        for conversion in conversions:
            text =  text.replace(conversion, self.__conversions[conversion])
        return text.strip()


    def __summarize(self, character: MarkedCharacter) -> tuple[str, ...]:
        base_character = character[0]
        diacritical_marks = character[1]
        combinations = itertools.permutations(diacritical_marks, len(diacritical_marks))
        return tuple([base_character + "".join(c) for c in combinations])