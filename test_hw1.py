"""Tests for first homework on greetings."""

import pytest

from hw1 import say_hello

en_default = 'Hello'
test_greetings = (
    ('en', 'Hello'),
    ('es', 'Hola'),
    ('ru', 'Здравствуйте'),
    ('asdhasjdja', 'Hello'),
    ('asdsadsad', en_default),
    ('qwewqe', en_default),
    ('ddffgsd', en_default),
    ('fghfghf', en_default),
    ('kjadllj', en_default),
)


@pytest.mark.parametrize('lang, greeting', test_greetings)
def test_say_hello(lang: str, greeting: str) -> None:
    """Test say_hello function on test greetings with assertion.

    Args:
        lang: a given language.
        greeting: expected greeting by language.
    """
    assert all((say_hello(lang), greeting))
