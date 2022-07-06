from Component import Component
from ComponentType import ComponentType
from Node import Node

class Resistance(Component):
    def __init__(self, n1: Node, n2: Node, resistance: float) -> None:
        super().__init__(ComponentType.resistance, n1, n2)
        self._resistance = resistance

    def getResistance(self) -> float:
        return self._resistance