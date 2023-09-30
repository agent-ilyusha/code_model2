"""Tests for first homework on greetings."""

import pytest

from hw1 import say_hello

test_greetings = (
    ('en', 'Hello'),
    ('es', 'Hola'),
    ('ru', 'Здравствуйте'),
    ('asdhasjdja', 'Hello'),
)


@pytest.mark.parametrize('lang, greeting', test_greetings)
def test_say_hello(lang: str, greeting: str) -> None:
    """Test say_hello function on test greetings with assertion.

    Args:
        lang: a given language.
        greeting: expected greeting by language.
    """
    assert say_hello(lang) == greeting
