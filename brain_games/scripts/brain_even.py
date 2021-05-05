"""This module is the entrypoint to run brain-even game."""
from brain_games.cli import (
    congratulate,
    loose,
    tell_rules,
    welcome_and_acknowledge_user,
)
from brain_games.games.even import ask_question, get_answer, get_round_data

GAME_STEPS = 3
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    """Starts the game."""
    user_name = welcome_and_acknowledge_user()
    tell_rules(GAME_RULE)
    steps_counter = 0
    while steps_counter < GAME_STEPS:
        number, right_answer = get_round_data()
        ask_question(number)
        answer = get_answer()
        if answer == right_answer:
            print('Correct!')
            steps_counter += 1
        else:
            return loose(answer, right_answer, user_name)
    return congratulate(user_name)
