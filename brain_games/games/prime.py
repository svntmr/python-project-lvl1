"""Module describes logic of a game to find greatest common divider."""
from math import sqrt
from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def get_round_data() -> (str, str):
    """
    Generates and returns question with the right answer for the game round.

    :returns: Tuple with question and right answer
    :rtype: tuple
    """
    number = randint(0, MAX_NUMBER)
    right_answer = is_prime(number)
    return str(number), right_answer


def is_prime(number: int) -> str:
    """
    Function checks if the given number is prime or not.

    :param number: Number to check
    :type number: int
    :returns: yes if number is prime, otherwise returns no
    :rtype: str
    """
    if number == 2:
        return 'yes'
    if number % 2 == 0 or number <= 1:
        return 'no'

    sqr = int(sqrt(number)) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return 'no'
    return 'yes'
