from PySide6.QtWidgets import QWidget


class Grid(QWidget):
  def __init__(self):
    super().__init__()
    self.setAutoFillBackground(True)
    self.setAcceptDrops(True)
