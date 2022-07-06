from Component import Component
from Node import Node

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