from Component import Component
from ComponentType import ComponentType
from Node import Node

class Generator(Component):
    def __init__(self, n1: Node, n2: Node, tension: float = 1) -> None:
        super().__init__(ComponentType.generator, n1, n2)
        self._tension = tension

    def getTension(self) -> float:
        return self._tension