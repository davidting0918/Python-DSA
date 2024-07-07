class Graph:
    def __init__(self):
        self.adj_list = {}

    def print(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True

    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError as e:
            pass
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False

        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)
        self.adj_list.pop(vertex)
        return True