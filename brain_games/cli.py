"""This module contains some cli functions, e.g. a function to welcome user."""
import prompt


def welcome_user() -> None:
    """Asks users to write their name then welcomes them."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
