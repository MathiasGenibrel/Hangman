from models.Player import Player


class Hangman:
    def __init__(self, game_master: Player, guesser: Player, error_guessing_allowed: int = 8):
        # Secret word Section
        self.secret_word = None
        self.secret_word_guessing = None

        # Guessing Section
        self.error_guessing_remaining = error_guessing_allowed
        self.list_guessing_letters = []

        # init Player
        self.game_master = game_master
        self.guesser = guesser

        # Other param
        self.regex_pattern = r"[A-Za-z]+$"

    def start_game(self):
        """Public function: Used for start the Hangman Game"""

        # Init the game with the secret word
        secret_word = self.game_master.get_secret_word(regex_pattern=self.regex_pattern)

        self.secret_word = secret_word
        self.secret_word_guessing = "".join(["_" for _ in secret_word])

        # While the secret word or life
        while self.secret_word_guessing != self.secret_word and self.error_guessing_remaining > 0:
            print(f"Le mot à deviner : {self.secret_word_guessing}")
            print(f"Vous avez {self.error_guessing_remaining} vie(s)")

            guessing_letter = self.guesser.guessing_letter(regex_pattern=self.regex_pattern,
                                                           list_guessing_letters=self.list_guessing_letters)
            # Add letter to list of 'already played letter'
            self.list_guessing_letters.append(guessing_letter)

            # Verify if the letter is in the secret word
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
