import unittest
from maze import Maze
from wall_follower import WallFollower

class TestWallFollower(unittest.TestCase):
    def setUp(self):
        self.class_maze = Maze(5)
        self.kruskal_maze = self.class_maze.solution
        self.air_directed_maze = self.class_maze.air_directed_maze
        self.wall_follower = WallFollower(self.air_directed_maze)

    def test_solution_is_empty_at_start(self):
        solution = self.wall_follower.solution
        empty = []
        self.assertEqual(solution, empty)

    def test_maze_is_solved(self):
        self.wall_follower.solve_maze()
        solution = self.wall_follower.solution
        empty = []
        self.assertNotEqual(solution,empty)

    def test_turn_right_returns_correct_air_direction(self):
        """
        north -> east
        east -> south
        south -> west
        west -> north
        """
        north = 0
        east = 1
        south = 2
        west = 3

        right_moving_north = self.wall_follower.turn_where_is_right(0) == east
        right_moving_east = self.wall_follower.turn_where_is_right(1) == south
        right_moving_south = self.wall_follower.turn_where_is_right(2) == west
        right_moving_west = self.wall_follower.turn_where_is_right(3) == north

        self.assertEqual(True, right_moving_north)
        self.assertEqual(True, right_moving_east)
        self.assertEqual(True, right_moving_south)
        self.assertEqual(True, right_moving_west)
        
    def test_turn_left_returns_correct_air_direction(self):
        """
        north -> west
        east -> north
        south -> east
        west -> south
        """
        north = 0
        east = 1
        south = 2
        west = 3

        left_moving_north = self.wall_follower.turn_where_is_left(0) == west
        left_moving_east = self.wall_follower.turn_where_is_left(1) == north
        left_moving_south = self.wall_follower.turn_where_is_left(2) == east
        left_moving_west = self.wall_follower.turn_where_is_left(3) == south

        self.assertEqual(True, left_moving_north)
        self.assertEqual(True, left_moving_east)
        self.assertEqual(True, left_moving_south)
        self.assertEqual(True, left_moving_west)

    def test_solution_size_is_adjusted_to_fit_in_maze(self):
        maze_size = 20
        maze = Maze(maze_size)
        wall_follower = WallFollower(maze.air_directed_maze)
        wall_follower.draw_solution()
        cell_thickness = int((10/maze_size)*20)
        wall_thickness = int((10/maze_size)*6)
        self.assertEqual(wall_follower.cell_thickness, cell_thickness)
        self.assertEqual(wall_follower.wall_thickness, wall_thickness)
