"""Module describes logic of a game to guess expression result."""

from random import choice, randint

import prompt

MAX_NUMBER = 20
OPERATORS = ('+', '-', '*')


def get_round_data() -> (int, str, int, int):
    """
    Returns round data.

    Generates and returns random operand, operator, second operand
    and the right answer for the game round as tuple.

    :returns: random operand, operator, second operand and the right answer
    :rtype: tuple
    """
    first_operand = randint(0, MAX_NUMBER)
    second_operand = randint(0, MAX_NUMBER)
    operator = choice(OPERATORS)
    right_answer = get_right_answer(first_operand, operator, second_operand)
    return first_operand, operator, second_operand, right_answer


def get_right_answer(
    first_operand: int,
    operator: str,
    second_operand: int,
) -> int:
    """
    Calculates given expression result.

    :param first_operand: first number
    :type first_operand: int
    :param operator: operator from expression
    :type operator: int
    :param second_operand: second number
    :type second_operand: int
    :returns: Expression result
    :rtype: int
    """
    if operator == '+':
        return first_operand + second_operand
    if operator == '-':
        return first_operand - second_operand
    return first_operand * second_operand


def ask_question(first_operand, operator, second_operand) -> None:
    """Asks user a round question."""
    print('Question: {0} {1} {2}'.format(
        first_operand, operator, second_operand,
    ))


def get_answer() -> str:
    """Gets user answer."""
    return prompt.integer('Your answer: ')
