import unittest
from maze import Maze
from explore import Explore


class TestExplore(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(5)
        self.explore = Explore(self.maze)

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

        right_moving_north = self.explore.turn_where_is_right(0) == east
        right_moving_east = self.explore.turn_where_is_right(1) == south
        right_moving_south = self.explore.turn_where_is_right(2) == west
        right_moving_west = self.explore.turn_where_is_right(3) == north

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

        left_moving_north = self.explore.turn_where_is_left(0) == west
        left_moving_east = self.explore.turn_where_is_left(1) == north
        left_moving_south = self.explore.turn_where_is_left(2) == east
        left_moving_west = self.explore.turn_where_is_left(3) == south

        self.assertEqual(True, left_moving_north)
        self.assertEqual(True, left_moving_east)
        self.assertEqual(True, left_moving_south)
        self.assertEqual(True, left_moving_west)
