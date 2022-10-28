from models.abstract.AI import AI
from models.LetterUsageSoup import LetterUsageSoup

list_best_letter = ["e", "s", "a", "r", "t", "i", "n", "u", "l", "o", "d", "c"]


class AiDump(AI):
    def __init__(self):
        super(AiDump, self).__init__()

        letter_usage = LetterUsageSoup()

        self.list_best_letter = letter_usage.get_most_frequency_letters()

    def guessing_letter(self, list_guessing_letters: list[str], regex_pattern: str) -> str:
        # Return different letter each time.
        return self.list_best_letter[len(list_guessing_letters)]
