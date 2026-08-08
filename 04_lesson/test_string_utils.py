import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет", "Привет"),
    ("альбина", "Альбина"),
    ("а", "А")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("-", "-"),
    ("07.08.2026", "07.08.2026")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  hello world", "hello world"),
    ("python ", "python "),
    ("- привет", "- привет"),
    ("  ", ""),
    (" 1 2 3 4 5", "1 2 3 4 5")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    (" skypro", " "),
    ("  hello world", "h"),
    ("python ", "n"),
    ("- привет", "-"),
    (" 1 2 3 4 5", "1")
])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol) == True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (" skypro", "1"),
    ("  hello world", "Z")
])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol) == False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    (" skypro", " ", "skypro"),
    ("  hello world", "ll", "  heo world"),
    ("Python ", "P", "ython "),
    ("- привет", "-", " привет"),
    (" 1 2 3 4 5", "3", " 1 2  4 5")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (" skypro", "V", " skypro")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
