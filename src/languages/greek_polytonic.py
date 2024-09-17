from src.bases.converter import CombinationConverter


greek_converter = CombinationConverter(
    {
        "α": ("a", ()),
        "ἀ": ("a", (")",)),
        "ἁ": ("a", ("(",)),
        "ἂ": ("a", (")", "\\")),
        "ἃ": ("a", ("(", "\\")),
        "ἄ": ("a", (")", "/")),
        "ἅ": ("a", ("(", "/")),
        "ἆ": ("a", (")", "=")),
        "ἇ": ("a", ("(", "=")),
        "Α": ("A", ()),
        "Ἀ": ("A", (")",)),
        "Ἁ": ("A", ("(",)),
        "Ἂ": ("A", (")", "\\")),
        "Ἃ": ("A", ("(", "\\")),
        "Ἄ": ("A", (")", "/")),
        "Ἅ": ("A", ("(", "/")),
        "Ἆ": ("A", (")", "=")),
        "Ἇ": ("A", ("(", "=")),

        "ε": ("e", ()),
        "ἐ": ("e", (")",)),
        "ἑ": ("e", ("(",)),
        "ἒ": ("e", (")", "\\")),
        "ἓ": ("e", ("(", "\\")),
        "ἔ": ("e", (")", "/")),
        "ἕ": ("e", ("(", "/")),
        "Ε": ("E", ()),
        "Ἐ": ("E", (")",)),
        "Ἑ": ("E", ("(",)),
        "Ἒ": ("E", (")", "\\")),
        "Ἓ": ("E", ("(", "\\")),
        "Ἔ": ("E", (")", "/")),
        "Ἕ": ("E", ("(", "/")),

        "η": ("h", ()),
        "ἠ": ("h", (")",)),
        "ἡ": ("h", ("(",)),
        "ἢ": ("h", (")", "\\")),
        "ἣ": ("h", ("(", "\\")),
        "ἤ": ("h", (")", "/")),
        "ἥ": ("h", ("(", "/")),
        "ἦ": ("h", (")", "=")),
        "ἧ": ("h", ("(", "=")),
        "Ἠ": ("H", ()),
        "Ἡ": ("H", (")",)),
        "Ἢ": ("H", ("(",)),
        "Ἣ": ("H", (")", "\\")),
        "Ἤ": ("H", ("(", "\\")),
        "Ἥ": ("H", (")", "/")),
        "Ἦ": ("H", ("(", "/")),
        "Ἧ": ("H", (")", "=")),
        "Η": ("H", ("(", "=")),

        "ι": ("i", ()),
        "ἰ": ("i", (")",)),
        "ἱ": ("i", ("(",)),
        "ἲ": ("i", (")", "\\")),
        "ἳ": ("i", ("(", "\\")),
        "ἴ": ("i", (")", "/")),
        "ἵ": ("i", ("(", "/")),
        "ἶ": ("i", (")", "=")),
        "ἷ": ("i", ("(", "=")),
        "Ι": ("I", ()),
        "Ἰ": ("I", (")",)),
        "Ἱ": ("I", ("(",)),
        "Ἲ": ("I", (")", "\\")),
        "Ἳ": ("I", ("(", "\\")),
        "Ἴ": ("I", (")", "/")),
        "Ἵ": ("I", ("(", "/")),
        "Ἶ": ("I", (")", "=")),
        "Ἷ": ("I", ("(", "=")),

        "ο": ("o", ()),
        "ὀ": ("o", (")",)),
        "ὁ": ("o", ("(",)),
        "ὂ": ("o", (")", "\\")),
        "ὃ": ("o", ("(", "\\")),
        "ὄ": ("o", (")", "/")),
        "ὅ": ("o", ("(", "/")),
        "Ο": ("O", ()),
        "Ὀ": ("O", (")",)),
        "Ὁ": ("O", ("(",)),
        "Ὂ": ("O", (")", "\\")),
        "Ὃ": ("O", ("(", "\\")),
        "Ὄ": ("O", (")", "/")),
        "Ὅ": ("O", ("(", "/")),

        "υ": ("u", ()),
        "ὐ": ("u", (")",)),
        "ὑ": ("u", ("(",)),
        "ὒ": ("u", (")", "\\")),
        "ὓ": ("u", ("(", "\\")),
        "ὔ": ("u", (")", "/")),
        "ὕ": ("u", ("(", "/")),
        "ὖ": ("u", (")", "=")),
        "ὗ": ("u", ("(", "=")),
        "Υ": ("U", ()),
        "Ὑ": ("u", ("(",)),
        "Ὓ": ("u", ("(", "\\")),
        "Ὕ": ("u", ("(", "/")),
        "Ὗ": ("u", ("(", "=")),

        "ω": ("w", ()),
        "ὠ": ("w", (")",)),
        "ὡ": ("w", ("(",)),
        "ὢ": ("w", (")", "\\")),
        "ὣ": ("w", ("(", "\\")),
        "ὤ": ("w", (")", "/")),
        "ὥ": ("w", ("(", "/")),
        "ὦ": ("w", (")", "=")),
        "ὧ": ("w", ("(", "=")),
        "Ω": ("W", ()),
        "Ὠ": ("W", (")",)),
        "Ὡ": ("W", ("(",)),
        "Ὢ": ("W", (")", "\\")),
        "Ὣ": ("W", ("(", "\\")),
        "Ὤ": ("W", (")", "/")),
        "Ὥ": ("W", ("(", "/")),
        "Ὦ": ("W", (")", "=")),
        "Ὧ": ("W", ("(", "=")),

        "ὰ": ("a", ("\\",)),
        "ά": ("a", ("/",)),
        "ὲ": ("e", ("\\",)),
        "έ": ("e", ("/",)),
        "ὴ": ("h", ("\\",)),
        "ή": ("h", ("/",)),
        "ὶ": ("i", ("\\",)),
        "ί": ("i", ("/",)),
        "ὸ": ("o", ("\\",)),
        "ό": ("o", ("/",)),
        "ὺ": ("u", ("\\",)),
        "ύ": ("u", ("/",)),
        "ὼ": ("w", ("\\",)),
        "ώ": ("w", ("/",)),

        "ᾀ": ("a", ("|", ")")),
        "ᾁ": ("a", ("|", "(")),
        "ᾂ": ("a", ("|", ")", "\\")),
        "ᾃ": ("a", ("|", "(", "\\")),
        "ᾄ": ("a", ("|", ")", "/")),
        "ᾅ": ("a", ("|", "(", "/")),
        "ᾆ": ("a", ("|", ")", "=")),
        "ᾇ": ("a", ("|", "(", "=")),
        "ᾈ": ("A", ("|", "(")),
        "ᾉ": ("A", ("|", ")")),
        "ᾊ": ("A", ("|", ")", "\\")),
        "ᾋ": ("A", ("|", "(", "\\")),
        "ᾌ": ("A", ("|", ")", "/")),
        "ᾍ": ("A", ("|", "(", "/")),
        "ᾎ": ("A", ("|", ")", "=")),
        "ᾏ": ("A", ("|", "(", "=")),

        "ᾐ": ("h", ("|", ")")),
        "ᾑ": ("h", ("|", "(")),
        "ᾒ": ("h", ("|", ")", "\\")),
        "ᾓ": ("h", ("|", "(", "\\")),
        "ᾔ": ("h", ("|", ")", "/")),
        "ᾕ": ("h", ("|", "(", "/")),
        "ᾖ": ("h", ("|", ")", "=")),
        "ᾗ": ("h", ("|", "(", "=")),
        "ᾘ": ("H", ("|", "(")),
        "ᾙ": ("H", ("|", ")")),
        "ᾚ": ("H", ("|", ")", "\\")),
        "ᾛ": ("H", ("|", "(", "\\")),
        "ᾜ": ("H", ("|", ")", "/")),
        "ᾝ": ("H", ("|", "(", "/")),
        "ᾞ": ("H", ("|", ")", "=")),
        "ᾟ": ("H", ("|", "(", "=")),

        "ᾠ": ("w", ("|", ")")),
        "ᾡ": ("w", ("|", "(")),
        "ᾢ": ("w", ("|", ")", "\\")),
        "ᾣ": ("w", ("|", "(", "\\")),
        "ᾤ": ("w", ("|", ")", "/")),
        "ᾥ": ("w", ("|", "(", "/")),
        "ᾦ": ("w", ("|", ")", "=")),
        "ᾧ": ("w", ("|", "(", "=")),
        "ᾨ": ("W", ("|", ")")),
        "ᾩ": ("W", ("|", "(")),
        "ᾪ": ("W", ("|", ")", "\\")),
        "ᾫ": ("W", ("|", "(", "\\")),
        "ᾬ": ("W", ("|", ")", "/")),
        "ᾭ": ("W", ("|", "(", "/")),
        "ᾮ": ("W", ("|", ")", "=")),
        "ᾯ": ("W", ("|", "(", "=")),

        "ᾰ": ("a", ("-",)),
        "ᾱ": ("a", ("_",)),
        "ᾲ": ("a", ("\\", "|")),
        "ᾳ": ("a", ("|",)),
        "ᾴ": ("a", ("/", "|")),
        "ᾶ": ("a", ("=",)),
        "ᾷ": ("a", ("=", "|")),
        "Ᾰ": ("A", ("-",)),
        "Ᾱ": ("A", ("_",)),
        "Ὰ": ("A", ("\\",)),
        "Ά": ("A", ("/",)),
        "ᾼ": ("A", ("|",)),

        "ῂ": ("h", ("|", "\\")),
        "ῃ": ("h", ("|",)),
        "ῄ": ("h", ("|", "/")),
        "ῆ": ("h", ("=",)),
        "ῇ": ("h", ("|", "=")),

        "Ὲ": ("E", ("\\",)),
        "Έ": ("E", ("/",)),

        "Ὴ": ("H", ("\\",)),
        "Ή": ("H", ("/",)),
        "ῌ": ("H", ("|",)),

        "ῐ": ("i", ("-",)),
        "ῑ": ("i", ("_",)),
        "ῒ": ("i", ("\\", "+")),
        "ΐ": ("i", ("/", "+")),
        "ῖ": ("i", ("=",)),
        "ῗ": ("i", ("=", "+")),
        "Ῐ": ("I", ("-",)),
        "Ῑ": ("I", ("_",)),
        "Ὶ": ("I", ("\\",)),
        "Ί": ("I", ("/",)),

        "ῤ": ("r", (")",)),
        "ῥ": ("r", ("(",)),
        "Ῥ": ("R", ("(",)),

        "ῠ": ("u", ("-",)),
        "ῡ": ("u", ("_",)),
        "ῢ": ("u", ("\\", "+")),
        "ΰ": ("u", ("/", "+")),
        "ῦ": ("u", ("=",)),
        "ῧ": ("u", ("=", "+")),

        "Ῠ": ("U", ("-",)),
        "Ῡ": ("U", ("_",)),
        "Ὺ": ("U", ("\\",)),
        "Ύ": ("U", ("/",)),

        "Ὸ": ("O", ("\\",)),
        "Ό": ("O", ("/",)),

        "ῲ": ("w", ("|", "\\")),
        "ῳ": ("w", ("|", )),
        "ῴ": ("w", ("|", "/")),
        "ῶ": ("w", ("=", )),
        "ῷ": ("w", ("|", "=")),
        "Ὼ": ("W", ("\\", )),
        "Ώ": ("W", ("/", )),
        "ῼ": ("W", ("|", )),

        "Ϊ": ("I", ("+",)),
        "Ϋ": ("Y", ("+",)),
        "ϊ": ("i", ("+",)),
        "ϋ": ("u", ("+",)),

        "Β": ("B", ()),
        "Γ": ("G", ()),
        "Δ": ("D", ()),
        "Ζ": ("Z", ()),
        "Θ": ("Q", ()),
        "Κ": ("K", ()),
        "Λ": ("L", ()),
        "Μ": ("M", ()),
        "Ν": ("N", ()),
        "Ξ": ("C", ()),
        "Π": ("P", ()),
        "Ρ": ("R", ()),
        "Σ": ("S", ()),
        "Τ": ("T", ()),
        "Φ": ("F", ()),
        "Χ": ("X", ()),
        "Ψ": ("Y", ()),
        "β": ("b", ()),
        "γ": ("g", ()),
        "δ": ("d", ()),
        "ζ": ("z", ()),
        "θ": ("q", ()),
        "κ": ("k", ()),
        "λ": ("l", ()),
        "μ": ("m", ()),
        "ν": ("n", ()),
        "ξ": ("c", ()),
        "π": ("p", ()),
        "ρ": ("r", ()),
        "σ": ("s", ()),
        "τ": ("t", ()),
        "φ": ("f", ()),
        "χ": ("x", ()),
        "ψ": ("y", ()),

        "ς ": ("s", (" ",)),
        "ς\n": ("s", ("\n",)),
        "ς.": ("s", (".",)),
        "ς,": ("s", (",",)),
    
        "Ϝ": ("V", ()),
        "ϝ": ("v", ()),
    }
)

