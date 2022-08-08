from maze import maze

north = 0
east = 1
south = 2
west = 3

class WallFollower:
    def __init__(self, maze_size):
        self.maze = maze.maze_in_air_directions()
        self.solution = []
        self.maze_size = maze_size
        print(self.maze)

    def move_down(self, cell):
        air_directions = self.maze[cell]
        print(air_directions)
        if air_directions[south] == 1:
            print(cell)
            cell = (cell[0]+1, cell[1])
          
            return True, cell
        return False, cell

    def move_right(self, cell):
        air_directions = self.maze[cell]
        print(air_directions)
        if air_directions[east] == 1:
            print(cell)
            cell = (cell[0], cell[1]+1)
            return True, cell
        return False, cell

    def move_up(self, cell):
        air_directions = self.maze[cell]
        print(air_directions)
        if air_directions[north] == 1:
            print(cell)
            cell = (cell[0]-1, cell[1])
            return True, cell
        return False, cell

    def move_left(self, cell):
        air_directions = self.maze[cell]
       
        print(air_directions)
        if air_directions[west] == 1:
            print(cell)
            cell = (cell[0], cell[1]-1)
            return True, cell
        return False, cell
    
    def try_right(self, cell, moving_direction):
        air_directions = self.maze[cell]
        if air_directions[moving_direction] == 1:
            if moving_direction == north:
                cell = (cell[0]-1, cell[1])
            if moving_direction == east:
                cell = (cell[0], cell[1]+1)
            if moving_direction == south:
                cell = (cell[0]+1, cell[1])
            if moving_direction == west:
                cell = (cell[0], cell[1]-1)
            return True, cell
        return False, cell

    def where_is_right(self, moving_direction):
        if moving_direction == north:
            return east 
        if moving_direction == east:
            return south
        if moving_direction == south:
            return west
        if moving_direction == west:
            return north

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = east

        while cell != (self.maze_size-1,self.maze_size-1):
            print(cell)

            moved, cell = self.try_right(cell, moving_direction)
            if moved:
                moving_direction = self.where_is_right(moving_direction)
            


            if moving_direction == south:
                moved, cell = self.move_down(cell)
                if not moved:
                    moving_direction = self.where_is_right(moving_direction)
                    continue
                
                 
            if moving_direction == east:
                moved, cell = self.move_right(cell)
                if not moved:
                    moving_direction = self.where_is_right(moving_direction)
                    continue

            if moving_direction == north:
                moved, cell = self.move_up(cell)
                if not moved:
                    moving_direction = self.where_is_right(moving_direction)
                    continue

            if moving_direction == west:
                moved, cell = self.move_left(cell)
                if not moved:
                    moving_direction = self.where_is_right(moving_direction)
                    continue
        
        


if __name__ == "__main__":

    a = WallFollower(3)
    a.solve_maze()