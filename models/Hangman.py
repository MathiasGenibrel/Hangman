from models.abstract.Player import Player
from unidecode import unidecode
from models.Human import Human


class Hangman:
    """
    Create a new Hangman instance game, you need to pass as argument, 2 players.\n
    This class wait 1 Player to be Game Master (Host the game, and set the secret word), and
    1 other Player to be de Guesser (say letter by letter, to find the secret word).\n

    We initialize this class with an "error_guessing_allowed" argument with a default value to `8`,
    this argument allow the Guesser to have **n** mistake.
    """

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
        self.regex_pattern = r"[A-Za-zÀ-ÿ]+$"

    def start_game(self):
        """
        This method is used to start the Hangman Game
        :return: None
        """

        # Init the game with the secret word
        secret_word = self.game_master.get_secret_word(regex_pattern=self.regex_pattern)

        self.secret_word = secret_word
        self.secret_word_guessing = "".join(["_" for _ in secret_word])

        # While the secret word or life
        while self.secret_word_guessing != self.secret_word and self.error_guessing_remaining > 0:
            self.__print_info_player(f"Le mot à deviner : {self.secret_word_guessing}")
            self.__print_info_player(f"Vous avez {self.error_guessing_remaining} vie(s)")

            guessing_letter = self.guesser.guessing_letter(regex_pattern=self.regex_pattern,
                                                           list_guessing_letters=self.list_guessing_letters,
                                                           secret_word_guessing=self.secret_word_guessing
                                                           )
            # Add letter to list of 'already played letter'
            self.list_guessing_letters.append(guessing_letter)

            # Verify if the letter is in the secret word
            validation_guessing = self.__validation_guessing(guessing_letter)

            if validation_guessing is not None:
                self.__update_guessing_word(validation_guessing)

        if self.secret_word_guessing == self.secret_word:
            self.__print_info_player(f"Felicitation vous avez gagné, le mot à deviner était bien \"{self.secret_word}\"")
            return True
        else:
            self.__print_info_player("Vous avez perdu #HANG-MAN")
            self.__print_info_player(f"Vous avez jouez ces lettres : {self.list_guessing_letters}")
            return False

    def __validation_guessing(self, guessing_letter) -> list[tuple[int, str]] or None:
        """
        Verify if the current **guessing_letter** is on the current **secret_word**.\n
        If is not in the current secret_word, the guesser (Player who guess the secret word)
        loose 1 try.
        :param str guessing_letter: Letter selected by the Guesser
        :return: List with index and letter to change in the `secret_word_guessing` or `None`
        """
        all_secret_letter = [
            (index, letter)
            for index, letter in enumerate(self.secret_word)
            if unidecode(letter) == guessing_letter
        ]

        if len(all_secret_letter) > 0:
            return all_secret_letter

        self.error_guessing_remaining -= 1

    def __update_guessing_word(self, letter_to_display: list[tuple[int, str]]):
        """
        Update the `secret_word_guessing` according to the `letter_to_display`
        :param list[tuple[int, str]] letter_to_display: Letter to display in the `secret_word_guessing`
        :return: None
        """
        list_letter = [letter for letter in self.secret_word_guessing]
        for index, letter in letter_to_display:
            list_letter.pop(index)
            list_letter.insert(index, letter)

        self.secret_word_guessing = "".join(list_letter)

    def __print_info_player(self, message):
        if isinstance(self.guesser, Human) or isinstance(self.game_master, Human):
            print(message)
