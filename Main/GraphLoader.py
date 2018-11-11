import networkx as nx


class GraphLoader:
    def __init__(self, path):
        self.__path = path
        self.graph = None
        print('hello world')

    def load_gml(self):
        multi_graph = nx.read_gml(self.__path)
        return multi_graph

    def load_undirected_graph(self):
        self.graph = nx.Graph(self.load_gml()).to_undirected()
        print(type(self.graph))

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph):
        self.__graph = graph
