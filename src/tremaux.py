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
        self.visited = []
        self.visited_twice = []

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = east
        visited = []
        visited_twice = []

        while cell != ((self.maze_size-1,self.maze_size-1)):
            unvisited_directions = []
            once_visited_directions = []

            print(cell)
            self.visited.append(cell)
            left_cell = self.explore.turn_where_is_left(moving_direction)
            right_cell = self.explore.turn_where_is_right(moving_direction)
            front_cell = moving_direction

        

            unvisited_directions = self.not_visited_directions(cell, moving_direction)
            if unvisited_directions:
                moving_direction = random.choice(unvisited_directions)  
                cell = self.explore.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue

            #jos ei ole kulkemattomia suuntia tarkista onko kerran kuljettuja suuntia
            if not unvisited_directions:
                print("not unvisited directions")
                if self.explore.try_right(cell, moving_direction) and self.explore.move_forward(cell, right_cell) in self.visited and self.explore.move_forward(cell, right_cell) not in self.visited_twice:
                    once_visited_directions.append(right_cell)
                if self.explore.no_wall_in_front(cell, moving_direction) and self.explore.move_forward(cell, front_cell) in self.visited and self.explore.move_forward(cell, front_cell) not in self.visited_twice:
                    once_visited_directions.append(moving_direction)
                    print("eteenpäin pääsee takaisin ")
                if self.explore.try_left(cell,moving_direction) and self.explore.move_forward(cell, left_cell) in self.visited and self.explore.move_forward(cell, left_cell) not in self.visited_twice:
                    once_visited_directions.append(left_cell)

                print(once_visited_directions)
                if not once_visited_directions and not unvisited_directions:
                    print("este edessä")
                    moving_direction = self.explore.turn_around(moving_direction)
                    
                    continue
                else:
                    if len(once_visited_directions) == 1:
                        print("vain yksi suunta jo kuljettu suunta")
                        self.visited_twice.append(cell)
                        moving_direction = once_visited_directions[0]
                        cell = self.explore.move_forward(cell, moving_direction)
                        self.solution.append(cell)
                        continue
                    else:
                        moving_direction = random.choice(once_visited_directions)
                        cell = self.explore.move_forward(cell, moving_direction)
                        self.solution.append(cell)
                        continue

        print(self.visited_twice, "visited twice")
        print(self.solution)

    def not_visited_directions(self, cell, moving_direction):
        unvisited_directions = []

        left_cell = self.explore.turn_where_is_left(moving_direction)
        right_cell = self.explore.turn_where_is_right(moving_direction)
        front_cell = moving_direction

        if self.explore.try_right(cell, moving_direction) and self.explore.move_forward(cell, right_cell) not in self.visited:
            unvisited_directions.append(right_cell)
        if self.explore.no_wall_in_front(cell, moving_direction) and self.explore.move_forward(cell, front_cell) not in self.visited:
            unvisited_directions.append(moving_direction)
        if self.explore.try_left(cell, moving_direction) and self.explore.move_forward(cell, left_cell) not in self.visited:
            unvisited_directions.append(left_cell)
        
        return unvisited_directions
        


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
                im.save("src/data/solution_tremaux.png")

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

