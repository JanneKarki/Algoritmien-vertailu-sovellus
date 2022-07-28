
"Luo labyrintin"

size = 5
graph = dict()

for x in range (0, size):
    for y in range (0, size):
        node = (x,y)
        graph[node] = list()

for node in graph.keys():
    x,y = node
    neighbours = list()

    if x > 0:
        neighbours.append((x - 1, y))

    if x < size - 1:
        neighbours.append((x + 1, y))

    if y > 0:
        neighbours.append((x, y - 1))

    if y < size - 1:
        neighbours.append((x, y + 1))
            
    graph[node] = neighbours   
    

print(graph)

