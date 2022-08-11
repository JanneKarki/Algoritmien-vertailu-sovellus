from PIL import Image, ImageDraw
import math

north = 0
east = 1
south = 2
west = 3

class WallFollower:
    def __init__(self, maze):
        self.maze = maze
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        self.wall_thickness = 6
        self.cell_thickness = 20
        self.total_cell_thickness = 26
        self.cell_center = 13
        

    def no_wall_in_front(self, cell, moving_direction):
        air_directions = self.maze[cell]
        if air_directions[moving_direction] == 1:  
            return True
        return False    
    
    def try_right(self, cell, moving_direction):
        air_directions = self.maze[cell]
        right = self.turn_where_is_right(moving_direction)
        if air_directions[right] == 1:  
            return True
        return False

    def turn_where_is_right(self, moving_direction):
        if moving_direction == north:
            return east 
        if moving_direction == east:
            return south
        if moving_direction == south:
            return west
        if moving_direction == west:
            return north

    def turn_where_is_left(self, moving_direction):
        if moving_direction == north:
            return west 
        if moving_direction == east:
            return north
        if moving_direction == south:
            return east
        if moving_direction == west:
            return south

    def move_forward(self, cell, moving_direction):
        if moving_direction == north:
            cell = (cell[0]-1, cell[1])
        if moving_direction == east:
            cell = (cell[0], cell[1]+1)
        if moving_direction == south:
            cell = (cell[0]+1, cell[1])
        if moving_direction == west:
            cell = (cell[0], cell[1]-1)
        return cell

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = east
        while cell != ((self.maze_size-1,self.maze_size-1)):
            self.solution.append(cell)
            if self.try_right(cell, moving_direction):
                moving_direction = self.turn_where_is_right(moving_direction)
                cell = self.move_forward(cell, moving_direction)
                print("turned and moved to right")
                continue

            if self.no_wall_in_front(cell, moving_direction):    
                cell = self.move_forward(cell, moving_direction)
                print("no wall in front")
                continue
            
            else:
                moving_direction = self.turn_where_is_left(moving_direction)
                print("wall in front, turn left")
                continue
            
        last_step = (self.maze_size-1,self.maze_size-1)
        self.solution.append(last_step)

    def draw_solution(self):
        self.adjust_solution_size()
        self.solve_maze()
        with Image.open("src/data/maze.png") as im:

            draw = ImageDraw.Draw(im)
            last_point = (0,0)
            for line in self.solution:
                print(line)
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
            im.save("src/data/solution.png")

    def adjust_solution_size(self):
        if self.maze_size > 10:
            self.cell_thickness = int((10/self.maze_size)*20)
            self.wall_thickness = int((10/self.maze_size)*5)
            if self.wall_thickness < 1:
                self.wall_thickness = 1
            self.total_cell_thickness = round(self.cell_thickness+self.wall_thickness)
            self.cell_center = round(self.total_cell_thickness/2)
        else:
            return
