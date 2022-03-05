'''
Given a directed graph, design an algorithm to find out whether there is
a route between two nodes
'''

'''
APPROACH
- we can use either BFS or DFS in order to traverse through the graph
- use a visited set to avoid cycles and repetition of nodes
'''


def bfs_find_route(node1, node2):
    queue = Queue()
    path_found = None
    node = node1
    node.shortest_path = [node]
    all_visited_nodes = [node]

    while node:
        for adjacent in node.adjacency_list:
            if adjacent.shortest_path is None:
                adjacent.shortest_path = node.shortest_path + [adjacent]
                if adjacent == node2:
                    path_found = node.shortest_path + [adjacent]
                    break
                queue.add(adjacent)
                all_visited_nodes.append(adjacent)
        node = queue.remove()
    for visited in all_visited_nodes:
        visited.shortest_path = None
    return path_found


class Node():
    def __init__(self, data, adjacency_list=None) -> None:
        self.data = data
        self.adjacency_list = adjacency_list or []
        self.shortest_path = None

    def add_edge_to(self, node):
        self.adjacency_list += [ node ]

    def __str__(self):
        return self.data


class Queue():
    def __init__(self) -> None:
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item

    def is_empty(self):
        return len(self.array) == 0
