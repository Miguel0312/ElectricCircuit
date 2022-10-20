from Component import Component
from ComponentType import ComponentType
from Node import Node

class Wire(Component):
    def __init__(self, n1: Node, n2: Node) -> None:
        super().__init__(ComponentType.wire, n1, n2)

    def calculate(self, node: Node):
        if node == self._node1:
            if self._node2.getCalculated():
                self._node1.setTension(self._node2.getTension())
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")
        if node == self._node2:
            if self._node1.getCalculated():
                self._node2.setTension(self._node1.getTension())
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")