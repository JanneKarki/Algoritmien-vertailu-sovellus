import unittest
from maze import Maze
from wall_follower import WallFollower

class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.class_maze = Maze(5)
        self.maze = self.class_maze.maze_by_kruskal()
        self.wall_follower = WallFollower(self.maze)

    def test_solution_is_empty_at_start(self):
        solution = self.wall_follower.solution
        empty = []
        self.assertEqual(solution, empty)