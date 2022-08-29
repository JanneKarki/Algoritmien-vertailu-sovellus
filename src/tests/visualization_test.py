import unittest
from algorithms.maze import Maze
from functionalities.visualization import Visualization
from algorithms.wall_follower import WallFollower
from PIL import Image


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

    def test_wall_thickness_is_never_under_1_in_solution(self):
        solution = self.wall_follower.solution
        algorithm = "wall_follower"
        maze_size = 100
        self.visualization.draw_solution(solution, algorithm, maze_size)

        self.assertEqual(self.visualization.wall_thickness, 1)

    def test_draw_maze_image_creates_image_file(self):
        self.visualization.draw_maze_image(self.maze.solution, self.maze_size)
        image = Image.open("src/data/maze.png")

        self.assertEqual(str(type(image)), "<class 'PIL.PngImagePlugin.PngImageFile'>")

    def test_adjust_image_size_when_maze_size_is_over_10(self):
        maze_size = 30
        self.visualization.adjust_image_size(maze_size)

        wall = self.visualization.wall_thickness == int((10/maze_size)*6)
        cell = self.visualization.cell_thickness == int((10/maze_size)*20)

        self.assertEqual(True, wall)
        self.assertEqual(True, cell)

    def test_adjust_image_size_not_adjusted_when_maze_size_is_under_10(self):
        maze_size = 9
        self.visualization.adjust_image_size(maze_size)

        wall = self.visualization.wall_thickness == 6
        cell = self.visualization.cell_thickness == 20

        self.assertEqual(True, wall)
        self.assertEqual(True, cell)

    def test_adjust_image_size_wall_thickness_never_under_1(self):
        maze_size = 100
        self.visualization.adjust_image_size(maze_size)
        wall = self.visualization.wall_thickness == 1

        self.assertEqual(True, wall)
       