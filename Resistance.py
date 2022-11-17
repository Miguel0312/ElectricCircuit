from Component import Component
from ComponentType import ComponentType
from Node import Node

class Resistance(Component):
    def __init__(self, n1: Node, n2: Node, resistance: float = 1) -> None:
        super().__init__(ComponentType.resistance, n1, n2)
        self._resistance = resistance

    def getResistance(self) -> float:
        return self._resistance
    
    def setResistance(self, resistance: float) -> None:
        self._resistance = resistance

    def calculate(self, node: Node):
        if node == self._node1:
            if self._node2.getCalculated():
                self._node1.setTension(self._node2.getTension()-self._resistance*self._current)
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")
        if node == self._node2:
            if self._node1.getCalculated():
                self._node2.setTension(self._node1.getTension()+self._resistance*self._current)
            else:
                raise Exception("The tension of neither of the nodes has been calculated yet.")