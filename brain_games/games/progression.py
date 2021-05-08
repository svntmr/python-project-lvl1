"""Module describes logic of a game to find greatest common divider."""
from random import randint

RULE = 'What number is missing in the progression?'
MIN_PROGRESSION_STEPS = 5
MAX_PROGRESSION_STEPS = 10
MAX_START_NUMBER = 10
MAX_STEP_SIZE = 20


def get_round_data() -> (str, str):
    """
    Generates and returns question with the right answer for the game round.

    :returns: Tuple with question and right answer
    :rtype: tuple
    """
    progression_start = randint(0, MAX_START_NUMBER)
    progression_step = randint(1, MAX_STEP_SIZE)
    progression_size = randint(MIN_PROGRESSION_STEPS, MAX_PROGRESSION_STEPS)
    progression = range(
        progression_start,
        progression_start + progression_step * progression_size,
        progression_step,
    )
    progression = list(map(str, progression))
    question_item_index = randint(0, len(progression) - 1)
    right_answer = str(progression[question_item_index])
    progression[question_item_index] = '..'
    question = ' '.join(progression)
    return question, right_answer
