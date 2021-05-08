"""This module is the entrypoint to run brain-even game."""
from brain_games.engine import run
from brain_games.games import even


def main():
    """Starts the game."""
    run(even)
