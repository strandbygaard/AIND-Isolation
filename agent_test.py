"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit

from importlib import reload


class Timer:
    def __call__(self):
        return 1000


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    @unittest.skip("")
    def testMiniMax(self):
        minimaxPlayer = game_agent.MinimaxPlayer(search_depth=3)
        minimaxPlayer.time_left = Timer()
        self.game.apply_move((0, 0))
        self.game.apply_move((5, 5))

        time_millis = lambda: 1000 * timeit.default_timer()
        get_move_start = time_millis()
        move = minimaxPlayer.get_move(self.game, Timer())
        get_move_end = time_millis()
        print(self.game.to_string())

        print("Elapsed: " + str(get_move_end - get_move_start))

    def testAlphaBeta(self):
        alpha_beta_player = game_agent.AlphaBetaPlayer(search_depth=3)
        alpha_beta_player.time_left = Timer()
        self.game.apply_move((0, 0))
        self.game.apply_move((5, 5))

        time_millis = lambda: 1000 * timeit.default_timer()
        get_move_start = time_millis()
        move = alpha_beta_player.get_move(self.game, Timer())
        get_move_end = time_millis()
        print(self.game.to_string())

        print("Elapsed: " + str(get_move_end - get_move_start))


if __name__ == '__main__':
    unittest.main()
