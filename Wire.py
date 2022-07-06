from Component import Component
from ComponentType import ComponentType
from Node import Node

class Wire(Component):
    def __init__(self, n1: Node, n2: Node) -> None:
        super().__init__(ComponentType.wire, n1, n2)