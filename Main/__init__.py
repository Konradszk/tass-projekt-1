from .GraphLoader import GraphLoader
from .GraphAnalyzer import GraphAnalyzer


def main():
    gl = GraphLoader('./celegansneural.gml')
    gl.load_undirected_graph()
    ga = GraphAnalyzer(gl.graph)
    ga.analyze()
