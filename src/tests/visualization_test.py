import unittest
from maze import Maze
from visualization import Visualization
from wall_follower import WallFollower


class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.visualization = Visualization()
        self.maze_size = 20
        self.maze = Maze(self.maze_size)
        self.wall_follower = WallFollower(self.maze.air_directed_maze)

    def test_solution_drawing_size_is_adjusted_to_fit_in_the_maze(self):
        solution = self.wall_follower.solution
        algorithm = "wall_follower"
        maze_size = self.wall_follower.maze_size
        self.visualization.draw_solution(solution, algorithm, maze_size)

        cell_thickness = int((10/self.maze_size)*20)
        wall_thickness = int((10/self.maze_size)*6)

        self.assertEqual(self.visualization.cell_thickness, cell_thickness)
        self.assertEqual(self.visualization.wall_thickness, wall_thickness)
