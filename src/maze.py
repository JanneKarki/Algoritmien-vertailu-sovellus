
"Luo labyrintin"

import random

maze_size = 5
graph = {}
graph_edges = []


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
    

for node in graph.keys():
    neighbours = graph[node]
    for neighbour in neighbours:
        if(node, neighbour) not in graph_edges and (neighbour, node) not in graph_edges:
            graph_edges.append((node, neighbour))
            
print(graph)
print()
print(graph_edges)

