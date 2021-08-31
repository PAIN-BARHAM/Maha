from datetime import datetime

from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE

import maha.parsers.rules.numeral.values as numvalues
from maha.constants import ARABIC_COMMA, COMMA
from maha.expressions import EXPRESSION_SPACE, EXPRESSION_SPACE_OR_NONE
from maha.parsers.rules.duration.values import (
    ONE_DAY,
    ONE_MONTH,
    SEVERAL_DAYS,
    SEVERAL_MONTHS,
    TWO_DAYS,
    TWO_MONTHS,
)
from maha.parsers.rules.numeral.rule import (
    RULE_NUMERAL,
    RULE_NUMERAL_INTEGERS,
    RULE_NUMERAL_ONES,
    RULE_NUMERAL_TENS,
)
from maha.parsers.rules.numeral.values import TEH_OPTIONAL_SUFFIX
from maha.parsers.rules.ordinal.rule import RULE_ORDINAL_ONES, RULE_ORDINAL_TENS
from maha.parsers.rules.ordinal.values import ALEF_LAM, ALEF_LAM_OPTIONAL
from maha.parsers.templates import FunctionValue, Value
from maha.parsers.templates.value_expressions import MatchedValue
from maha.rexy import (
    Expression,
    ExpressionGroup,
    named_group,
    non_capturing_group,
    optional_non_capturing_group,
)

from ..common import ALL_ALEF, spaced_patterns
from .template import TimeValue


def value_group(value):
    return named_group("value", value)


def parse_value(value: dict) -> TimeValue:
    return TimeValue(**value)


TIME_WORD_SEPARATOR = Expression(
    non_capturing_group(
        f"{EXPRESSION_SPACE_OR_NONE}{non_capturing_group(COMMA, ARABIC_COMMA)}",
        str(EXPRESSION_SPACE),
    )
    + non_capturing_group(r"\b", str(EXPRESSION_SPACE_OR_NONE))
)

THIS = non_capturing_group("ها?ذ[ياه]", "ه[اذ]ي")
AFTER = non_capturing_group("[إا]لل?ي" + EXPRESSION_SPACE) + f"?" + "بعد"
BEFORE = optional_non_capturing_group("[إا]لل?ي" + EXPRESSION_SPACE) + "[أاق]بل"
PREVIOUS = non_capturing_group("الماضي?", "السابق", "المنصرم", "الفا[يئ]ت")
NEXT = (
    non_capturing_group("الجاي", "القادم", "التالي?", "ال[اآ]تي?", "المقبل")
    + TEH_OPTIONAL_SUFFIX
)
AFTER_NEXT = spaced_patterns(AFTER, NEXT)
BEFORE_PREVIOUS = spaced_patterns(BEFORE, PREVIOUS)
IN_FROM_AT = non_capturing_group("في", "من", "خلال", "الموافق")
IN_FROM_AT_THIS = spaced_patterns(IN_FROM_AT + "?", THIS)

# region this time
AT_THE_MOMENT = Value(
    TimeValue(years=0, months=0, days=0, hours=0, minutes=0, seconds=0),
    non_capturing_group(
        "ال[أآا]ن",
        THIS
        + non_capturing_group(
            "الوقت",
            "اللح[زضظ][ةه]",
        ),
        "هس[ةه]",
        "في الحال",
    ),
)
# endregion

# region DAYS
# ----------------------------------------------------
# DAYS
# ----------------------------------------------------
SUNDAY = Value(SU, "ال[أا]حد")
MONDAY = Value(MO, "ال[إا][تث]نين")
TUESDAY = Value(TU, "ال[ثت]لا[ثت]اء")
WEDNESDAY = Value(WE, "ال[أا]ربعاء")
THURSDAY = Value(TH, "الخميس")
FRIDAY = Value(FR, "الجمع[ةه]")
SATURDAY = Value(SA, "السبت")
_days = ExpressionGroup(SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY)

WEEKDAY = FunctionValue(
    lambda match: TimeValue(
        weekday=_days.get_matched_expression(match.group("value")).value  # type: ignore
    ),
    non_capturing_group(
        spaced_patterns("يوم", named_group("value", _days.join())),
        named_group("value", _days.join()),
    ),
)
THIS_DAY = Value(
    TimeValue(days=0),
    non_capturing_group("اليوم", spaced_patterns(IN_FROM_AT_THIS, "اليوم")),
)
YESTERDAY = Value(
    TimeValue(days=-1),
    non_capturing_group(
        "[اإ]?مبارح",
        ALEF_LAM + "بارح[ةه]",
        ALEF_LAM_OPTIONAL + "[أا]مس",
        spaced_patterns(BEFORE, ONE_DAY),
        spaced_patterns(ALEF_LAM + ONE_DAY, PREVIOUS),
    ),
)
BEFORE_YESTERDAY = Value(
    TimeValue(days=-2),
    non_capturing_group(
        spaced_patterns(non_capturing_group("[أا]ول", str(BEFORE)), YESTERDAY),
        spaced_patterns(ALEF_LAM + ONE_DAY, BEFORE_PREVIOUS),
        spaced_patterns(BEFORE, TWO_DAYS),
    ),
)
TOMORROW = Value(
    TimeValue(days=1),
    non_capturing_group(
        ALEF_LAM_OPTIONAL + "غدا?",
        "بكر[ةه]",
        spaced_patterns(ALEF_LAM + ONE_DAY, NEXT),
        spaced_patterns(AFTER, ONE_DAY),
    ),
)
AFTER_TOMORROW = Value(
    TimeValue(days=2),
    non_capturing_group(
        spaced_patterns(ALEF_LAM + ONE_DAY, AFTER_NEXT),
        spaced_patterns(AFTER, TOMORROW),
        spaced_patterns(AFTER, TWO_DAYS),
    ),
)

AFTER_N_DAYS = FunctionValue(
    lambda match: parse_value({"days": list(RULE_NUMERAL(match.group("value")))[0]}),
    spaced_patterns(AFTER, value_group(RULE_NUMERAL), SEVERAL_DAYS),
)
BEFORE_N_DAYS = FunctionValue(
    lambda match: parse_value({"days": list(RULE_NUMERAL(match.group("value")))[0]}),
    spaced_patterns(BEFORE, value_group(RULE_NUMERAL), SEVERAL_DAYS),
)
NEXT_WEEKDAY = FunctionValue(
    lambda match: parse_value(
        {"weekday": _days.get_matched_expression(match.group("value")).value(1)}  # type: ignore
    ),
    non_capturing_group(
        spaced_patterns("يوم", value_group(_days.join()), NEXT),
        spaced_patterns(value_group(_days.join()), NEXT),
    ),
)
PREVIOUS_WEEKDAY = FunctionValue(
    lambda match: parse_value(
        {"weekday": _days.get_matched_expression(match.group("value")).value(-1)}  # type: ignore
    ),
    non_capturing_group(
        spaced_patterns("يوم", value_group(_days.join()), PREVIOUS),
        spaced_patterns(value_group(_days.join()), PREVIOUS),
    ),
)
AFTER_NEXT_WEEKDAY = FunctionValue(
    lambda match: parse_value(
        {"weekday": _days.get_matched_expression(match.group("value")).value(2)}  # type: ignore
    ),
    non_capturing_group(
        spaced_patterns("يوم", value_group(_days.join()), AFTER_NEXT),
        spaced_patterns(value_group(_days.join()), AFTER_NEXT),
    ),
)
BEFORE_PREVIOUS_WEEKDAY = FunctionValue(
    lambda match: parse_value(
        {"weekday": _days.get_matched_expression(match.group("value")).value(-2)}  # type: ignore
    ),
    non_capturing_group(
        spaced_patterns("يوم", value_group(_days.join()), BEFORE_PREVIOUS),
        spaced_patterns(value_group(_days.join()), BEFORE_PREVIOUS),
    ),
)
# endregion

# region MONTHS
# -----------------------------------------------------------
# MONTHS
# -----------------------------------------------------------
JANUARY = Value(TimeValue(month=1), non_capturing_group("يناير", "كانون الثاني"))
FEBRUARY = Value(TimeValue(month=2), non_capturing_group("فبراير", "شباط"))
MARCH = Value(TimeValue(month=3), non_capturing_group("مارس", "[اأآ]ذار"))
APRIL = Value(TimeValue(month=4), non_capturing_group("نيسان", f"{ALL_ALEF}بريل"))
MAY = Value(TimeValue(month=5), non_capturing_group("مايو", "أيار"))
JUNE = Value(TimeValue(month=6), non_capturing_group("يونيو", "حزيران"))
JULY = Value(TimeValue(month=7), non_capturing_group("يوليو", "تموز"))
AUGUST = Value(TimeValue(month=8), non_capturing_group("[اأآ]غسطس", "[أاآ]ب"))
SEPTEMBER = Value(TimeValue(month=9), non_capturing_group("سبتمبر", "[اأ]يلول"))
OCTOBER = Value(TimeValue(month=10), non_capturing_group("[اأ]كتوبر", "تشرين الأول"))
NOVEMBER = Value(TimeValue(month=11), non_capturing_group("نوفمبر", "تشرين الثاني"))
DECEMBER = Value(TimeValue(month=12), non_capturing_group("ديسمبر", "كانون الأول"))

JANUARY_IN_NUMBERS = Value(TimeValue(month=1), spaced_patterns("شهر", numvalues.ONE))
FEBRUARY_IN_NUMBERS = Value(TimeValue(month=2), spaced_patterns("شهر", numvalues.TWO))
MARCH_IN_NUMBERS = Value(TimeValue(month=3), spaced_patterns("شهر", numvalues.THREE))
APRIL_IN_NUMBERS = Value(TimeValue(month=4), spaced_patterns("شهر", numvalues.FOUR))
MAY_IN_NUMBERS = Value(TimeValue(month=5), spaced_patterns("شهر", numvalues.FIVE))
JUNE_IN_NUMBERS = Value(TimeValue(month=6), spaced_patterns("شهر", numvalues.SIX))
JULY_IN_NUMBERS = Value(TimeValue(month=7), spaced_patterns("شهر", numvalues.SEVEN))
AUGUST_IN_NUMBERS = Value(TimeValue(month=8), spaced_patterns("شهر", numvalues.EIGHT))
SEPTEMBER_IN_NUMBERS = Value(TimeValue(month=9), spaced_patterns("شهر", numvalues.NINE))
OCTOBER_IN_NUMBERS = Value(TimeValue(month=10), spaced_patterns("شهر", numvalues.TEN))
NOVEMBER_IN_NUMBERS = Value(
    TimeValue(month=11), spaced_patterns("شهر", numvalues.ELEVEN)
)
DECEMBER_IN_NUMBERS = Value(
    TimeValue(month=12), spaced_patterns("شهر", numvalues.TWELVE)
)


_months_text = ExpressionGroup(
    JANUARY,
    FEBRUARY,
    MARCH,
    APRIL,
    MAY,
    JUNE,
    JULY,
    AUGUST,
    SEPTEMBER,
    OCTOBER,
    NOVEMBER,
    DECEMBER,
)

_months_number = ExpressionGroup(
    JANUARY_IN_NUMBERS,
    FEBRUARY_IN_NUMBERS,
    MARCH_IN_NUMBERS,
    APRIL_IN_NUMBERS,
    MAY_IN_NUMBERS,
    JUNE_IN_NUMBERS,
    JULY_IN_NUMBERS,
    AUGUST_IN_NUMBERS,
    SEPTEMBER_IN_NUMBERS,
    OCTOBER_IN_NUMBERS,
    NOVEMBER_IN_NUMBERS,
    DECEMBER_IN_NUMBERS,
)

_months = ExpressionGroup(_months_text, _months_number)

THIS_MONTH = Value(
    TimeValue(months=0),
    non_capturing_group("الشهر", spaced_patterns(IN_FROM_AT_THIS, "الشهر")),
)
LAST_MONTH = Value(
    TimeValue(months=-1),
    non_capturing_group(
        spaced_patterns(BEFORE, ONE_MONTH),
        spaced_patterns(ALEF_LAM + ONE_MONTH, PREVIOUS),
    ),
)
LAST_TWO_MONTHS = Value(
    TimeValue(months=-2),
    non_capturing_group(
        spaced_patterns(ALEF_LAM + ONE_MONTH, BEFORE_PREVIOUS),
        spaced_patterns(BEFORE, TWO_MONTHS),
    ),
)
NEXT_MONTH = Value(
    TimeValue(months=1),
    non_capturing_group(
        spaced_patterns(ALEF_LAM + ONE_MONTH, NEXT),
        spaced_patterns(AFTER, ONE_MONTH),
    ),
)
NEXT_TWO_MONTHS = Value(
    TimeValue(months=2),
    non_capturing_group(
        spaced_patterns(ALEF_LAM + ONE_MONTH, AFTER_NEXT),
        spaced_patterns(AFTER, TWO_MONTHS),
    ),
)

AFTER_N_MONTHS = FunctionValue(
    lambda match: parse_value({"months": list(RULE_NUMERAL(match.group("value")))[0]}),
    spaced_patterns(AFTER, value_group(RULE_NUMERAL), SEVERAL_MONTHS),
)
BEFORE_N_MONTHS = FunctionValue(
    lambda match: parse_value({"months": list(RULE_NUMERAL(match.group("value")))[0]}),
    spaced_patterns(BEFORE, value_group(RULE_NUMERAL), SEVERAL_MONTHS),
)


def specific_month(match, next_month=False, years=0):
    month = _months.get_matched_expression(match.group("value")).value.month  # type: ignore
    current_month = datetime.now().month
    if next_month:
        years += 1 if month <= current_month else 0
    else:
        years += 0 if month <= current_month else -1
    return parse_value(
        {
            "month": month,
            "years": years,
        }
    )


SPECIFIC_MONTH = MatchedValue(_months, _months.join())
NEXT_SPECIFIC_MONTH = FunctionValue(
    lambda match: specific_month(match, next_month=True),
    non_capturing_group(
        spaced_patterns("شهر", value_group(_months.join()), NEXT),
        spaced_patterns(value_group(_months.join()), NEXT),
    ),
)
PREVIOUS_SPECIFIC_MONTH = FunctionValue(
    lambda match: specific_month(match, next_month=False),
    non_capturing_group(
        spaced_patterns("شهر", value_group(_months.join()), PREVIOUS),
        spaced_patterns(value_group(_months.join()), PREVIOUS),
    ),
)
AFTER_NEXT_MONTH = FunctionValue(
    lambda match: specific_month(match, next_month=True, years=1),
    non_capturing_group(
        spaced_patterns("شهر", value_group(_months.join()), AFTER_NEXT),
        spaced_patterns(value_group(_months.join()), AFTER_NEXT),
    ),
)
BEFORE_PREVIOUS_MONTH = FunctionValue(
    lambda match: specific_month(match, years=-1),
    non_capturing_group(
        spaced_patterns("شهر", value_group(_months.join()), BEFORE_PREVIOUS),
        spaced_patterns(value_group(_months.join()), BEFORE_PREVIOUS),
    ),
)
# endregion


# region DAY WITH MONTH
# ----------------------------------------------------
# DAY WITH MONTH
# ----------------------------------------------------
ordinal_ones_tens = ExpressionGroup(RULE_ORDINAL_TENS, RULE_ORDINAL_ONES)
numeral_ones_tens = ExpressionGroup(
    RULE_NUMERAL_TENS, RULE_NUMERAL_ONES, RULE_NUMERAL_INTEGERS
)

_optional_middle = optional_non_capturing_group(
    IN_FROM_AT + EXPRESSION_SPACE
) + optional_non_capturing_group("شهر" + EXPRESSION_SPACE)

_optional_start = (
    optional_non_capturing_group("يوم" + EXPRESSION_SPACE)
    + optional_non_capturing_group("اليوم" + EXPRESSION_SPACE)
    + optional_non_capturing_group(_days.join() + EXPRESSION_SPACE)
    + optional_non_capturing_group(IN_FROM_AT + EXPRESSION_SPACE)
)
ORDINAL_AND_SPECIFIC_MONTH = FunctionValue(
    lambda match: parse_value(
        {
            "month": _months.get_matched_expression(match.group("value")).value.month,  # type: ignore
            "day": (list(ordinal_ones_tens.parse(match.group("ordinal")))[0].value),
        }
    ),
    spaced_patterns(
        _optional_start + named_group("ordinal", ordinal_ones_tens.join()),
        _optional_middle + value_group(_months.join()),
    ),
)
ORDINAL_AND_THIS_MONTH = FunctionValue(
    lambda match: parse_value(
        {
            "months": 0,
            "day": (list(ordinal_ones_tens.parse(match.group("ordinal")))[0].value),
        }
    ),
    spaced_patterns(
        _optional_start + named_group("ordinal", ordinal_ones_tens.join()),
        _optional_middle + THIS_MONTH,
    ),
)
NUMERAL_AND_SPECIFIC_MONTH = FunctionValue(
    lambda match: parse_value(
        {
            "month": _months.get_matched_expression(match.group("value")).value.month,  # type: ignore
            "day": (list(numeral_ones_tens.parse(match.group("numeral")))[0].value),
        }
    ),
    spaced_patterns(
        _optional_start + named_group("numeral", numeral_ones_tens.join()),
        _optional_middle + value_group(_months.join()),
    ),
)
NUMERAL_AND_THIS_MONTH = FunctionValue(
    lambda match: parse_value(
        {
            "month": 0,
            "day": (list(numeral_ones_tens.parse(match.group("numeral")))[0].value),
        }
    ),
    spaced_patterns(
        _optional_start + named_group("numeral", numeral_ones_tens.join()),
        _optional_middle + THIS_MONTH,
    ),
)
# endregion