"""Module describes logic of a game to guess numbers evenness."""

from random import randint

import prompt

ANSWERS = frozenset(('yes', 'no'))
MAX_NUMBER = 50


def get_round_data() -> (int, str):
    """
    Returns random number and the right answer for the game round as tuple.

    :returns: Tuple with round number and right answer
    :rtype: tuple
    """
    number = randint(0, MAX_NUMBER)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return number, right_answer


def ask_question(asked_number) -> None:
    """Asks user a round question."""
    print('Question: {0}'.format(asked_number))


def get_answer() -> str:
    """Gets user answer."""
    answer = prompt.string('')
    return answer if answer in ANSWERS else ''
