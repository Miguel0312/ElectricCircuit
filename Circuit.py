from importlib.resources import path
from Component import Component
from Node import Node
from Path import Path

class Circuit:
    def __init__(self):
        self._nodes = []
        self._components = []

    def addNode(self, n: Node) -> None:
        self._nodes.append(n)
    
    def addComponent(self, c: Component) -> None:
        self._components.append(c)

    def getNodes(self) -> list[Node]:
        return self._nodes

    def getComponents(self) -> list[Component]:
        return self._components

    def getCycles(self) -> list[Node]:
        cycles = []
        for edge in self._components:
            for node in edge.getNodes():
                p = Path()
                p.nodes.append(node)
                self.findNewCycles(p, cycles)
        return cycles

    def findNewCycles(self, path: Path, cycles: list[Path]) -> None:
        start_node = path.nodes[0]
        next_node= None
        sub = []

        #visit each edge and each node of each edge
        for component in self._components:
            node1, node2 = component.getNodes()
            if start_node in [node1, node2]:
                    if node1 == start_node:
                        next_node = node2
                    else:
                        next_node = node1
                    if not path.visited(next_node):
                            # neighbor node not on path yet
                            sub = Path()
                            sub.addSegment(next_node, component)
                            sub.extend(path)
                            # explore extended path
                            self.findNewCycles(sub, cycles);
                    elif len(path.nodes)>1 and next_node == path.nodes[-1]:
                            sub = Path()
                            sub.addSegment(next_node, component)
                            sub.extend(path)
                            repeat = False
                            for c in sub.components:
                                if sub.components.count(c) != 1:
                                    repeat = True
                            if sub.isNew(cycles) and not repeat:
                                cycles.append(sub)
