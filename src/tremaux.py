from explore import Explore
import math
from maze import Maze
import random
import time

north = 0
east = 1
south = 2
west = 3

class Tremaux:
    """Luokka joka vastaa labyrintin ratkaisusta Tremaux-algoritmilla,
        joka merkitsemällä kulkemansa reitin löytää reitin ulos. Kaksi kertaa
        merkattulle reitille ei enään mennä.
    """
    def __init__(self, maze):
        """Luokan konstruktori, joka luo Treamaux-algoritmista vastaavan
           palvelun.

        Args:
            maze (dict): Labyrintti sanakirjassa, avaimena solut jotka sisältävät
                        tuplen (0,0,0,0) (north,east,south,west) nolla=seinä,
                        1=pääsy.
        """
        self.maze = maze
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        self.explore = Explore(self.maze)
        self.elapsed_time = None
        self.visited = []
        self.visited_twice = []
        self.elapsed_time = None

        self.solve_maze()

    def solve_maze(self):
        """Ratkaisee labyrintin, alkupisteenä vasen yläkulma ja loppupisteenä
           oikea alakulma.
        """

        start = 0,0
        cell = start
        moving_direction = east
        start_time = time.time()

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
        end_time = time.time()
        self.count_time(start_time, end_time)

    def not_visited_directions(self, cell, moving_direction):
        """Tarkistaa onko solusta reittejä, joilla algoritmi ei ole vielä vieraillut.

        Args:
            cell (tuple): Solu jossa algoritmi on.
            moving_direction (int): Etenemissuunta.

        Returns:
            list: Palauttaa suunnat, joissa algorimti ei ole vielä käynyt.
        """
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
        """Tarkistaa onko solusta reittejä, joilla algoritmi on  vieraillut jo kerran.

        Args:
            cell (tuple): Solu jossa algoritmi on.
            moving_direction (int): Etenemissuunta.

        Returns:
            list: Palauttaa suunnat, joissa algorimti on käynyt kerran.
        """
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

    def count_time(self, start_time, end_time):
        """Laskee labyrintin ratkaisuun kuluneen ajan.

        Args:
            start_time (float): Ratkaisun aloitusaika.
            end_time (float): Ratkaisun valmistumisaika.
        """
        elapsed_time = "{0:.5f}".format(end_time-start_time)
        self.elapsed_time = elapsed_time