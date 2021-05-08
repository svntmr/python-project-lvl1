"""This module is the entrypoint to run brain-calc game."""
from brain_games.engine import run
from brain_games.games import prime


def main():
    """Starts the game."""
    run(prime)
