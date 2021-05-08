"""This module contains some cli functions, e.g. a function to welcome user."""
import prompt


def welcome_and_acknowledge_user() -> str:
    """
    Welcomes users in the Brain Games project and asks their name.

    Welcomes users, asks them to write their name and welcomes them,
    returning user name.

    :returns: User name
    :rtype: str
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def tell_rules(game_rule: str) -> None:
    """
    Tells users game rules.

    :param game_rule: Rule of the current game
    :type game_rule: str
    :returns: Nothing, but prints game rules into the console
    """
    print(game_rule)


def ask_question(question: str) -> None:
    """Asks user a round question."""
    print('Question: {0}'.format(question))


def get_answer() -> str:
    """Gets user answer."""
    return prompt.string('Your answer: ')


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
