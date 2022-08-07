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
        if air_directions[south] == 1:
            cell = (cell[0]+1, cell[1])
            return 0, cell
        return 1, cell

    def move_right(self, cell):
        air_directions = self.maze[cell]
        if air_directions[east]:
            cell = (cell[0], cell[1]+1)
            return (0, cell)
        return (2, cell)

    def move_up(self, cell):
        air_directions = self.maze[cell]
        if air_directions[north]:
            cell = (cell[0]-1, cell[1])
            return (1, cell)
        return (3, cell)

    def move_left(self, cell):
        air_directions = self.maze[cell]
        if air_directions[west]:
            cell = (cell[0]-1, cell[1])
            return (2, cell)
        return ()

    def solve_maze(self):
        start = 0,0
        cell = start
        moving_direction = 0
        while cell != (self.maze_size-1,self.maze_size-1):

            if moving_direction == 0:
                moving_direction, cell = self.move_down(cell)
                continue
            
            if moving_direction == 1:
                moving_direction, cell = self.move_right(cell)
                continue

            if moving_direction == 2:
                moving_direction, cell = self.move_up(cell)
                continue

            if moving_direction == 3:
                moving_direction, cell = self.move_left(cell)
                continue
        
        


if __name__ == "__main__":

    a = WallFollower(3)
    a.solve_maze()