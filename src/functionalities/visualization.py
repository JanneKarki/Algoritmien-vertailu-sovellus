from PIL import Image, ImageDraw
import numpy as np


class Visualization:
    """Luokka joka vastaa labyrintin piirtämisestä kuvaksi"""

    def __init__(self):
        """Luokan konstruktori, joka määritää labyrintin solun ja seinän paksuuden.
        """
        self.cell_thickness = 20
        self.wall_thickness = 6
        self.total_cell_thickness = 26
        self.cell_center = 13

    def draw_maze_image(self, maze, maze_size):
        """Piirtää tallentaa labyrintin kuvan

        Args:
            maze (list): Piirrettävä labyrintti.
            maze_size (int): Labyrintin koko.
        """
        self.adjust_image_size(maze_size)
        img = np.zeros((maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness,
                        maze_size * (self.cell_thickness + self.wall_thickness) + self.wall_thickness), dtype=np.uint8)
        image_size = (maze_size * (self.cell_thickness +
                      self.wall_thickness) + self.wall_thickness)
        for edge in maze:

            min_x = self.wall_thickness + \
                min(edge[0][0], edge[1][0]) * \
                (self.cell_thickness + self.wall_thickness)
            max_x = self.wall_thickness + \
                max(edge[0][0], edge[1][0]) * \
                (self.cell_thickness + self.wall_thickness)
            min_y = self.wall_thickness + \
                min(edge[0][1], edge[1][1]) * \
                (self.cell_thickness + self.wall_thickness)
            max_y = self.wall_thickness + \
                max(edge[0][1], edge[1][1]) * \
                (self.cell_thickness + self.wall_thickness)
            img[min_x:max_x+self.cell_thickness,
                min_y:max_y+self.cell_thickness] = 255
            img[0:self.wall_thickness,
                self.wall_thickness:self.cell_thickness+self.wall_thickness] = 255
            img[image_size-self.wall_thickness:image_size, image_size -
                (self.cell_thickness+self.wall_thickness):image_size-self.wall_thickness] = 255
        image = Image.fromarray(img)
        image.save("src/data/maze.png")

    def adjust_image_size(self, maze_size):
        """Säätäää solun ja seinämän paksuutta niin että kuvan ulkomitat
           pysyvät samankokoisina eri kokoisilla labyrinteillä.

        Args:
            maze_size (int): Labyrintin koko.
        """
        if maze_size > 10:
            self.cell_thickness = int((10/maze_size)*20)
            self.wall_thickness = int((10/maze_size)*6)
            if self.wall_thickness < 1:
                self.wall_thickness = 1
        else:
            self.cell_thickness = 20
            self.wall_thickness = 6

    def draw_solution(self, solution, algorithm, maze_size):
        """Piirtää ratkaistun reitin labyrintin kuvaan.
        """
        self.adjust_solution_size(maze_size)
        path = "src/data/solution_" + algorithm + ".png"
        with Image.open("src/data/maze.png") as im:

            draw = ImageDraw.Draw(im)
            last_point = (0, 0)
            for line in solution:
                draw.line(
                    fill="RGB(44,55,255)",
                    width=self.wall_thickness,
                    xy=[(last_point[1]*self.total_cell_thickness+self.cell_center,
                         last_point[0]*self.total_cell_thickness+self.cell_center),
                        (line[1]*self.total_cell_thickness+self.cell_center,
                         line[0]*self.total_cell_thickness+self.cell_center)
                        ]
                )

                last_point = line
            im.save(path)

    def adjust_solution_size(self, maze_size):
        """Säätää piirrettävän ratkaisun kokoa labyrintin kokoa vastaavaksi.
        """
        if maze_size > 10:
            self.cell_thickness = int((10/maze_size)*20)
            self.wall_thickness = int((10/maze_size)*6)
            if self.wall_thickness < 1:
                self.wall_thickness = 1
            self.total_cell_thickness = round(
                self.cell_thickness+self.wall_thickness)
            self.cell_center = round(self.total_cell_thickness/2)
        else:
            self.cell_thickness = 20
            self.wall_thickness = 6


visualization = Visualization()
