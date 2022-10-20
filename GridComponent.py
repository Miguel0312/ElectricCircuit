from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt
from Component import Component
from ComponentType import ComponentType
from Grid import Grid
from math import cos, radians, sin
from Node import Node
from Wire import Wire
from Resistance import Resistance
from Generator import Generator

class GridComponent(QLabel):
  def __init__(self, container: Grid, type: ComponentType, x: int, y: int, angle: int, node1: Node = None, node2: Node = None):
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

    node1Position = [x + 32*cos(radians(self.angle)), y + 32*sin(radians(self.angle))]
    node2Position = [x - 32*cos(radians(self.angle)), y - 32*sin(radians(self.angle))]

    if node1 == None:
      self.node1 = Node(container.circuit, node1Position)
      container.circuit.addNode(self.node1)
    else:
      self.node1 = node1
    if node2 == None:
      self.node2 = Node(container.circuit, node2Position)
      container.circuit.addNode(self.node2)
    else:
      self.node2 = node2

    self.component = None

    if type == ComponentType.wire:
      self.component = Wire(self.node1, self.node2)
    elif type == ComponentType.resistance:
      self.component = Resistance(self.node1, self.node2)
    elif type == ComponentType.generator:
      self.component = Generator(self.node1, self.node2)

    container.circuit.addComponent(self.component)

    self.show()