import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.maze = Maze(5)

    def test_maze_size_is_correct(self):
        size = self.maze.maze_size
        self.assertEqual(size, 5)

    def test_maze_created_with_kruskal(self):
        maze = self.maze.maze_by_kruskal()
        empty_maze = []
        self.assertNotEqual(maze, empty_maze)

    def test_maze_turned_to_air_directed_set(self):
        maze = self.maze.maze_by_kruskal()
        air_directed_maze = self.maze.maze_in_air_directions(maze)
        empty_set = {}
        self.assertNotEqual(air_directed_maze, empty_set)

    def test_air_directed_set_length_correct(self):
        maze = self.maze.maze_by_kruskal()
        air_directed_maze = self.maze.maze_in_air_directions(maze)
        length = len(air_directed_maze)
        self.assertEqual(length, 5*5)

    def test_air_directed_maze_set_has_starting_point(self):
        maze = self.maze.maze_by_kruskal()
        air_directed_maze = self.maze.maze_in_air_directions(maze)
        start = (0,0)
        find = start in air_directed_maze
        self.assertEqual(True, find)

