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
            clean_words_list = self.__remove_incorrect_words(words_list, secret_word_guessing)

            if len(clean_words_list) > 0:
                guessing_letter = self.__get_letter_probability(clean_words_list, list_guessing_letters)
            # If no words match with the letter position of our secret_word, user basic words_list
            else:
                guessing_letter = self.__get_letter_probability(words_list, list_guessing_letters)

        print(guessing_letter)

        return guessing_letter

    def __get_letter_probability(self, words_list: list[str], list_guessing_letters: list[str]) -> str:
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

        # The dictionary that contains the letters with the highest probability rate.
        sorted_count_letter = self.__get_probability_dictionary(count_letter)

        # If the dictionary is empty, we return a list based on list with high frequency letters
        if len(sorted_count_letter) == 0:
            return [letter for letter in self.list_best_letter if letter not in list_guessing_letters][0]

        # Return list of letter by best probability
        return [letter for letter in sorted_count_letter][0]

    @staticmethod
    def __remove_incorrect_words(words_list, secret_word_guessing) -> list[str]:
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

    def __get_probability_dictionary(self, dictionary):
        """
        Get dictionary with the highest probability letter
        :param dictionary: dictionary generate with list of word (scrapping)
        :return: dictionary with the highest probability letter
        """
        # Sorted the dictionary in descending order
        sorted_by_value = self.__sort_dictionary_by_value(dictionary)

        if len(sorted_by_value) <= 1:
            return sorted_by_value

        # Retrieves the first two elements, in order to compare them
        first_value = list(sorted_by_value.values())[0]
        second_value = list(sorted_by_value.values())[1]

        if first_value == second_value:
            # Get dictionary to represent value of letter by frequency in current language.
            best_letter_value = {
                letter: value for value, letter in
                enumerate(sorted(self.list_best_letter, reverse=True))
            }

            for letter, value in sorted_by_value.items():
                if value == first_value and letter in self.list_best_letter:
                    # Update the value and sort the dictionary again
                    sorted_by_value.update({letter: value + best_letter_value[letter]})
                    sorted_by_value = self.__sort_dictionary_by_value(sorted_by_value)

        # Return the dictionary without equality.
        return sorted_by_value

    @staticmethod
    def __sort_dictionary_by_value(dictionary):
        return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
