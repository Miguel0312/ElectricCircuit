from Node import Node
from ComponentType import ComponentType

class Component:
    def __init__(self, componentType: ComponentType, n1: Node, n2: Node) -> None:
        self._type = componentType
        self._node1 = n1
        self._node2 = n2
        self._current = 0
        self._calculated = False

    def getNodes(self) -> list[Node]:
        return self._node1, self._node2
    
    def setNodes(self, n1: Node, n2: Node) -> None:
        self._node1 = n1
        self._node2 = n2

    def getType(self) -> ComponentType:
        return self._type

    def setType(self, componentType: ComponentType) -> None:
        self._type = componentType

    def setCurrent(self, current: float) -> None:
        if not self._calculated:
            self._current = current

    def getCurrent(self) -> float:
        if self._calculated:
            return self._current
        raise Exception("Current of this component hasn't been calculated yet")

    def setCalculated(self, calculated: bool) -> None:
        self._calculated = calculated

    def getCalculated(self) -> bool:
        return self._calculated