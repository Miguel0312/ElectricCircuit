class Node:
    currentID = 0

    def __init__(self) -> None:
        self._id = Node.currentID
        Node.currentID += 1
        self._tension = 0

    def getTension(self) -> float:
        return self._tension

    def setTension(self, tension: float) -> None:
        self._tension = tension

    def getID(self) -> int:
        return self._id

    def __str__(self) -> str:
        return str(self._id)

    def __lt__(self, n2):
        return self.getID() < n2.getID()