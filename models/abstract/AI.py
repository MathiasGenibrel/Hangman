from random import choice

from models.abstract.Player import Player

list_secret_words_default = ["vite", "yoga", "absorbez", "denaturalisassions"]


class AI(Player):
    """
        Artificial Intelligence Player, This class init this AI with a default username ("Siri").\n
        This class is parents of different AI models present in this 'Project'.\n

        This class has a method so that the AI offers the player to guess the secret word.
    """
    def __init__(self, list_secret_words=None):
        # Give a name to AI
        super(AI, self).__init__("Siri")

        # Get a list of different secret_word
        # TODO: Change this by a method get, a word from https://www.listesdemots.net/
        self.list_secret_words = list_secret_words if list_secret_words is not None else list_secret_words_default

    def get_secret_word(self, regex_pattern: str) -> str:
        secret_word = choice(self.list_secret_words)

        return secret_word
