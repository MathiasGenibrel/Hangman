from models.Hangman import Hangman
from models.Player import Player
from models.AiRandom import AiRandom

game_master = Player("Alfred")
# guesser = Player("Greg")
guesser = AiRandom()

Hangman(game_master=game_master, guesser=guesser).start_game()
