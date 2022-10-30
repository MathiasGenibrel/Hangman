from random import choice
from string import ascii_lowercase

from models.abstract.AI import AI


class AiRandom(AI):
    """
        This Player is an AI, it plays randomly
    """

    def __init__(self, secret_word=None):
        super(AiRandom, self).__init__()

        self.list_letters = [letter for letter in ascii_lowercase]

    def guessing_letter(self, list_guessing_letters: list[str], regex_pattern: str, secret_word_guessing=None) -> str:
        guessing_letter = None

        while guessing_letter is None:
            guessing_letter_choice = choice(self.list_letters)

            if guessing_letter_choice not in list_guessing_letters:
                guessing_letter = guessing_letter_choice

        return guessing_letter
