import unittest
from algorithms.maze import Maze
from algorithms.tremaux import Tremaux


class TestTremaux(unittest.TestCase):
    def setUp(self):
        self.my_maze = {(0, 0): (0, 1, 1, 0),(0, 1): (0, 0, 0, 1),(0, 2): (0, 1, 1, 0),(0, 3): (0, 0, 1, 1),
                        (0, 4): (0, 0, 1, 0),(0, 5): (0, 1, 1, 0),(0, 6): (0, 0, 0, 1),(1, 0): (1, 1, 0, 0),
                        (1, 1): (0, 1, 1, 1),(1, 2): (1, 0, 0, 1),(1, 3): (1, 0, 0, 0),(1, 4): (1, 1, 0, 0),
                        (1, 5): (1, 0, 1, 1),(1, 6): (0, 0, 1, 0),(2, 0): (0, 0, 1, 0),(2, 1): (1, 1, 0, 0),
                        (2, 2): (0, 1, 0, 1), (2, 3): (0, 1, 0, 1),(2, 4): (0, 0, 1, 1), (2, 5): (1, 0, 1, 0),
                        (2, 6): (1, 0, 1, 0), (3, 0): (1, 0, 1, 0),(3, 1): (0, 0, 1, 0), (3, 2): (0, 1, 0, 0),
                        (3, 3): (0, 0, 1, 1), (3, 4): (1, 1, 1, 0),(3, 5): (1, 1, 0, 1), (3, 6): (1, 0, 0, 1),
                        (4, 0): (1, 1, 1, 0), (4, 1): (1, 0, 0, 1),(4, 2): (0, 1, 0, 0), (4, 3): (1, 1, 1, 1),
                        (4, 4): (1, 0, 0, 1), (4, 5): (0, 1, 1, 0),(4, 6): (0, 0, 0, 1), (5, 0): (1, 1, 0, 0),
                        (5, 1): (0, 1, 1, 1), (5, 2): (0, 1, 0, 1),(5, 3): (1, 0, 1, 1), (5, 4): (0, 1, 1, 0),
                        (5, 5): (1, 1, 0, 1), (5, 6): (0, 0, 1, 1),(6, 0): (0, 1, 0, 0), (6, 1): (1, 0, 0, 1),
                        (6, 2): (0, 1, 0, 0), (6, 3): (1, 1, 0, 1),(6, 4): (1, 1, 0, 1), (6, 5): (0, 0, 0, 1),
                        (6, 6): (1, 0, 0, 0)}
        self.tremaux = Tremaux(self.my_maze)
        self.maze_size = self.tremaux.maze_size

    def test_maze_size_is_correct(self): 
        self.assertEqual(self.maze_size, 7)

    def test_maze_is_solved(self):
        solved = self.tremaux.solution != []
        self.assertEqual(True, solved)

    def test_tremaux_ends_in_right_down_corner(self):
        end = self.tremaux.solution[len(self.tremaux.solution)-1]
        self.assertEqual(end, ((self.maze_size)-1,(self.maze_size)-1))
    
    def test_elapsed_time_is_calculated(self):
        measured_time = float(self.tremaux.elapsed_time) > 0
        self.assertEqual(True, measured_time)
