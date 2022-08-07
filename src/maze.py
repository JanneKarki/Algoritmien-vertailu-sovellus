
"Luo labyrintin"

import random

class Maze:

    def __init__(self):
        self.maze_size = 10
        self.graph = {}
        self.graph_edges = []
        self.disjoint_set = {}
        self.solution = []

    def maze_by_kruskal(self):
        for x in range (0, self.maze_size):
            for y in range (0, self.maze_size):
                node = (x,y)
                self.graph[node] = []

        for node in self.graph.keys():
            x,y = node
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
            

        for element in self.graph.keys():
            self.disjoint_set[element] = element

        for node in self.graph.keys():
            neighbours = self.graph[node]
            for neighbour in neighbours:
                if(node, neighbour) not in self.graph_edges and (neighbour, node) not in self.graph_edges:
                    self.graph_edges.append((node, neighbour))


        while (len(self.solution) < (len(self.graph.keys()) - 1)):
            rnd_edge = random.choice(self.graph_edges)
            node1, node2 = rnd_edge
            set1 = self._find(node1)
            set2 = self._find(node2)
                    
            if (set1 != set2):
                self._union(node1, node2)
                self.solution.append(rnd_edge)

                self.graph_edges.remove(rnd_edge)

        return self.solution

    def _find(self, element):
        if self.disjoint_set[element] == element:
            return element
        else:
            return self._find(self.disjoint_set[element])

    def _union(self, element1, element2):
        _set1 = self._find(element1)
        _set2 = self._find(element2)
        self.disjoint_set[_set1] = _set2
    
    def maze_in_air_directions(self):
        air_directions = {}
        "0,1,2,3"
        "N,E,S,W"
        for x in range(self.maze_size):
            for y in range(self.maze_size):
                air_directions[(x,y)] = (0,0,0,0)
        for edge in self.solution:
            y = (edge[1][0]-edge[0][0])
            if y == 1: #solusta pääsee alas
                north = air_directions[edge[0]][0]
                east = air_directions[edge[0]][1]
                south = air_directions[edge[0]][2]+y
                west = air_directions[edge[0]][3]
                air_directions[edge[0]] = (north,east,south,west) #solusta pääsee alas
                air_directions[edge[1]] = (north+1,east,south,west) #solusta pääsee ylös
            x = (edge[1][1]-edge[0][1])
            if x == 1: #solusta pääsee oikealle
                north = air_directions[edge[0]][0]
                east = air_directions[edge[0]][1]+x
                south = air_directions[edge[0]][2]
                west = air_directions[edge[0]][3]

                air_directions[edge[0]] = (north,east,south,west) #solusta pääsee oikealle
                air_directions[edge[1]] = (north,east,south,west+1) #solusta pääsee vasemmalle
        print(air_directions)    


maze = Maze()

if __name__ == "__main__":
    a = Maze()
    a.maze_by_kruskal()
    a.maze_in_air_directions()
    print(a.solution)