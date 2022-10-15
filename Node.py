from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Circuit import Circuit

class Node:
    currentID = 0

    def __init__(self, circuit: "Circuit") -> None:
        self._id = Node.currentID
        Node.currentID += 1
        self._tension = 0
        self._circuit = circuit
        circuit.addNode(self)
        self._tension = 0
        self._calculated = False

    def getTension(self) -> float:
        return self._tension

    def setTension(self, tension: float) -> None:
        self._tension = tension

    def getID(self) -> int:
        return self._id

    def setTension(self, tension: float) -> None:
        if not self._calculated:
            self._tension = tension

    def getCurrent(self) -> float:
        if self._calculated:
            return self._tension
        raise Exception("Tension of this node hasn't been calculated yet")

    def setCalculated(self, calculated: bool) -> None:
        self._calculated = calculated

    def getCalculated(self) -> bool:
        return self._calculated

    def __str__(self) -> str:
        return str(self._id)

    def __lt__(self, n2: "Node"):
        return self.getID() < n2.getID()