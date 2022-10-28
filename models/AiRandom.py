from random import choice
from string import ascii_lowercase

from models.abstract.AI import AI


class AiRandom(AI):
    """
        This Player is an AI, it plays randomly
    """
    def __init__(self, list_secret_words=None):
        super(AiRandom, self).__init__()

        self.list_letters = [letter for letter in ascii_lowercase]

    def guessing_letter(self, list_guessing_letters: list[str], regex_pattern: str) -> str:
        guessing_letter = None

        while guessing_letter is None:
            guessing_letter_choice = choice(self.list_letters)

            if guessing_letter_choice in list_guessing_letters:
                print("Veuillez choisir une lettre que vous n'avez pas déjà sélectionnée !")
                print(f"Voici un rappel des lettre que vous avez joué : {list_guessing_letters}")

            else:
                guessing_letter = guessing_letter_choice

        return guessing_letter
