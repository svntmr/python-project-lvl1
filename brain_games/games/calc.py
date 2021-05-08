"""Module describes logic of a game to guess expression result."""
from operator import add, mul, sub
from random import choice, randint

RULE = 'What is the result of the expression?'
MAX_NUMBER = 20
OPERATORS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_round_data() -> (str, str):
    """
    Returns round data.

    Generates and returns question with the right answer for the game round.

    :returns: Tuple with question and right answer
    :rtype: tuple
    """
    first_operand = randint(0, MAX_NUMBER)
    second_operand = randint(0, MAX_NUMBER)
    symbol, operation = choice(OPERATORS)
    question = '{0} {1} {2}'.format(first_operand, symbol, second_operand)
    right_answer = str(operation(first_operand, second_operand))
    return question, right_answer
