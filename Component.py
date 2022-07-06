from Node import Node
from ComponentType import ComponentType

class Component:
    def __init__(self, componentType: ComponentType, n1: Node, n2: Node) -> None:
        self._type = componentType
        self._node1 = n1
        self._node2 = n2

    def getNodes(self) -> list[Node]:
        return self.node1, self.node2
    
    def setNodes(self, n1: Node, n2: Node) -> None:
        self._node1 = n1
        self._node2 = n2

    def getType(self) -> ComponentType:
        return self._type

    def setType(self, componentType: ComponentType) -> None:
        self._type = componentType