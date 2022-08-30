import unittest
from algorithms.maze import Maze
from algorithms.tremaux import Tremaux


class TestTremaux(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(5)
        self.tremaux = Tremaux(self.maze.air_directed_maze)
        self.my_maze = {(0, 0): (0, 1, 0, 0),
                        (0, 1): (0, 0, 1, 1),
                        (0, 2): (0, 0, 1, 0),
                        (1, 0): (0, 1, 1, 0),
                        (1, 1): (1, 1, 1, 1),
                        (1, 2): (1, 0, 1, 1),
                        (2, 0): (1, 0, 0, 0),
                        (2, 1): (1, 0, 0, 0),
                        (2, 2): (1, 0, 0, 0)}

    def test_maze_size_is_correct(self):
        maze_size = self.tremaux.maze_size
        self.assertEqual(maze_size, 5)
