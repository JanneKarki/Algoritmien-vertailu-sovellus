north = 0
east = 1
south = 2
west = 3

class Explore:
    """Luokka, joka vastaa labyrintissä liikkumisesta.
    """
    def __init__(self, maze):
        """Luokan konstruktori, joka luo labyrintin liikkumisesta vastaavan palvelun.

        Args:
            maze (_type_): maze (dict): Labyrintti sanakirjassa, avaimena solut jotka sisältävät
                            tuplen (0,0,0,0) (north,east,south,west) nolla=seinä,
                            1=pääsy.
        """
        self.maze = maze


    def no_wall_in_front(self, cell, moving_direction):
        """Tarkistaa, ettei edessä ole seinää.

        Args:
            cell (tuple): Sijainti.
            moving_direction (int): Etenemissuunta.

        Returns:
            boolean: Palauttaa True, jos edessä ei ole seinää,
                muuten False.
        """
        air_directions = self.maze[cell]
        if air_directions[moving_direction] == 1:  
            return True
        return False    
    
    def try_right(self, cell, moving_direction):
        """Tarkistaa, ettei oikealla ole seinää.

        Args:
            cell (tuple): Sijainti.
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Palauttaa True, jos oikealla ei ole seinää,
                muuten False.
        """
        air_directions = self.maze[cell]
        right = self.turn_where_is_right(moving_direction)
        if air_directions[right] == 1:  
            return True
        return False

    def turn_around(self, moving_direction):
        """Kääntää etenemissuunnan päinvastaiseen suuntaan.

        Args:
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Palauttaa vastakkaisen suunnnan.
        """
        if moving_direction == north:
            return south
        if moving_direction == south:
            return north
        if moving_direction == east:
            return west
        if moving_direction == west:
            return east

    def try_left(self, cell, moving_direction):
        """Tarkistaa, ettei vasemmalla ole seinää.

        Args:
            cell (tuple): Sijainti.
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Palauttaa True, jos vasemmalla ei ole seinää,
                muuten False.
        """
        air_directions = self.maze[cell]
        right = self.turn_where_is_left(moving_direction)
        if air_directions[right] == 1:  
            return True
        return False

    def turn_where_is_right(self, moving_direction):
        """Kääntää etenemissuunnan oikealle.

        Args:
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Oikealle kääntynyt etenemissuunta.
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
        """Kääntää etenemissuunnan vasemmalle.

        Args:
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Vasemmalle kääntynyt etenemissuunta.
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
        """Etenee yhden ruudun eteenpäin.

        Args:
            cell (tuple): Sijainti.
            moving_direction (int): Etenemissuunta.

        Returns:
            tuple: Palauttaa uuden sijainnin, etenemisen jälkeen.
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