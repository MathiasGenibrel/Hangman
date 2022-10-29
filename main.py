# from models.WordFinder import WordFinder
from models.AiSmart import AiSmart

from models.Hangman import Hangman
from models.Human import Human

# from models.AiRandom import AiRandom
# from models.AiDump import AiDump
# # game_master = AiRandom()
# # guesser = Human("Greg")
#
# # game_master = Human("Alfred")
# # guesser = AiRandom()
#
# game_master = Human("Alfred")
# guesser = AiDump()
#
game_master = Human("Alfred")
guesser = AiSmart()
#
Hangman(game_master=game_master, guesser=guesser).start_game()

# print(WordFinder().get_list_word(["a", "e", "s"], 6))
