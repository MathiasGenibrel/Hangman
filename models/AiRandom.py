from random import choice
from string import ascii_lowercase

from models.Player import Player

list_secret_words_default = ["vite", "yoga", "absorbez", "denaturalisassions"]


class AiRandom(Player):
    def __init__(self, list_secret_words=None):
        super(AiRandom, self).__init__("Siri")

        self.list_secret_words = list_secret_words if list_secret_words is None else list_secret_words_default
        self.list_letters = [letter for letter in ascii_lowercase]

    def get_secret_word(self, regex_pattern: str) -> str:
        secret_word = choice(self.list_secret_words)

        return secret_word

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
