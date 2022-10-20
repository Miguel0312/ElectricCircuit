from Component import Component
from ComponentType import ComponentType
from Node import Node

class Generator(Component):
    def __init__(self, n1: Node, n2: Node, tension: float = 1) -> None:
        super().__init__(ComponentType.generator, n1, n2)
        self._tension = tension

    def getTension(self) -> float:
        return self._tension

    def calculate(self, node: Node):
        if node == self._node1:
            if self._node2.getCalculated():
                self._node1.setTension(self._node2.getTension()-self._tension)
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")
        if node == self._node2:
            if self._node1.getCalculated():
                self._node2.setTension(self._node1.getTension()+self._tension)
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")