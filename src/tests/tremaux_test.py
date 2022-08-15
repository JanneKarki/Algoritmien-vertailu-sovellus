import unittest
from maze import Maze
from tremaux import Tremaux


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

    def test_cells_visited_twice_is_correct(self):
        tremaux = Tremaux(self.my_maze)
        visited_twice = tremaux.visited_twice
        listed_cells = []
        self.assertEqual(visited_twice, listed_cells)
