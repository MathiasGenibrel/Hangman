import string
import requests
from bs4 import BeautifulSoup


# List frequency letter get by scrapping wikipedia :
# (https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres)

class LetterUsageSoup:
    def __init__(self):
        # Use Wikipedia to get order of the most frequencies letter in French language.
        self.url = "https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres"

    def get_most_frequency_letters(self):
        soup = BeautifulSoup(self.__get_source_page(), "html.parser")

        # Get the first table, the first table corresponding to the frequency letter table
        frequency_letter_table = soup.find("table", class_="wikitable sortable")

        # Get all letter in the order (by default the table has been sorted to most frequently letter to the less)
        letter_by_most_frequency = [
            letter.text.strip("\n")
            for row in frequency_letter_table.find_all("tr")
            for letter in row.find_all("td") if letter.text.strip("\n") in string.ascii_lowercase
        ]

        return letter_by_most_frequency

    def __get_source_page(self):
        source_page = requests.get(self.url)

        return source_page.text
