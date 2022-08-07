from maze import maze

class WallFollower:
    def __init__(self):
        self.maze = maze.maze_in_air_directions()
        self.solution = []
        print(self.maze)

a = WallFollower()