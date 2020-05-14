

from tic_tac_toe.game import Game, GameTied, InvalidMove
from tic_tac_toe.player import Player
from tic_tac_toe.ai_player import AIPlayer
from tic_tac_toe import io
import sys

# Initialize objects
game = Game(3)
players = [Player('X'), AIPlayer('O')]
playing = True # Main loop control needed to break out of multiple levels
io.init()

# Main game loop
while playing:
  io.print_board(game)
  try:
    for player in players:
      player.make_move(game)
      if game.check_winner(player.symbol):
        io.print_board(game)
        if players.index(player) == 0:
          io.winner()
        else:
          io.loser()
        playing = False
        break

  except InvalidMove:
    io.invalid()

  except GameTied:
    io.print_board(game)
    io.game_tied()
    break

  except KeyboardInterrupt:
    io.game_over()
    break
