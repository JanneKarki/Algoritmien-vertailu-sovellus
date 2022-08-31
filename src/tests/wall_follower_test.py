import unittest
from algorithms.maze import Maze
from algorithms.wall_follower import WallFollower


class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.class_maze = Maze(5)
        self.kruskal_maze = self.class_maze.solution
        self.air_directed_maze = self.class_maze.air_directed_maze
        self.wall_follower = WallFollower(self.air_directed_maze)
        self.solution = self.wall_follower.solution
        self.maze_size =self.wall_follower.maze_size

    def test_maze_is_solved(self):
        solved = self.wall_follower.solution != []
        self.assertEqual(True, solved)

    def test_maze_size_is_correct(self): 
        self.assertEqual(self.maze_size, 5)

    def test_wall_follower_ends_in_down_right_corner(self):
        end = self.wall_follower.solution[len(self.wall_follower.solution)-1]
        self.assertEqual(end, ((self.maze_size)-1,(self.maze_size)-1))
    
    def test_elapsed_time_is_calculated(self):
        measured_time = float(self.wall_follower.elapsed_time) > 0
        self.assertEqual(True, measured_time)
