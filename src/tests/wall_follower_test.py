import unittest
from maze import Maze
from wall_follower import WallFollower

class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.class_maze = Maze(5)
        self.kruskal_maze = self.class_maze.solution
        self.air_directed_maze = self.class_maze.air_directed_maze
        self.wall_follower = WallFollower(self.air_directed_maze)

    def test_maze_is_solved(self):
        self.wall_follower.solve_maze()
        solution = self.wall_follower.solution
        empty = []
        self.assertNotEqual(solution,empty)

    