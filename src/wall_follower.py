from maze import maze

north = 0
east = 1
south = 2
west = 3

class WallFollower:
    def __init__(self):
        self.maze = maze.maze_in_air_directions()
        self.solution = []
        self.maze_size = 5
        print(self.maze)

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
            print(cell)
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


if __name__ == "__main__":

    a = WallFollower()
    a.solve_maze()