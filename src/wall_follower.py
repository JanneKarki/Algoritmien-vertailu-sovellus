from PIL import Image, ImageDraw
import math
import time

north = 0
east = 1
south = 2
west = 3

class WallFollower:
    """Luokka joka vastaa labyrintin ratkaisusta Wall-Follower algoritmilla,
    joka oikean puoleista seinää seuraamalla, löytää ratkaisun.
    """
    def __init__(self, maze):
        """Luokan konstruktorin joka luo Wall-Follower-Algoritmista vastaavan
           palvelun.

        Args:
            maze (dict): Labyrintti sanakirjassa, avaimena solut jotka sisältävät
                        tuplen (0,0,0,0) (north,east,south,west) nolla=seinä,
                        1=pääsy.
        """
        self.maze = maze
        self.solution = []
        self.maze_size = math.sqrt(len(self.maze))
        self.wall_thickness = 6
        self.cell_thickness = 20
        self.total_cell_thickness = 26
        self.cell_center = 13
        self.elapsed_time = None
        

    def no_wall_in_front(self, cell, moving_direction):
        """Tarkistaa onko edessä seinää. Jos on, palauttaa False, muuten True.

        Args:
            cell (tuple): Solu jossa algoritmi on etenemässä.
            moving_direction (int): Suunta johon ollaan kulkemassa.

        Returns:
            boolean: Palauttaa True, jos edessä ei ole seinää, muuten False.
        """
        air_directions = self.maze[cell]
        if air_directions[moving_direction] == 1:  
            return True
        return False    
    
    def try_right(self, cell, moving_direction):
        """Tarkistaa voko solusta kääntyä oikealle.

        Args:
            cell (tuple): Solu jossa algorimti on etenemässä.
            moving_direction (int): Suunta, johon ollaan kulkemassa.

        Returns:
            Boolean: Palauttaa True, jos oikealle voi kulkea, muuten palauttaa False.
        """
        air_directions = self.maze[cell]
        right = self.turn_where_is_right(moving_direction)
        if air_directions[right] == 1:  
            return True
        return False

    def turn_where_is_right(self, moving_direction):
        """Palauttaa ilmansuunnan, joka on kulkusuunnasta oikealla.

        Args:
            moving_direction (int): Suunta, johon ollaan kulkemassa.

        Returns:
            int: Palauttaa kulkusuunnasta oikealla olevan ilmansuunnan. 
        """
        if moving_direction == north:
            return east 
        if moving_direction == east:
            return south
        if moving_direction == south:
            return west
        if moving_direction == west:
            return north

    def turn_where_is_left(self, moving_direction):
        """Palauttaa ilmansuunnan, joka on kulkusuunnasta vasemmalla.

        Args:
            moving_direction (int): Suunta, johon ollaan kulkemassa.

        Returns:
            int: Palauttaa kulkusuunnasta vasemmalla olevan ilmansuunnan.
        """
        if moving_direction == north:
            return west 
        if moving_direction == east:
            return north
        if moving_direction == south:
            return east
        if moving_direction == west:
            return south

    def move_forward(self, cell, moving_direction):
        """Siirtää algoritmin seuraavaan soluun.

        Args:
            cell (tuple): Solu, jossa nyt ollaan.
            moving_direction (int): Suunta johon ollaan etenemässä.

        Returns:
            tuple: Palauttaa solun johon siirryttiin.
        """
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
        """Ratkaisee labyrintin, alkupisteenä vasen yläkulma ja loppupisteenä
           oikea alakulma, ja mittaa siihen kuluneen ajan.
        """
        start = 0,0
        cell = start
        moving_direction = east
        start_time = time.time()
        end = (self.maze_size-1,self.maze_size-1)
        while cell != (end):
            
            if self.try_right(cell, moving_direction):
                moving_direction = self.turn_where_is_right(moving_direction)
                cell = self.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue

            if self.no_wall_in_front(cell, moving_direction):    
                cell = self.move_forward(cell, moving_direction)
                self.solution.append(cell)
                continue
            
            else:
                moving_direction = self.turn_where_is_left(moving_direction)
                continue

        end_time = time.time()
        last_step = (self.maze_size-1,self.maze_size-1)
        self.solution.append(last_step)
        self.count_time(start_time, end_time)

    def draw_solution(self):
        """Piirtää ratkaistun reitin labyrintin kuvaan.
        """
        self.adjust_solution_size()
        self.solve_maze()
        with Image.open("src/data/maze.png") as im:

            draw = ImageDraw.Draw(im)
            last_point = (0,0)
            for line in self.solution:
                draw.line(
                          fill="RGB(44,55,255)",
                          width=self.wall_thickness,
                          xy=[(last_point[1]*self.total_cell_thickness+self.cell_center,
                             last_point[0]*self.total_cell_thickness+self.cell_center),
                             (line[1]*self.total_cell_thickness+self.cell_center,
                             line[0]*self.total_cell_thickness+self.cell_center)
                             ]
                            )
                
                last_point = line
            im.save("src/data/solution.png")

    def adjust_solution_size(self):
        """Säätää piirrettävän ratkaisun kokoa labyrintin kokoa vastaavaksi.
        """
        if self.maze_size > 10:
            self.cell_thickness = int((10/self.maze_size)*20)
            self.wall_thickness = int((10/self.maze_size)*6)
            if self.wall_thickness < 1:
                self.wall_thickness = 1
            self.total_cell_thickness = round(self.cell_thickness+self.wall_thickness)
            self.cell_center = round(self.total_cell_thickness/2)
        else:
            self.cell_thickness = 20
            self.wall_thickness = 6

    def count_time(self, start_time, end_time):
        """Laskee labyrintin ratkaisuun kuluneen ajan.

        Args:
            start_time (float): Ratkaisun aloitusaika.
            end_time (float): Ratkaisun valmistumisaika.
        """
        elapsed_time = "{0:.5f}".format(end_time-start_time)
        self.elapsed_time = elapsed_time
