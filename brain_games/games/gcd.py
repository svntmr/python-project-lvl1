"""Module describes logic of a game to find greatest common divider."""

from math import gcd
from random import randint

import prompt

MAX_NUMBER = 50


def get_round_data() -> (int, int, int):
    """
    Returns two random numbers and the right answer for the game round as tuple.

    :returns: Tuple with two round numbers and right answer
    :rtype: tuple
    """
    first_number = randint(0, MAX_NUMBER)
    second_number = randint(0, MAX_NUMBER)
    right_answer = gcd(first_number, second_number)
    return first_number, second_number, right_answer


def ask_question(first_number: int, second_number: int) -> None:
    """Asks user a round question."""
    print('Question: {0} {1}'.format(first_number, second_number))


def get_answer() -> str:
    """Gets user answer."""
    return prompt.integer('Your answer: ')
