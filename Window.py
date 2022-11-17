from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from GridComponent import GridComponent
from Menu import Menu
from Grid import Grid
from Footer import Footer

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.showMaximized()

    self.components: list[GridComponent] = []

    self.central = QWidget()
    self.layout = QVBoxLayout(self.central)
    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.setSpacing(0)

    self.setCentralWidget(self.central)

    palette = self.palette()
    palette.setColor(QPalette.Window, QColor("white"))
    self.setPalette(palette)

    self.footer = Footer()
    self.grid = Grid(self.components, self.footer)
    self.menu = Menu(self.grid, self.footer, self.components)

    self.layout.addWidget(self.menu, stretch=1)
    self.layout.addWidget(self.grid, stretch=10)
    self.layout.addWidget(self.footer, stretch=1)