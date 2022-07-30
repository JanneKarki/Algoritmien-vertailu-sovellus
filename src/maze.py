
"Luo labyrintin"

import random

maze_size = 5
graph = {}
graph_edges = []
disjoint_set = {}
solution = []

def find(element):
    if disjoint_set[element] == element:
        return element
    else:
        return find(disjoint_set[element])

def union(element1, element2):
    _set1 = find(element1)
    _set2 = find(element2)
    disjoint_set[_set1] = _set2


for x in range (0, maze_size):
    for y in range (0, maze_size):
        node = (x,y)
        graph[node] = []

for node in graph.keys():
    x,y = node
    neighbours = []

    if x > 0:
        neighbours.append((x - 1, y))

    if x < maze_size - 1:
        neighbours.append((x + 1, y))

    if y > 0:
        neighbours.append((x, y - 1))

    if y < maze_size - 1:
        neighbours.append((x, y + 1))
            
    graph[node] = neighbours   
    

for element in graph.keys():
    disjoint_set[element] = element

for node in graph.keys():
    neighbours = graph[node]
    for neighbour in neighbours:
        if(node, neighbour) not in graph_edges and (neighbour, node) not in graph_edges:
            graph_edges.append((node, neighbour))


while (len(solution) < (len(graph.keys()) - 1)):
    rnd_edge = random.choice(graph_edges)
    node1, node2 = rnd_edge
    set1 = find(node1)
    set2 = find(node2)
            
    if (set1 != set2):
        union(node1, node2)
        solution.append(rnd_edge)

        graph_edges.remove(rnd_edge)



print(graph)
print()
print(graph_edges)
print()
print(solution, "solution")