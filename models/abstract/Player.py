class Player:
    """
        This class is abstract, **do not instantiate it**.\n
        It allows to implement methods common to all its children.
    """

    def __init__(self, username):
        self.username = username

    @staticmethod
    def get_secret_word(regex_pattern: str) -> str:
        """
        Getting secret word from Human or AI.

        :param str regex_pattern: Pattern to check if the user inputs are good or not
        :return: Secret word selected by the Player (Human | AI)
        """
        pass

    @staticmethod
    def guessing_letter(list_guessing_letters: list[str], regex_pattern: str) -> str:
        """
        Getting a letter from Human or AI.

        :param list[str] list_guessing_letters: List of all letters already played by the player
        :param str regex_pattern: Pattern to check if the user inputs are good or not
        :return: Letter selected by Player (Human | AI)
        """
        pass
