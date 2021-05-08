"""This module is the entrypoint to run brain-gcd game."""
from brain_games.engine import run
from brain_games.games import gcd


def main():
    """Starts the game."""
    run(gcd)
