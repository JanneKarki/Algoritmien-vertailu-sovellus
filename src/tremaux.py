from explore import Explore
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
        self.explore = Explore(self.maze)
        self.wall_thickness = 6
        self.cell_thickness = 20
        self.total_cell_thickness = 26
        self.cell_center = 13
        self.elapsed_time = None
        self.visited = []
        self.visited_twice = []

        self.solve_maze()

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = east

        while cell != ((self.maze_size-1,self.maze_size-1)):

            self.visited.append(cell)       
            unvisited_directions = self.not_visited_directions(cell, moving_direction)

            if unvisited_directions:
                moving_direction = random.choice(unvisited_directions)  
                cell = self.explore.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue

            if not unvisited_directions:
                once_visited_directions = self.visited_directions(cell, moving_direction)
               
                if not once_visited_directions:
                    moving_direction = self.explore.turn_around(moving_direction)
                    continue
                else:
                    if len(once_visited_directions) == 1:
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

    def not_visited_directions(self, cell, moving_direction):
        unvisited_directions = []

        left_cell = self.explore.turn_where_is_left(moving_direction)
        right_cell = self.explore.turn_where_is_right(moving_direction)
        front_cell = moving_direction

        if (
            self.explore.try_right(cell, moving_direction) and
            self.explore.move_forward(cell, right_cell) not in self.visited
            ):

            unvisited_directions.append(right_cell)

        if (
            self.explore.no_wall_in_front(cell, moving_direction) and
            self.explore.move_forward(cell, front_cell) not in self.visited
            ):

            unvisited_directions.append(moving_direction)

        if (
            self.explore.try_left(cell, moving_direction) and
            self.explore.move_forward(cell, left_cell) not in self.visited
            ):

            unvisited_directions.append(left_cell)

        return unvisited_directions
        
    def visited_directions(self, cell, moving_direction):
        once_visited_directions = []

        left_cell = self.explore.turn_where_is_left(moving_direction)
        right_cell = self.explore.turn_where_is_right(moving_direction)
        front_cell = moving_direction

        if (
            self.explore.try_right(cell, moving_direction) and
            self.explore.move_forward(cell, right_cell) in self.visited and
            self.explore.move_forward(cell, right_cell) not in self.visited_twice
            ):

            once_visited_directions.append(right_cell)
            
        if (
            self.explore.no_wall_in_front(cell, moving_direction) and
            self.explore.move_forward(cell, front_cell) in self.visited and
            self.explore.move_forward(cell, front_cell) not in self.visited_twice
            ):

            once_visited_directions.append(moving_direction)

        if (
            self.explore.try_left(cell,moving_direction) and
            self.explore.move_forward(cell, left_cell) in self.visited and
            self.explore.move_forward(cell, left_cell) not in self.visited_twice
            ):

            once_visited_directions.append(left_cell)

        return once_visited_directions