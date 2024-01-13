import typing

from GraphClass import (Distances, Graph, GraphClass, Node, Paths,
                        ProcessedGraph)

# type SomeType = tuple[dict[Node, int | float], dict[Node, list[Node]]]


class ChannelState(typing.NamedTuple):
    volume: float
    active: bool


my_graph: Graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph: Graph, start: str, target: str = "") -> ProcessedGraph:
    new_graph: GraphClass = GraphClass(graph, start, target)

    # cleaning up
    distances: Distances = new_graph.distances
    paths: Paths = new_graph.paths
    unvisited = new_graph.unvisited

    while unvisited:
        current: Node = min(unvisited, key=distances.get)  # type: ignore
        for node, distance in graph[current]:
            # logics(distance, distances, node, current)
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    print_graph(new_graph)

    return distances, paths


def print_graph(new_graph: GraphClass) -> None:
    targets_to_print: list[Node] | Graph = (
        [new_graph.target] if new_graph.target else new_graph.graph
    )
    for node in targets_to_print:
        if node == new_graph.start:
            continue
        print(f'\n{new_graph.start}-{node} distance: {new_graph.distances[node]}\nPath: {" -> ".join(new_graph.paths[node])}')  # type: ignore


shortest_path(my_graph, "A", "F")
