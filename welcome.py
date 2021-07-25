import prompts
import config


def welcome():
    """Prints a welcome message and some ASCII art to the terminal
    """
    print(prompts.WELCOME)
    print(config.ascii_book)

welcome()
