"""Greeting in different languages."""


def say_hello(lang: str) -> str:
    """Get a greeting in a given language.

    Args:
        lang: a given language to greet in.

    Returns:
        str: a greeting by language, defaults to 'Hello'.
    """
    greetings = {
        'en': 'Hello',
        'ru': 'Здравствуйте',
        'es': 'Hola',
    }
    greeting = greetings.get(lang)
    return greeting if greeting else 'Hello'
