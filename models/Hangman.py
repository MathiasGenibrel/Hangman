import re


class Hangman:
    def __init__(self, error_guessing_allowed: int = 8):
        # Secret word Section
        self.secret_word = None
        self.secret_word_guessing = None

        # Guessing Section
        self.error_guessing_remaining = error_guessing_allowed
        self.list_guessing_letters = []

        # Other param
        self.regex_pattern = r"[A-Za-z]+$"

    def start_game(self):
        """Public function: Used for start the Hangman Game"""

        # Init the game with the secret word
        self.__get_secret_word()

        # print(self.secret_word)
        # print(self.secret_word_guessing)

        # While the secret word or life
        while self.secret_word_guessing != self.secret_word and self.error_guessing_remaining > 0:
            print(f"Le mot à deviner : {self.secret_word_guessing}")
            print(f"Vous avez {self.error_guessing_remaining} vie(s)")

            guessing_letter = self.__guessing_letter()
            validation_guessing = self.validation_guessing(guessing_letter)

            if validation_guessing is not None:
                self.update_guessing_word(validation_guessing)

        if self.secret_word_guessing == self.secret_word:
            print(f"Felicitation vous avez gagné, le mot à deviner était bien \"{self.secret_word}\"")
        else:
            print("Vous avez perdu #HANG-MAN")

    def validation_guessing(self, guessing_letter):
        all_secret_letter = [
            (index, letter)
            for index, letter in enumerate(self.secret_word)
            if letter == guessing_letter
        ]

        if len(all_secret_letter) > 0:
            return all_secret_letter

        self.error_guessing_remaining -= 1

    def update_guessing_word(self, letter_to_display):
        list_letter = [letter for letter in self.secret_word_guessing]
        for index, letter in letter_to_display:
            list_letter.pop(index)
            list_letter.insert(index, letter)

        self.secret_word_guessing = "".join(list_letter)

    # TODO: Move in another class
    def __get_secret_word(self) -> None:
        """Set the secret word for the current game"""

        while not self.secret_word:
            secret_word = str(input("Votre mot secret : "))

            if len(secret_word) < 5:
                print("Veuillez choisir un mot de plus de 4 caractères \n")
            elif len(secret_word) > 25:
                print("Veuillez choisir un mot de moins de 25 caractères \n")
            elif re.match(self.regex_pattern, secret_word) is None:
                print("Veuillez ne mettre que des lettres dans votre mot \n")

            # Set the secret word in the context class
            else:
                self.secret_word = secret_word.lower()
                self.secret_word_guessing = "".join(["_" for _ in secret_word])

    # TODO: Move in another class
    def __guessing_letter(self) -> str:
        """Get the letter from the user input, and validate the input"""
        guessing_letter = None

        while not guessing_letter:
            guessing_letter_input = str(input("Choisissez une lettre : ")).lower()
            # Line break
            print("\n")

            # TODO remove this Dev mode
            if guessing_letter_input == "exit":
                self.secret_word_guessing = self.secret_word
                break

            # Validate data, control => length, pattern (regex) and if the letter has already played
            if 0 == len(guessing_letter_input) or len(guessing_letter_input) > 1:
                print("Veuillez ne choisir qu'une lettre ! [a, b, c, d, ...]")
            elif re.match(self.regex_pattern, guessing_letter_input) is None:
                print("Veuillez choisir une lettre !")
            elif guessing_letter_input in self.list_guessing_letters:
                print("Veuillez choisir une lettre que vous n'avez pas déjà sélectionnée !")
                print(f"Voici un rappel des lettre que vous avez joué : {self.list_guessing_letters}")

            # Save guessing letter in context class, and return guessing letter
            else:
                self.list_guessing_letters.append(guessing_letter_input)
                guessing_letter = guessing_letter_input

        return guessing_letter
