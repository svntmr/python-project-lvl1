"""Module describes logic of a game to find greatest common divider."""
from math import gcd
from random import randint

RULE = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 50


def get_round_data() -> (str, str):
    """
    Generates and returns question with the right answer for the game round.

    :returns: Tuple with question and right answer
    :rtype: tuple
    """
    first_number = randint(0, MAX_NUMBER)
    second_number = randint(0, MAX_NUMBER)
    question = '{0} {1}'.format(first_number, second_number)
    right_answer = str(gcd(first_number, second_number))
    return question, right_answer
