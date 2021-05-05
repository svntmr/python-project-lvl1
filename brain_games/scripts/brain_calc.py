"""This module is the entrypoint to run brain-calc game."""
from brain_games.cli import (
    congratulate,
    loose,
    tell_rules,
    welcome_and_acknowledge_user,
)
from brain_games.games.calc import ask_question, get_answer, get_round_data

GAME_STEPS = 3
GAME_RULE = 'What is the result of the expression?'


def main():
    """Starts the game."""
    user_name = welcome_and_acknowledge_user()
    tell_rules(GAME_RULE)
    steps_counter = 0
    while steps_counter < GAME_STEPS:
        first_operand, operator, second_operand, right_answer = get_round_data()
        ask_question(first_operand, operator, second_operand)
        answer = get_answer()
        if answer == right_answer:
            print('Correct!')
            steps_counter += 1
        else:
            return loose(answer, right_answer, user_name)
    return congratulate(user_name)
