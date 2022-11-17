from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt
from GridComponent import GridComponent
from Circuit import Circuit
from Footer import Footer

class Grid(QWidget):
  def __init__(self, gridComponents: list[GridComponent], footer: Footer):
    super().__init__()
    self.gridComponents = gridComponents
    self.footer = footer
    self.setFocusPolicy(Qt.StrongFocus)
    self.setMouseTracking(True)
    self.setAutoFillBackground(True)
    self.setAcceptDrops(True)
    self.circuit = Circuit()

  def mousePressEvent(self, event: QMouseEvent):
    if event.button() == Qt.LeftButton:
      x = event.pos().x()
      y = event.pos().y()
      for gridComponent in self.gridComponents:
        left = min(gridComponent.node1.position[0], gridComponent.node2.position[0])
        right = max(gridComponent.node1.position[0], gridComponent.node2.position[0])
        top = min(gridComponent.node1.position[1], gridComponent.node2.position[1])
        bottom = max(gridComponent.node1.position[1], gridComponent.node2.position[1])
        if gridComponent.angle%180==0 and x >= left and x <= right and abs(y-gridComponent.node1.position[1]) <= 10:
          self.setCursor(Qt.PointingHandCursor)
          # Display current direction and absolute value instead of value
          self.footer.setComponent(gridComponent.component)
          return
        if gridComponent.angle%180 == 90 and y >= top and y <= bottom and abs(x-gridComponent.node1.position[0]) <= 10:
          self.setCursor(Qt.PointingHandCursor)
          self.footer.setComponent(gridComponent.component)
          return

  def mouseMoveEvent(self, event: QMouseEvent):
    x = event.pos().x()
    y = event.pos().y()
    for gridComponent in self.gridComponents:
      left = min(gridComponent.node1.position[0], gridComponent.node2.position[0])
      right = max(gridComponent.node1.position[0], gridComponent.node2.position[0])
      top = min(gridComponent.node1.position[1], gridComponent.node2.position[1])
      bottom = max(gridComponent.node1.position[1], gridComponent.node2.position[1])
      if gridComponent.angle%180==0 and x >= left and x <= right and abs(y-gridComponent.node1.position[1]) <= 10:
        self.setCursor(Qt.PointingHandCursor)
        return
      if gridComponent.angle%180 == 90 and y >= top and y <= bottom and abs(x-gridComponent.node1.position[0]) <= 10:
        self.setCursor(Qt.PointingHandCursor)
        return
    self.setCursor(Qt.ArrowCursor)