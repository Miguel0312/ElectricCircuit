from Node import Node
from Component import Component

class Path:
    def __init__(self) -> None:
        self.nodes = []
        self.components = []

    def visited(self, node: Node) -> bool:
        return node in self.nodes

    def addSegment(self, node: Node, component: Component):
        self.nodes.append(node)
        self.components.append(component)

    def extend(self, path: "Path"):
        for node in path.nodes:
            self.nodes.append(node)
        for component in path.components:
            self.components.append(component)

    def __str__(self) -> str:
        for node in self.nodes:
            print(str(node))

    def isNew(self, cycles: list) -> bool:
        for path in cycles:
            if len(self.nodes) != len(path.nodes) or len(self.components) != len(path.components):
                continue

            hasSameNodes = True
            for node in self.nodes:
                if node not in path.nodes:
                    hasSameNodes = False
            for node in path.nodes:
                if node not in self.nodes:
                    hasSameNodes = False

            hasSameComponents = True
            for component in self.components:
                if component not in path.components:
                    hasSameComponents = False
            for component in path.components:
                if component not in self.components:
                    hasSameComponents = False
            
            if hasSameComponents and hasSameNodes:
                return False
            
        return True