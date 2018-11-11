import networkx as nx


class GraphAnalyzer:
    def __init__(self, graph):
        self.__graph = graph

    def analyze(self):
        print(type(self.__graph))

