import requests
from bs4 import BeautifulSoup


class WordFinder:
    def __init__(self, word_check: int = 100):
        # The data is provided from this website -> "https://scrabbledb.com/"
        # The param -> q is usage for pass the letter is in the secret word.
        # Use r param to change the size of the word table
        self.url = "https://scrabbledb.com/api.php"
        self.params = {
            "s": "fr_aspell",
            "l": "fr",
            "r": word_check,
            "q": str()
        }

        # TODO: add cache system

    def get_list_word(self, letter_found: list[str], length_secret_word: int) -> list[str] or str:
        """
        Get a list of all words possibility with the current letter found and the length of the secret word.
        :param list[str] letter_found: List of letters found that are present in the secret word.
        :param int length_secret_word: Total length of the secret word.
        :return: Return a list with all words found, or return a string with an error message.
        """

        # Update the query param, for search word, cannot be None and the max length is 12.
        self.params["q"] = self.__get_global_letters(letter_found, length_secret_word)

        # Try if we can request get the source code on the context url.
        try:
            words_list = self.__get_words_list(length_secret_word)

            return words_list
        except ConnectionError as error:
            # Return a Message Error (only catch ConnectionError)
            return f"Connection error : {error}"

    def __get_source_code(self) -> str:
        """
        Get the source code of the context url
        :return: String contains the source code, on string format.
        """
        source_page = requests.get(self.url, params=self.params)

        return source_page.text

    def __get_words_list(self, length_secret_word: int) -> list[str] or ConnectionError:
        """
        Get words list from a web page.
        :param int length_secret_word: Use this param to remove all word not corresponding at our secret word.
        :return: A list of words that could match our secret word.
        """
        try:
            source_code = self.__get_source_code()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Une erreur avec le serveur distant est survenue, Veuillez ressayer plus tard.")

        soup = BeautifulSoup(source_code, "html.parser")

        # Get all words equal to the same length of secret word, in the web page
        words = [
            word.text.lower()
            for word in soup.find_all("a", {"id": "wordLink"})
            if len(word.text) == length_secret_word
        ]

        return words

    @staticmethod
    def __get_global_letters(letter_found: list[str], length_secret_word: int) -> str:
        """
        Format letter present in the secret word and the length of the secret word, in string ready for the request.
        \n
        Example: letter_found : ["a","b","c"], length_secret_word: 6 => return "abc***"
        :param list[str] letter_found: List of letters found that are present in the secret word.
        :param int length_secret_word: Total length of the secret word.
        :return: Formatted string (to match api format) => "abc***"
        """
        # Concat list
        global_letters_list = [] + letter_found

        for index in range(len(letter_found), length_secret_word):
            global_letters_list.insert(index, "*")

        return "".join(global_letters_list)
