import math
import time
from functionalities.explore import EAST, Explore
from functionalities.visualization import Visualization


class WallFollower:
    """Luokka joka vastaa labyrintin ratkaisusta Wall-Follower algoritmilla,
    joka oikean puoleista seinää seuraamalla, löytää ratkaisun.
    """

    def __init__(self, maze):
        """Luokan konstruktori, joka luo Wall-Follower-Algoritmista vastaavan
           palvelun.

        Args:
            maze (dict): Labyrintti sanakirjassa, avaimena solut jotka sisältävät
                        tuplen (0,0,0,0) (north,east,south,west) nolla=seinä,
                        1=pääsy.
        """
        self.maze = maze
        self.explore = Explore(self.maze)
        self.visualization = Visualization()
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        self.elapsed_time = None

        self.solve_maze()

    def solve_maze(self):
        """Ratkaisee labyrintin, alkupisteenä vasen yläkulma ja loppupisteenä
           oikea alakulma, ja mittaa siihen kuluneen ajan.
        """
        start = 0, 0
        cell = start
        moving_direction = EAST
        start_time = time.time()
        end = (self.maze_size-1, self.maze_size-1)
        while cell != (end):

            if self.explore.try_right(cell, moving_direction):
                moving_direction = self.explore.turn_where_is_right(
                    moving_direction)
                cell = self.explore.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue

            if self.explore.no_wall_in_front(cell, moving_direction):
                cell = self.explore.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue

            moving_direction = self.explore.turn_where_is_left(
                moving_direction)
            continue

        end_time = time.time()

        self.count_time(start_time, end_time)
        self.visualization.draw_solution(
            self.solution, "wall_follower", self.maze_size)

    def count_time(self, start_time, end_time):
        """Laskee labyrintin ratkaisuun kuluneen ajan.

        Args:
            start_time (float): Ratkaisun aloitusaika.
            end_time (float): Ratkaisun valmistumisaika.
        """
        elapsed_time = f"{end_time-start_time:.5f}"
        self.elapsed_time = elapsed_time
