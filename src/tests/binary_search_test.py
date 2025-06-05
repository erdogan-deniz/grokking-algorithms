from src.module.binary_search import binary_search

int_massive = [1, 3, 5, 7, 9]
char_massive = ['a', 'b', 'c', 'd', 'e']
str_massive = "abcdef"
float_massive = [1.5, 2.6, 3.7]


def test_binary_search_int():
    assert binary_search(int_massive, 3) == 1


def test_binary_search_string():
    assert binary_search(str_massive, 'c') == 2


def test_binary_search_char():
    assert binary_search(char_massive, 'e') == 4


def test_binary_search_none():
    assert binary_search(int_massive, -1) is None
