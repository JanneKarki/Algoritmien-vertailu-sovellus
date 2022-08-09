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

    def draw_solution(self):
        self.solve_maze()
        with Image.open("src/data/maze.png") as im:

            draw = ImageDraw.Draw(im)
            last_point = (0,0)
            for line in self.solution:
                print(line)
                draw.line(fill="RGB(44,55,255)", width=5, xy=[(last_point[1]*25+12.5,last_point[0]*25+12.5),(line[1]*25+12.5,line[0]*25+12.5)])
                last_point = line
            im.save("src/data/solution.png")
