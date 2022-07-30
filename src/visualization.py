from maze import maze
from PIL import Image
import numpy as np

class Visualization:

    def __init__(self):
        self.maze_size = 10
        self.cell_thickness = 20
        self.wall_thickness = 5
        self.maze = maze.maze_by_kruskal()

    def draw_maze_image(self):
        img = np.zeros((self.maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness,
                self.maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness),dtype=np.uint8)

        for edge in self.maze:
            min_x = self.wall_thickness+min(edge[0][0],edge[1][0])*(self.cell_thickness + self.wall_thickness)
            max_x = self.wall_thickness+max(edge[0][0],edge[1][0])*(self.cell_thickness + self.wall_thickness)
            min_y = self.wall_thickness+min(edge[0][1],edge[1][1])*(self.cell_thickness + self.wall_thickness)
            max_y = self.wall_thickness+max(edge[0][1],edge[1][1])*(self.cell_thickness + self.wall_thickness)
            img[min_x:max_x+self.cell_thickness,min_y:max_y+self.cell_thickness] = 255

        return Image.fromarray(img)
        

if __name__ == "__main__":
    a = Visualization()
    image = a.draw_maze_image()
    image.show()    