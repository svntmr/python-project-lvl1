"""Module describes logic of a game to guess numbers evenness."""

from random import randint

import prompt

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
STEPS = 3
ANSWERS = frozenset(('yes', 'no'))
MAX_NUMBER = 50


def game(user_name: str) -> None:
    """
    Executes the game logic.

    :param user_name: Name of the user who runs the game
    :type user_name: str
    :returns: Nothing
    """
    tell_rules()
    steps_counter = 0
    while steps_counter < STEPS:
        number, right_answer = get_round_data()
        ask_question(number)
        answer = get_answer()
        if answer == right_answer:
            print('Correct!')
            steps_counter += 1
        else:
            return loose(answer, right_answer, user_name)
    return congratulate(user_name)


def tell_rules() -> None:
    """Tells users game rules."""
    print(GAME_RULE)


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


def loose(answer: str, right_answer: str, user_name: str) -> None:
    """Says that user has loosed the game."""
    print(
        "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
            answer, right_answer,
        ))
    print("Let's try again, {0}!".format(user_name))


def congratulate(user_name: str) -> None:
    """Congratulates user with the win."""
    print("Congratulations, {0}!".format(user_name))
