from math import cos, radians, sin
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QTransform, QMouseEvent
from PySide6.QtCore import Qt
from ComponentType import ComponentType
from Grid import Grid
from GridComponent import GridComponent

class ComponentIcon(QLabel):
  def __init__(self, type: ComponentType, grid: Grid, components: list[GridComponent]):
    self.grid = grid
    self.path = "./assets/"
    self.components = components

    if type == ComponentType.wire:
      self.path += "Wire"
    elif type == ComponentType.resistance:
      self.path += "Resistance"
    elif type == ComponentType.generator:
      self.path += "Generator"

    self.type = type
    self.image = QPixmap(self.path)
    self.image = self.image.scaled(64, 64)

    super().__init__()
    self.setPixmap(self.image)
  
    self.setFocusPolicy(Qt.StrongFocus)

  def mousePressEvent(self, event: QMouseEvent):
    if event.button() == Qt.LeftButton:
        self.setCursor(Qt.ClosedHandCursor)
        # This will give us the start position when a drag is triggered
        self.drag_start_pos = event.pos()
        self.clone = QLabel(parent=self.grid)
        self.clone.angle = 0
        self.clone.setPixmap(self.image)
        x = (event.pos() + self.pos() - self.grid.pos()).x() - 32
        y = (event.pos() + self.pos() - self.grid.pos()).y() - 32
        self.clone.move(x, y)
        self.clone.show()

    super().mousePressEvent(event)

  def mouseMoveEvent(self, event: QMouseEvent):
    x = (event.pos() + self.pos() - self.grid.pos()).x()
    y = (event.pos() + self.pos() - self.grid.pos()).y()

    node1Position = [x + 32*cos(radians(self.clone.angle)), y + 32*sin(radians(self.clone.angle))]
    node2Position = [x - 32*cos(radians(self.clone.angle)), y - 32*sin(radians(self.clone.angle))]

    for c in self.components:
      for node in [node1Position, node2Position]:
        for destNode in [c.node1, c.node2]:
          if(pow(node[0] - destNode.position[0], 2) + pow(node[1] - destNode.position[1], 2) <= 80):
            x = destNode.position[0] + (node1Position[0] + node2Position[0] - 2*node[0])/2
            y = destNode.position[1] + (node1Position[1] + node2Position[1] - 2*node[1])/2
            if node == node1Position:
              node1 = destNode
            elif node == node2Position:
              node2 = destNode


    self.clone.move(x-32, y-32)
    super().mouseMoveEvent(event)

  def mouseReleaseEvent(self, event: QMouseEvent):
    self.setCursor(Qt.ArrowCursor)
    self.drag_start_pos = None

    x = (event.pos() + self.pos() - self.grid.pos()).x()    
    y = (event.pos() + self.pos() - self.grid.pos()).y()

    node1Position = [x + 32*cos(radians(self.clone.angle)), y + 32*sin(radians(self.clone.angle))]
    node2Position = [x - 32*cos(radians(self.clone.angle)), y - 32*sin(radians(self.clone.angle))]
    node1 = None
    node2 = None

    for c in self.components:
      for node in [node1Position, node2Position]:
        for destNode in [c.node1, c.node2]:
          if(pow(node[0] - destNode.position[0], 2) + pow(node[1] - destNode.position[1], 2) <= 80):
            x = destNode.position[0] + (node1Position[0] + node2Position[0] - 2*node[0])/2
            y = destNode.position[1] + (node1Position[1] + node2Position[1] - 2*node[1])/2
            if node == node1Position:
              node1 = destNode
            elif node == node2Position:
              node2 = destNode

    self.components.append(GridComponent(self.grid, self.type, x, y, self.clone.angle, node1, node2))

    self.clone.deleteLater()

    super().mouseReleaseEvent(event)

  def keyPressEvent(self, event: QMouseEvent):
    if not event.isAutoRepeat() and event.key() == Qt.Key_R and self.drag_start_pos != None:
      self.clone.angle = (self.clone.angle + 90) % 360
      self.clone.setPixmap(self.image.transformed(QTransform().rotate(self.clone.angle)))
    return super().keyPressEvent(event)
