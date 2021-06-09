"""List of English constant definitions."""

from typing import List

from .simple import *

ENGLISH_SMALL_LETTERS: List[str] = [
    SMALL_A,
    SMALL_B,
    SMALL_C,
    SMALL_D,
    SMALL_E,
    SMALL_F,
    SMALL_G,
    SMALL_H,
    SMALL_I,
    SMALL_J,
    SMALL_K,
    SMALL_L,
    SMALL_M,
    SMALL_N,
    SMALL_O,
    SMALL_P,
    SMALL_Q,
    SMALL_R,
    SMALL_S,
    SMALL_T,
    SMALL_U,
    SMALL_V,
    SMALL_W,
    SMALL_X,
    SMALL_Y,
    SMALL_Z,
]
""" List of all small English letters"""

ENGLISH_CAPITAL_LETTERS: List[str] = [
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I,
    J,
    K,
    L,
    M,
    N,
    O,
    P,
    Q,
    R,
    S,
    T,
    U,
    V,
    W,
    X,
    Y,
    Z,
]
""" List of all capital English letters"""

ENGLISH_LETTERS: List[str] = ENGLISH_CAPITAL_LETTERS + ENGLISH_SMALL_LETTERS
""" List of all English letters"""

NUMBERS: List[str] = [
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
]
""" List of western Arabic numerals"""

PUNCTUATIONS: List[str] = [
    EXCLAMATION_MARK,
    QUOTATION_MARK,
    NUMBER_SIGN,
    HASHTAG,
    DOLLAR_SIGN,
    PERCENT_SIGN,
    AND_SIGN,
    AMPERSAND,
    APOSTROPHE,
    LEFT_PARENTHESIS,
    RIGHT_PARENTHESIS,
    ASTERISK,
    PLUS_SIGN,
    COMMA,
    MINUS_SIGN,
    HYPHEN_SIGN,
    DOT,
    FULL_STOP,
    SLASH,
    COLON,
    SEMICOLON,
    LESSTHAN_SIGN,
    EQUAL_SIGN,
    GREATERTHAN_SIGN,
    QUESTION_MARK,
    AT_SIGN,
    LEFT_BRACKET,
    BACKSLASH,
    RIGHT_BRACKET,
    EXPONENT_SIGN,
    CIRCUMFLEX_ACCENT,
    UNDERSCORE,
    LOWLINE,
    GRAVE_ACCENT,
    LEFTCURLY_BRACKET,
    VERTICAL_BAR,
    RIGHTCURLY_BRACKET,
    TILDE,
]
""" List of English punctuations"""