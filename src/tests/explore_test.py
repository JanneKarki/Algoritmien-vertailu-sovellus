import unittest
from algorithms.maze import Maze
from functionalities.explore import Explore


class TestExplore(unittest.TestCase):
    def setUp(self):
        self.maze = {(0, 0): (0, 1, 0, 0),
                     (0, 1): (0, 0, 1, 1),
                     (0, 2): (0, 0, 1, 0),
                     (1, 0): (0, 1, 1, 0),
                     (1, 1): (1, 1, 1, 1),
                     (1, 2): (1, 0, 1, 1),
                     (2, 0): (1, 0, 0, 0),
                     (2, 1): (1, 0, 0, 0),
                     (2, 2): (1, 0, 0, 0)}

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

    def test_no_wall_in_front(self):
        cell = (0, 0)
        moving_east = 1
        no_wall = self.explore.no_wall_in_front(cell, moving_east)
        self.assertEqual(True, no_wall)

    def test_wall_is_in_front(self):
        cell = (0, 0)
        moving_north = 0
        no_wall = self.explore.no_wall_in_front(cell, moving_north)
        self.assertEqual(False, no_wall)

    def test_no_wall_in_right(self):
        cell = (0, 1)
        moving_south = 2
        no_wall = self.explore.try_right(cell, moving_south)
        self.assertEqual(True, no_wall)

    def test_wall_is_in_right(self):
        cell = (0, 1)
        moving_north = 0
        no_wall = self.explore.try_right(cell, moving_north)
        self.assertEqual(False, no_wall)

    def test_no_wall_in_left(self):
        cell = (0, 1)
        moving_west = 3
        no_wall = self.explore.try_left(cell, moving_west)
        self.assertEqual(True, no_wall)

    def test_wall_is_in_left(self):
        cell = (0, 1)
        moving_east = 1
        no_wall = self.explore.try_left(cell, moving_east)
        self.assertEqual(False, no_wall)

    def test_move_forward_east(self):
        cell = (1, 1)
        moving_east = 1
        location = self.explore.move_forward(cell, moving_east)
        self.assertEqual(location, (1, 2))

    def test_move_forward_south(self):
        cell = (1, 1)
        moving_south = 2
        location = self.explore.move_forward(cell, moving_south)
        self.assertEqual(location, (2, 1))

    def test_move_forward_west(self):
        cell = (1, 1)
        moving_west = 3
        location = self.explore.move_forward(cell, moving_west)
        self.assertEqual(location, (1, 0))

    def test_move_forward_north(self):
        cell = (1, 1)
        moving_north = 0
        location = self.explore.move_forward(cell, moving_north)
        self.assertEqual(location, (0, 1))

    def test_turn_around_returns_correct_direction(self):
        north = 0
        east = 1
        south = 2
        west = 3

        left_moving_north = self.explore.turn_around(0) == south
        left_moving_east = self.explore.turn_around(1) == west
        left_moving_south = self.explore.turn_around(2) == north
        left_moving_west = self.explore.turn_around(3) == east

        self.assertEqual(True, left_moving_north)
        self.assertEqual(True, left_moving_east)
        self.assertEqual(True, left_moving_south)
        self.assertEqual(True, left_moving_west)
