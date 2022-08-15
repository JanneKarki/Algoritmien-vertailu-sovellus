import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(5)

    def test_maze_size_is_correct(self):
        size = self.maze.maze_size
        self.assertEqual(size, 5)

    def test_maze_created_with_kruskal(self):
        maze = self.maze.solution
        empty_maze = []
        self.assertNotEqual(maze, empty_maze)

    def test_maze_turned_to_air_directed_set(self):
        air_directed_maze = self.maze.air_directed_maze
        empty_set = {}
        self.assertNotEqual(air_directed_maze, empty_set)

    def test_air_directed_set_length_correct(self):
        length = len(self.maze.air_directed_maze)
        self.assertEqual(length, 5*5)

    def test_air_directed_maze_set_has_starting_point(self):
        maze = self.maze.air_directed_maze
        start = (0, 0)
        find = start in maze
        self.assertEqual(True, find)
