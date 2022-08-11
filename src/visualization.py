from PIL import Image
import numpy as np
import math
class Visualization:

    def __init__(self):
        self.cell_thickness = 20
        self.wall_thickness = 5

    def draw_maze_image(self, maze, maze_size):
        img = np.zeros((maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness,
                maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness),dtype=np.uint8)
        image_size = (maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness)
        for edge in maze:

            min_x = self.wall_thickness+min(edge[0][0],edge[1][0])*(self.cell_thickness + self.wall_thickness)
            max_x = self.wall_thickness+max(edge[0][0],edge[1][0])*(self.cell_thickness + self.wall_thickness)
            min_y = self.wall_thickness+min(edge[0][1],edge[1][1])*(self.cell_thickness + self.wall_thickness)
            max_y = self.wall_thickness+max(edge[0][1],edge[1][1])*(self.cell_thickness + self.wall_thickness)
            img[min_x:max_x+self.cell_thickness,min_y:max_y+self.cell_thickness] = 255
            img[0:self.wall_thickness , self.wall_thickness :self.cell_thickness+self.wall_thickness] = 255
            img[image_size-self.wall_thickness:image_size, image_size-(self.cell_thickness+self.wall_thickness):image_size-self.wall_thickness] = 255
        image = Image.fromarray(img)
        image.save("src/data/maze.png")
        return image

visualization = Visualization()