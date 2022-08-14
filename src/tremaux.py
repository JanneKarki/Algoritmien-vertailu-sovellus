from explore import Explore
import math
from maze import Maze
import random
from PIL import Image, ImageDraw
north = 0
east = 1
south = 2
west = 3

class Tremaux:
    def __init__(self, maze):
        self.maze = maze
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        self.explore = Explore(self.maze)
        self.wall_thickness = 6
        self.cell_thickness = 20
        self.total_cell_thickness = 26
        self.cell_center = 13
        self.elapsed_time = None

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = east
        visited = {}

        while cell != ((self.maze_size-1,self.maze_size-1)):
            available_directions = []

           
            if self.explore.try_right(cell, moving_direction) and cell not in visited:
                available_directions.append(self.explore.turn_where_is_right(moving_direction))
            if self.explore.no_wall_in_front(cell, moving_direction) and cell not in visited:
                available_directions.append(moving_direction)
            if self.explore.try_left(cell, moving_direction) and cell not in visited:
                available_directions.append(self.explore.turn_where_is_left(moving_direction))

            if available_directions:
                moving_direction = random.choice(available_directions)
                cell = self.explore.move_forward(cell, moving_direction)
                
            if not available_directions:
                if self.explore.try_right(cell, moving_direction) and cell in visited:
                    if visited[cell] == 1:
                        available_directions.append(self.explore.turn_where_is_right(moving_direction))
                if self.explore.no_wall_in_front(cell, moving_direction) and cell in visited:
                    if visited[cell] == 1:
                        available_directions.append(moving_direction)
                if self.explore.try_left(cell,moving_direction) and cell in visited:
                    available_directions.append(self.explore.turn_where_is_left(moving_direction))

                if not available_directions:
                    moving_direction = self.explore.turn_around(moving_direction)
                    continue
                else:
                    moving_direction = random.choice(available_directions)
                    cell = self.explore.move_forward(cell, moving_direction)


            #else:
            print(available_directions)
            
            if cell not in visited:
                visited[cell] = 1
            else:
                visited[cell] = 2

            
            self.solution.append(cell)
            print(self.solution)

    def draw_solution(self):
            """Piirtää ratkaistun reitin labyrintin kuvaan.
            """
            self.adjust_solution_size()
            self.solve_maze()
            with Image.open("src/data/maze.png") as im:

                draw = ImageDraw.Draw(im)
                last_point = (0,0)
                for line in self.solution:
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
                im.save("src/data/solution_treamux.png")

    def adjust_solution_size(self):
            """Säätää piirrettävän ratkaisun kokoa labyrintin kokoa vastaavaksi.
            """
            if self.maze_size > 10:
                self.cell_thickness = int((10/self.maze_size)*20)
                self.wall_thickness = int((10/self.maze_size)*6)
                if self.wall_thickness < 1:
                    self.wall_thickness = 1
                self.total_cell_thickness = round(self.cell_thickness+self.wall_thickness)
                self.cell_center = round(self.total_cell_thickness/2)
            else:
                self.cell_thickness = 20
                self.wall_thickness = 6

