Node = str
Graph = dict[Node, list[tuple[Node, int]]]
Distances = dict[Node, int | float]
Paths = dict[Node, list[Node]]
ProcessedGraph = tuple[Distances, Paths]

class GraphClass:
    def __init__(self, graph: Graph, start: str, target: str = '') -> None:
        self.graph: Graph = graph
        self.start: str = start
        self.target: str = target
        self.distances: Distances = {node: 0 if node == start else float('inf') for node in graph}
        self.unvisited: list[Node] = list(graph)
        self.paths: Paths = {node: [] for node in graph}
        self.paths[start].append(start)