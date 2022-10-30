import re
import time
import json
import string
import requests

from math import floor
from random import choice, randint
from bs4 import BeautifulSoup


class WordListGenerator:
    def __init__(self):
        # Same regex at Hangman class
        self.regex_pattern = r"[A-Za-zÀ-ÿ]+$"

        # Set default attributs
        self.url = "https://www.le-dictionnaire.com/repertoire/"
        self.list_letter = [letter for letter in string.ascii_lowercase]
        self.max_page_path = {}

        # Update self.max_page_path, to it's initial value.
        self.__get_max_page_path()

        # Set value for the word list file
        self.filename = "WordList"
        self.file_format = "json"

        # Contains all select word by algorithm
        self.selected_words = []

    def generate_file(self):
        while len(self.selected_words) < 1000:
            self.__get_words()

        with open(f"{self.filename}.{self.file_format}", "w+") as file:
            json.dump(dict(words=self.selected_words), file)

            print("\nFile Created ! 🎉")
            print(f"The file was named : '{self.filename}.{self.file_format}'")

    # Refactor this into 1 parent class (this method was used in 3 différent files)
    @staticmethod
    def __get_source_code(url, params=None):
        return requests.get(url, params=params).text

    def __get_words(self):
        current_letter = choice(self.list_letter)
        current_page = randint(1, self.max_page_path[current_letter])
        current_url = f"{self.url}{current_letter}{current_page:02d}"

        soup = BeautifulSoup(self.__get_source_code(url=current_url), "html.parser")
        words_list = [
            link.text
            for link in soup.find_all("a")
            if "/definition/" in link.get("href")
               and re.match(self.regex_pattern, link.text)
               and 4 <= len(link.text) <= 12
        ]

        self.selected_words += words_list

    def __get_max_page_path(self):
        print("Preparation of letter path dictionary ...")
        for letter in self.list_letter:
            time.sleep(0.25)
            # Build url, this current url correspond to this (for letter 'a'):
            # "https://www.le-dictionnaire.com/repertoire/a01"
            current_url = f"{self.url}{letter}01"

            soup = BeautifulSoup(self.__get_source_code(current_url), "html.parser")

            paths_current_letter = [
                link.get("href")
                for link in soup.find_all("a")
                if f"/repertoire/{letter}" in link.get("href")
            ]

            self.max_page_path[letter] = len(paths_current_letter)
            print(f"In progress ...{floor(len(self.max_page_path) / len(self.list_letter) * 100)}%")
