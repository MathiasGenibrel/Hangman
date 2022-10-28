from models.Hangman import Hangman
from models.Human import Human
from models.AiRandom import AiRandom

game_master = Human("Alfred")
# game_master = AiRandom()
# guesser = Human("Greg")
guesser = AiRandom()

Hangman(game_master=game_master, guesser=guesser).start_game()
