from models.Hangman import Hangman
from models.Player import Player

game_master = Player("Alfred")
guesser = Player("Greg")

Hangman(game_master=game_master, guesser=guesser).start_game()
