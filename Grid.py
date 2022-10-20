from PySide6.QtWidgets import QWidget
from Circuit import Circuit

class Grid(QWidget):
  def __init__(self):
    super().__init__()
    self.setAutoFillBackground(True)
    self.setAcceptDrops(True)
    self.circuit = Circuit()
