"""Module to run games."""
from types import ModuleType

from brain_games.cli import (
    ask_question,
    congratulate,
    get_answer,
    loose,
    tell_rules,
    welcome_and_acknowledge_user,
)

ROUNDS = 3


def run(game: ModuleType):
    """Starts the game."""
    user_name = welcome_and_acknowledge_user()
    tell_rules(game.RULE)
    for _ in range(0, ROUNDS):
        question, right_answer = game.get_round_data()
        ask_question(question)
        answer = get_answer()
        if answer == right_answer:
            print('Correct!')
        else:
            return loose(answer, right_answer, user_name)
    return congratulate(user_name)
