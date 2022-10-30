import re
from models.abstract.Player import Player


class Human(Player):
    """
    This class allow a human player to play the Hangman game
    """

    def __init__(self, username):
        super(Human, self).__init__(username)

    @staticmethod
    def get_secret_word(regex_pattern: str) -> str:
        secret_word = None

        while not secret_word:
            secret_word_input = str(input("Votre mot secret : "))

            if len(secret_word_input) < 4:
                print("Veuillez choisir un mot de plus de 4 caractères \n")
            elif len(secret_word_input) > 12:
                print("Veuillez choisir un mot de moins de 12 caractères \n")
            elif re.match(regex_pattern, secret_word_input) is None:
                print("Veuillez mettre que des lettres dans votre mot \n")
            else:
                secret_word = secret_word_input.lower()

        return secret_word

    @staticmethod
    def guessing_letter(list_guessing_letters: list[str], regex_pattern: str, secret_word_guessing=None) -> str:
        guessing_letter = None

        while guessing_letter is None:
            guessing_letter_input = str(input("\nChoisissez une lettre : ")).lower()

            # Validate data, control => length, pattern (regex) and if the letter has already played
            if 0 == len(guessing_letter_input) or len(guessing_letter_input) > 1:
                print("Veuillez ne choisir qu'une lettre ! [a, b, c, d, ...]")
            elif re.match(regex_pattern, guessing_letter_input) is None:
                print("Veuillez choisir une lettre !")
            elif guessing_letter_input in list_guessing_letters:
                print("Veuillez choisir une lettre que vous n'avez pas déjà sélectionnée !")
                print(f"Voici un rappel des lettre que vous avez joué : {list_guessing_letters}")
            else:
                guessing_letter = guessing_letter_input

        return guessing_letter
