import prompts
import config


class Welcome():

    def welcome(self):
        """Prints a welcome message and some ASCII art to the terminal
        """
        print(prompts.WELCOME)
        print(config.ascii_book)


welcome = Welcome()
welcome.welcome()
