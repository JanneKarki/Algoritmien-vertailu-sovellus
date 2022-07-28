
"Luo labyrintin"

from sklearn import neighbors


size = 5
graph = dict()

for x in range (0, size):
    for y in range (0, size):
        node = (x,y)
        graph[node] = list()


print(graph)

