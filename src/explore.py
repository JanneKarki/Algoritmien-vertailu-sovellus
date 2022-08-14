north = 0
east = 1
south = 2
west = 3

class Explore:
    def __init__(self, maze):
        self.maze = maze


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