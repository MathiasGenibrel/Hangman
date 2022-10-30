from models.abstract.Player import Player


class AI(Player):
    """
        Artificial Intelligence Player, This class init this AI with a default username ("Siri").\n
        This class is parents of different AI models present in this 'Project'.\n

        This class has a method so that the AI offers the player to guess the secret word.
    """

    def __init__(self, secret_word=None):
        # Give a name to AI
        super(AI, self).__init__("Siri")

        # Get a list of different secret_word
        self.secret_word = secret_word

    def get_secret_word(self, regex_pattern: str) -> str:
        return self.secret_word
