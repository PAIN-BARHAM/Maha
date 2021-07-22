import pytest

from maha.parsers.expressions.duration import (
    EXPRESSION_DURATION,
    EXPRESSION_DURATION_DAYS,
    EXPRESSION_DURATION_HOURS,
    EXPRESSION_DURATION_MINUTES,
    EXPRESSION_DURATION_MONTHS,
    EXPRESSION_DURATION_SECONDS,
    EXPRESSION_DURATION_WEEKS,
    EXPRESSION_DURATION_YEARS,
    NAME_OF_DAY,
    NAME_OF_HOUR,
    NAME_OF_MINUTE,
    NAME_OF_MONTH,
    NAME_OF_SECOND,
    NAME_OF_WEEK,
    NAME_OF_YEAR,
)
from maha.parsers.templates.types import DurationUnit


@pytest.mark.parametrize(
    "expected, input",
    [
        (1, "دقيقة"),
        (1, "دقيقه"),
        (2, "دقيقتين"),
        (2, "ودقيقتان"),
        (4, "4 دقايق"),
        (30, "30 دقيقة"),
        (3, "3 دقائق"),
        (4.5, "4 دقائق ونص"),
        (3.25, "3 دقيقه و ربع"),
        (4.5, "4.5 دقيقة"),
        (13 + 1 / 3, "13 دقيقه وثلث"),
    ],
)
def test_parse_minutes_with_simple_values(input: str, expected: float):
    output = list(EXPRESSION_DURATION_MINUTES.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.MINUTES


@pytest.mark.parametrize(
    "expected, input",
    [
        (135, "دقيقتين وربع"),
        (140, "دقيقتان و ثلث"),
        (150, "ودقيقتين ونصف"),
        (150, "دقيقتين ونص"),
        (90, "دقيقه ونصف"),
        (75, "دقيقه وربع"),
        (80, "دقيقة وثلث"),
        (45, "دقيقة الا ربع"),
        (15, "ربع دقيقه"),
        (30, "نص دقيقه"),
        (20, "ثلث دقيقه"),
    ],
)
def test_parse_minutes_with_more_simple_values(expected: float, input: str):
    output = list(EXPRESSION_DURATION_MINUTES.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.SECONDS


@pytest.mark.parametrize(
    "expected, input",
    [
        (1, "ساعة"),
        (1, "ساعه"),
        (2, "ساعتين"),
        (2, "وساعتان"),
        (4, "4 ساعات"),
        (30, "30 ساعة"),
        (30, "30 ساعه"),
        (3, "3 ساعات"),
        (4.5, "4 ساعات ونص"),
        (3.25, "3 ساعات وربع"),
        (4.5, "4.5 ساعة"),
        (13 + 1 / 3, "13 ساعة وثلث"),
    ],
)
def test_parse_hours_with_simple_values(input: str, expected: float):
    output = list(EXPRESSION_DURATION_HOURS.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.HOURS


@pytest.mark.parametrize(
    "expected, input",
    [
        (135, "ساعتين وربع"),
        (140, "ساعتان و ثلث"),
        (150, "ساعتين ونص"),
        (150, "وساعتان ونصف"),
        (90, "ساعة ونص"),
        (75, "ساعة وربع"),
        (80, "ساعة وثلث"),
        (45, "وساعة الا ربع"),
        (15, "ربع ساعه"),
        (30, "نص ساعه"),
        (20, "ثلث ساعه"),
    ],
)
def test_parse_hours_with_more_simple_values(expected: float, input: str):
    output = list(EXPRESSION_DURATION_HOURS.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.MINUTES


@pytest.mark.parametrize(
    "expected, input",
    [
        (1, "يوم"),
        (2, "يومين"),
        (2, "ويومين"),
        (2, "يومان اثنان"),
        (4, "4 ايام"),
        (30, "30 يوم"),
        (3, "3 أيام"),
        (20, "و20 يوما"),
    ],
)
def test_parse_days_with_simple_values(input: str, expected: float):
    output = list(EXPRESSION_DURATION_DAYS.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.DAYS


@pytest.mark.parametrize(
    "expected, input",
    [
        (54, "يومين وربع"),
        (56, "يومين و ثلث"),
        (60, "يومين ونص"),
        (36, "يوم ونص"),
        (30, "يوم وربع"),
        (32, "يوم وثلث"),
        (18, "يوم الا ربع"),
        (6, "ربع يوم"),
        (12, "نص يوم"),
        (8, "ثلث يوم"),
    ],
)
def test_parse_days_with_more_simple_values(expected: float, input: str):
    output = list(EXPRESSION_DURATION_DAYS.parse(input))
    assert len(output) == 1
    output = output[0]

    assert output.value == expected
    assert output.expression.unit == DurationUnit.HOURS
