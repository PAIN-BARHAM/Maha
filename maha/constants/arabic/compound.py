"""List of constant definitions."""

from typing import List

from .simple import *

ARABIC_CHARS: List[str] = [
    ALEF,
    BEH,
    TEH,
    THEH,
    JEEM,
    HAH,
    KHAH,
    DAL,
    THAL,
    REH,
    ZAIN,
    SEEN,
    SHEEN,
    SAD,
    DAD,
    TAH,
    ZAH,
    AIN,
    GHAIN,
    FEH,
    QAF,
    KAF,
    LAM,
    MEEM,
    NOON,
    HEH,
    WAW,
    YEH,
    ALEF_MAKSURA,
    TEH_MARBUTA,
    ALEF_MADDA_ABOVE,
    ALEF_HAMZA_ABOVE,
    ALEF_HAMZA_BELOW,
    HAMZA,
    HAMZA_WAW,
    HAMZA_YA,
    TATWEEL,
]
""" List of Arabic characters """

SIMPLE_HARAKAT: List[str] = [
    FATHA,
    DAMMA,
    KASRA,
    SUKUN,
]
""" Harakat that can be written anywhere in a word"""

TANWEN: List[str] = [
    FATHATAN,
    DAMMATAN,
    KASRATAN,
]
""" Harakat that are written at the end of a word """

HARAKAT: List[str] = [SHADDA] + SIMPLE_HARAKAT + TANWEN
""" Common Harakat """

ALEF_VARIATIONS: List[str] = [
    ALEF,
    ALEF_HAMZA_ABOVE,
    ALEF_HAMZA_BELOW,
    ALEF_MADDA_ABOVE,
    ALEF_HAMZA_ABOVE_WAVY,
    ALEF_HAMZA_BELOW_WAVY,
    ALEF_WASLA,
]
""" Variations of the letter ALEF """

LAM_ALEF_VARIATIONS: List[str] = [
    LAM_ALEF,
    LAM_ALEF_HAMZA_ABOVE,
    LAM_ALEF_HAMZA_BELOW,
    LAM_ALEF_MADDA_ABOVE,
]
""" Variations of the one-letter LAM_ALEF """

ARABIC_NUMBERS: List[str] = [
    ARABIC_ZERO,
    ARABIC_ONE,
    ARABIC_TWO,
    ARABIC_THREE,
    ARABIC_FOUR,
    ARABIC_FIVE,
    ARABIC_SIX,
    ARABIC_SEVEN,
    ARABIC_EIGHT,
    ARABIC_NINE,
]
""" Arabic numbers. """

ARABIC_PUNCTUATIONS: List[str] = [
    ARABIC_COMMA,
    ARABIC_SEMICOLON,
    ARABIC_QUESTION_MARK,
    TRIPLE_DOT,
    STAR,
    ARABIC_FULL_STOP,
    DATE_SEPARATOR,
    END_OF_AYAH,
    MISRA_SIGN,
    POETIC_VERSE_SIGN,
    SAJDAH,
    HIZB_START,
    ORNATE_LEFT_PARENTHESIS,
    ORNATE_RIGHT_PARENTHESIS,
]
""" Arabic punctuations. """

ARABIC_LIGATURES: List[str] = [
    LIGATURE_SALLA_KORANIC,
    LIGATURE_QALA,
    LIGATURE_ALLAH,
    LIGATURE_AKBAR,
    LIGATURE_MOHAMMAD,
    LIGATURE_SALAM,
    LIGATURE_RASOUL,
    LIGATURE_ALAYHE,
    LIGATURE_WASALLAM,
    LIGATURE_SALLA,
    LIGATURE_SALLALLAHOU,
    LIGATURE_JALLAJALALOUHOU,
    LIGATURE_RIAL,
    LIGATURE_BISMILLAH,
]
""" Arabic ligature. """


SMALL_HARAKAT: List[str] = [
    SMALL_TAH,
    SMALL_LAM_ALEF_YEH,
    SMALL_ZAIN,
    SMALL_FATHA,
    SMALL_DAMMA,
    SMALL_KASRA,
    SMALL_LAM_ALEF_HIGH,
    SMALL_JEEM_HIGH,
    SMALL_THREE_DOTS_HIGH,
    SMALL_MEEM_HIGH_ISOLATED,
    SMALL_MEEM_HIGH_INITIAL,
    SMALL_MEEM_LOW,
    SMALL_SEEN_LOW,
    SMALL_SEEN_HIGH,
    SMALL_ZERO_ROUNDED_HIGH,
    SMALL_ZERO_RECTANGULAR_HIGH,
    SMALL_DOTLESS_HEAD_HIGH,
    SMALL_MADDA,
    SMALL_WAW,
    SMALL_YEH_LOW,
    SMALL_YEH_HIGH,
    SMALL_NOON,
    SMALL_V,
    SMALL_V_INVERTED,
]
""" Small harakat """

OTHER_HARAKAT: List[str] = [
    SAD_SIGN,
    AIN_SIGN,
    RAHMATULLAH_SIGN,
    RADI_SIGN,
    TAKHALLUS,
    MADDAH_ABOVE,
    HAMZA_ABOVE,
    HAMZA_BELOW,
    ALEF_SUBSCRIPT,
    ALEF_SUPERSCRIPT,
    DAMMA_INVERTED,
    NOON_MARK,
    ZWARAKAY,
    DOT_BELOW,
    DAMMA_REVERSED,
    PERCENTAGE_ABOVE,
    HAMZA_BELOW_WAVY,
    LOW_STOP,
    HIGH_STOP,
    HIGH_STOP_FILLED,
]
""" Other harakat """

ALL_HARAKAT = HARAKAT + SMALL_HARAKAT + OTHER_HARAKAT
""" All harakat from the unicode block 0600–06FF """