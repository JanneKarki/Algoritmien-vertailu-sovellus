import math
from maze import Maze
import random

north = 0
east = 1
south = 2
west = 3

class Tremaux:
    def __init__(self, maze):
        self.maze = maze
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        #self.wall_thickness = 6
        #self.cell_thickness = 20
        #self.total_cell_thickness = 26
        #self.cell_center = 13
        #self.elapsed_time = None

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

    def turn_around(self, moving_direction):
        if moving_direction == north:
            return south
        if moving_direction == south:
            return north
        if moving_direction == east:
            return west
        if moving_direction == west:
            return east

    def try_left(self, cell, moving_direction):
        air_directions = self.maze[cell]
        right = self.turn_where_is_left(moving_direction)
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
        visited = {}

        while cell != ((self.maze_size-1,self.maze_size-1)):
            available_directions = []

           
            if self.try_right(cell, moving_direction) and cell not in visited:
                available_directions.append(self.turn_where_is_right(moving_direction))
            if self.no_wall_in_front(cell, moving_direction) and cell not in visited:
                available_directions.append(moving_direction)
            if self.try_left(cell, moving_direction) and cell not in visited:
                available_directions.append(self.turn_where_is_left(moving_direction))

            if not available_directions:
                if self.try_right(cell, moving_direction) and cell in visited:
                    if visited[cell] == 1:
                        available_directions.append(self.turn_where_is_right(moving_direction))
                if self.no_wall_in_front(cell, moving_direction) and cell in visited:
                    if visited[cell] == 1:
                        available_directions.append(moving_direction)
                if self.try_left(cell,moving_direction) and cell in visited:
                    available_directions.append(self.turn_where_is_left(moving_direction))

            if not available_directions:
                moving_direction = self.turn_around(moving_direction)
                


            #else:
            print(available_directions)
            moving_direction = random.choice(available_directions)
            if cell not in visited:
                visited[cell] = 1
            else:
                visited[cell] = 2

            cell = self.move_forward(cell, moving_direction)
            self.solution.append(cell)
            print(self.solution)

if __name__ == '__main__':
    maze_class = Maze(6)
    maze = maze_class.air_directed_maze
    tremaux = Tremaux(maze)
    tremaux.solve_maze()