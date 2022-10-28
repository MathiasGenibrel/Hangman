from models.Hangman import Hangman
from models.Human import Human
from models.AiRandom import AiRandom

# game_master = AiRandom()
# guesser = Human("Greg")
game_master = Human("Alfred")
guesser = AiRandom()

Hangman(game_master=game_master, guesser=guesser).start_game()
