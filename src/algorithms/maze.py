import random
import time


class Maze:
    "Luokka, joka luo syklittömän, neliön labyrintin Kruskallin algoritmilla"

    def __init__(self, size):
        """Luokan konstuktori, joka alustaa labyrintin luomisesta vastaavan palvelun.

        Args:
            size (int): Luotavan neliön labyrintin sivun koko.
        """
        self.maze_size = size
        self.graph = {}
        self.graph_edges = []
        self.disjoint_set = {}
        self.solution = []
        self.air_directed_maze = {}
        self.elapsed_time = 0

        self.maze_by_kruskal()

    def maze_by_kruskal(self):
        """Kruskalin algortmi, joka luo syklittömän labyrintin.
        """
        start_time = time.time()
        for x in range(0, self.maze_size):
            for y in range(0, self.maze_size):
                node = (x, y)
                self.graph[node] = []

        for node in self.graph:
            x, y = node
            neighbours = []

            if x > 0:
                neighbours.append((x - 1, y))
            if x < self.maze_size - 1:
                neighbours.append((x + 1, y))
            if y > 0:
                neighbours.append((x, y - 1))
            if y < self.maze_size - 1:
                neighbours.append((x, y + 1))
            self.graph[node] = neighbours

        for element in self.graph:
            self.disjoint_set[element] = element

        for node in self.graph:
            neighbours = self.graph[node]
            for neighbour in neighbours:
                if (
                    node, neighbour) not in\
                    self.graph_edges and\
                    (neighbour, node) not in\
                    self.graph_edges:
                    self.graph_edges.append((node, neighbour)
                    )

        while (len(self.solution) < (len(self.graph) - 1)):
            rnd_edge = random.choice(self.graph_edges)
            node1, node2 = rnd_edge
            set1 = self._find(node1)
            set2 = self._find(node2)

            if set1 != set2:
                self._union(node1, node2)
                self.solution.append(rnd_edge)

                self.graph_edges.remove(rnd_edge)

        end_time = time.time()
        self.count_time(start_time, end_time)

        self.maze_in_air_directions(self.solution)

    def _find(self, element):
        if self.disjoint_set[element] == element:
            return element

        return self._find(self.disjoint_set[element])

    def _union(self, element1, element2):
        _set1 = self._find(element1)
        _set2 = self._find(element2)
        self.disjoint_set[_set1] = _set2

    def maze_in_air_directions(self, maze):
        """Käy läpi Kruskalin luoman ratkaisun ja muodostaa niistä
            avain=solu + arvo=tuple(0,0,0,0) pareja, jossa on tieto
            mihin ilman suuntaan solusta on pääsy.
            (north,east,south,west) 0=ei pääsyä, 1=pääsy.

        Args:
            maze (list): Kruskalin luoma labyrintti.

        Returns:
            dict: Palauttaa sanakirjan, jossa jokaisesta labyrintin
                  solusta löytyy tieto mihin ilmansuuntaan on pääsy.
        """

        for x in range(self.maze_size):
            for y in range(self.maze_size):
                self.air_directed_maze[(x, y)] = (0, 0, 0, 0)

        for edge in maze:
            x = (edge[1][0]-edge[0][0])

            if x == 1:  # solusta pääsee alas
                north = self.air_directed_maze[edge[0]][0]
                east = self.air_directed_maze[edge[0]][1]
                south = 1
                west = self.air_directed_maze[edge[0]][3]
                self.air_directed_maze[edge[0]] = (
                    north, east, south, west)  # solusta pääsee alas
                # solusta pääsee ylös
                north = 1
                east = self.air_directed_maze[edge[1]][1]
                south = self.air_directed_maze[edge[1]][2]
                west = self.air_directed_maze[edge[1]][3]
                # solusta pääsee ylös
                self.air_directed_maze[edge[1]] = (north, east, south, west)

            y = (edge[1][1]-edge[0][1])
            if y == 1:  # solusta pääsee oikealle
                north = self.air_directed_maze[edge[0]][0]
                east = 1
                south = self.air_directed_maze[edge[0]][2]
                west = self.air_directed_maze[edge[0]][3]

                self.air_directed_maze[edge[0]] = (
                    north, east, south, west)  # solusta pääsee oikealle

                north = self.air_directed_maze[edge[1]][0]
                east = self.air_directed_maze[edge[1]][1]
                south = self.air_directed_maze[edge[1]][2]
                # solusta pääsee vasemmalle
                west = 1
                self.air_directed_maze[edge[1]] = (north, east, south, west)

        return self.air_directed_maze

    def count_time(self, start_time, end_time):
        """Laskee labyrintin muodostamiseen kuluneen ajan.

        Args:
            start_time (float): Ratkaisun aloitusaika.
            end_time (float): Ratkaisun valmistumisaika.
        """
        elapsed_time = f"{end_time-start_time:.5f}"
        self.elapsed_time = elapsed_time
