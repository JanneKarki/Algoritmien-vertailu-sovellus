NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


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
        if moving_direction == NORTH:
            return SOUTH
        if moving_direction == SOUTH:
            return NORTH
        if moving_direction == EAST:
            return WEST
        else: # moving direction == west
            return EAST

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
        if moving_direction == NORTH:
            return EAST
        if moving_direction == EAST:
            return SOUTH
        if moving_direction == SOUTH:
            return WEST
        else: # moving_direction == west
            return NORTH

    def turn_where_is_left(self, moving_direction):
        """Kääntää etenemissuunnan vasemmalle.

        Args:
            moving_direction (int): Etenemissuunta.

        Returns:
            int: Vasemmalle kääntynyt etenemissuunta.
        """
        if moving_direction == NORTH:
            return WEST
        if moving_direction == EAST:
            return NORTH
        if moving_direction == SOUTH:
            return EAST
        else: # moving_direction == west
            return SOUTH

    def move_forward(self, cell, moving_direction):
        """Etenee yhden ruudun eteenpäin.

        Args:
            cell (tuple): Sijainti.
            moving_direction (int): Etenemissuunta.

        Returns:
            tuple: Palauttaa uuden sijainnin, etenemisen jälkeen.
        """
        if moving_direction == NORTH:
            cell = (cell[0]-1, cell[1])
        if moving_direction == EAST:
            cell = (cell[0], cell[1]+1)
        if moving_direction == SOUTH:
            cell = (cell[0]+1, cell[1])
        if moving_direction == WEST:
            cell = (cell[0], cell[1]-1)
        return cell
