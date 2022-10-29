import time

from models.abstract.AI import AI
from models.LetterUsageSoup import LetterUsageSoup
from models.WordFinder import WordFinder


class AiSmart(AI):
    def __init__(self):
        super(AiSmart, self).__init__()

        letter_usage = LetterUsageSoup()

        self.list_best_letter = letter_usage.get_most_frequency_letters()
        self.words_finder = WordFinder()

    def guessing_letter(self, list_guessing_letters: list[str], regex_pattern: str, secret_word_guessing=None) -> str:
        letters_found = [letter for letter in secret_word_guessing if letter != "_"]
        time.sleep(1)

        if len(list_guessing_letters) == 0 or len(letters_found) == 0:
            guessing_letter = self.list_best_letter[len(list_guessing_letters)]
        else:
            # Decomposition of parameters, for the function to get all words corresponding to letter already found
            length_secret_word = len(secret_word_guessing)
            print(f"Letters Found = {letters_found}")

            words_list = self.words_finder.get_list_word(letter_found=letters_found,
                                                         length_secret_word=length_secret_word)

            guessing_letter = self.get_letter_probability(words_list, list_guessing_letters)

        return guessing_letter

    @staticmethod
    def get_letter_probability(words_list, list_guessing_letters) -> list[str]:
        all_letter = [
            letter
            for word in words_list
            for letter in word
            if letter not in list_guessing_letters
        ]

        count_letter = {letter: all_letter.count(letter) for letter in all_letter}

        # Sorted the dictionary in descending order
        sorted_count_letter = dict(sorted(count_letter.items(), key=lambda item: item[1], reverse=True))
        print(sorted_count_letter)
        print(words_list)

        # Return list of letter by best probability
        return [letter for letter in sorted_count_letter][0]
