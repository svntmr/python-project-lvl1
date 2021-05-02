"""This module is the entrypoint to run brain-even game."""
from brain_games.cli import welcome_user
from brain_games.games.even import game


def main():
    """Welcomes users in the Brain Games project and starts the game."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    game(user_name)
