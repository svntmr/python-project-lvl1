"""Module describes logic of a game to guess numbers evenness."""
from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 50


def get_round_data() -> (str, str):
    """
    Returns question and the right answer for the game round.

    :returns: Tuple with question and right answer
    :rtype: tuple
    """
    number = randint(0, MAX_NUMBER)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), right_answer
