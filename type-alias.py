import typing
from typing import TypeAlias

# modo 1
NamedTuple = tuple[str, int]

# modo 2
Node: TypeAlias = str
Graph: TypeAlias = dict[Node, list[tuple[Node, int]]]
ProcessedGraph: TypeAlias = tuple[dict[Node, int | float], dict[Node, list[Node]]]

# modo 3
Key = str
Value = list[tuple]
my_graph2: dict[Key, Value] = {}

class Graph1(typing.NamedTuple):
    node: float
    distance: bool

Nod = tuple[Graph1]
NodesDict = list[Nod]