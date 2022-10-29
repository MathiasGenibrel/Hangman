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
        # Sleeping time to not get ban
        time.sleep(0.5)

        if len(list_guessing_letters) == 0 or len(letters_found) == 0:
            guessing_letter = self.list_best_letter[len(list_guessing_letters)]
        else:
            words_list = self.words_finder.get_list_word(
                letter_found=letters_found,
                length_secret_word=len(secret_word_guessing)
            )
            clean_words_list = self.remove_incorrect_words(words_list, secret_word_guessing)

            if len(clean_words_list) > 0:
                guessing_letter = self.get_letter_probability(clean_words_list, list_guessing_letters)
            # If no words match with the letter position of our secret_word, user basic words_list
            else:
                guessing_letter = self.get_letter_probability(words_list, list_guessing_letters)

        return guessing_letter

    def get_letter_probability(self, words_list: list[str], list_guessing_letters: list[str]) -> str:
        """
        Get the probability of each letter that could potentially be in the secret word.\n

        If the words list contains no potential words, we use the list with high frequency letters.
        :param list[str] words_list: List of all the words that can potentially be the secret word
        :param list[str] list_guessing_letters: List of all letters already played by the player
        :return: The letter with the best probability.
        """
        all_letter = [
            letter
            for word in words_list
            for letter in word
            if letter not in list_guessing_letters
        ]

        count_letter = {letter: all_letter.count(letter) for letter in all_letter}

        # Sorted the dictionary in descending order
        sorted_count_letter = dict(sorted(count_letter.items(), key=lambda item: item[1], reverse=True))

        # If the dictionary is empty, we return a list based on list with high frequency letters
        if len(sorted_count_letter) == 0:
            return [letter for letter in self.list_best_letter if letter not in list_guessing_letters][0]

        # Return list of letter by best probability
        return [letter for letter in sorted_count_letter][0]

    @staticmethod
    def remove_incorrect_words(words_list, secret_word_guessing) -> list[str]:
        """
        Remove words not match with the position of letter in the secret word.
        :param words_list: List of all the words that can potentially be the secret word
        :param secret_word_guessing: Secret word, to know the position of the letters that have been guessed
        :return: List of words can be the current secret word, can be emtpy list if no words in the list match.
        """
        # Get position of each letter in the secret word.
        enumerate_secret_word = [(index, letter) for index, letter in enumerate(secret_word_guessing) if letter != "_"]

        list_correct_potential_word = []

        # Control each position of letter in word of the list word
        # If one letter is not in same the position of secret_word
        # we don't add it on the correct potential word.
        for word in words_list:
            potential_correct_word = True
            for index, letter in enumerate_secret_word:
                if letter != word[index]:
                    potential_correct_word = False
                    break
            if potential_correct_word is True:
                list_correct_potential_word.append(word)

        return list_correct_potential_word
