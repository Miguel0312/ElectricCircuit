from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt
from ComponentType import ComponentType
from Grid import Grid
from math import cos, radians, sin

class GridComponent(QLabel):
  def __init__(self, container: Grid, type: ComponentType, x: int, y: int, angle: int):
    self.angle = angle
    self.x = x
    self.y = y
    
    self.neighbours = []
    path = "./assets/"

    if type == ComponentType.wire:
      path += "Wire"
    elif type == ComponentType.resistance:
      path += "Resistance"
    elif type == ComponentType.generator:
      path += "Generator"

    super().__init__(container, text="YES")

    self.image = QPixmap(path)
    self.image = self.image.scaled(64, 64)
    self.image = self.image.transformed(QTransform().rotate(self.angle))
    self.setPixmap(self.image)
    self.move(x-32, y-32)

    self.node1 = [x + 32*cos(radians(self.angle)), y + 32*sin(radians(self.angle))]
    self.node2 = [x - 32*cos(radians(self.angle)), y - 32*sin(radians(self.angle))]

    self.show()