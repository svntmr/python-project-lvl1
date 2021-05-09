"""This module is the entrypoint to run brain-calc game."""
from brain_games.engine import run
from brain_games.games import progression


def main():
    """Starts the game."""
    run(progression)


if __name__ == '__main__':
    main()
