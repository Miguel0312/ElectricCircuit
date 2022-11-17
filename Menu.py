from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from ComponentType import ComponentType
from ComponentIcon import ComponentIcon
from Grid import Grid
from Footer import Footer
from GridComponent import GridComponent

class Menu(QWidget):
  def __init__(self, grid: Grid, footer: Footer, components: list[GridComponent]):
    super().__init__()
    self.grid = grid
    self.footer = footer
    self.setAutoFillBackground(True)

    palette = self.palette()
    palette.setColor(QPalette.Window, QColor("#aaa"))
    self.setPalette(palette)
    

    self.layout = QHBoxLayout(self)

    self.wireIcon = ComponentIcon(ComponentType.wire, grid, components)
    self.resistanceIcon = ComponentIcon(ComponentType.resistance, grid, components)
    self.generatorIcon = ComponentIcon(ComponentType.generator, grid, components)

    self.button = QPushButton(text="Go")
    self.button.clicked.connect(self.goButtonOnClick)

    self.layout.addStretch(5)
    self.layout.addWidget(self.wireIcon, stretch=1)
    self.layout.addWidget(self.resistanceIcon, stretch=1)
    self.layout.addWidget(self.generatorIcon, stretch=1)
    self.layout.addStretch(5)
    self.layout.addWidget(self.button, stretch = 1)

  def goButtonOnClick(self):
    self.grid.circuit.solveCircuit()
    self.footer.setComponent(self.footer.component)
    