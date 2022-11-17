from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from Component import Component
from ComponentType import ComponentType

class Footer(QWidget):
  def __init__(self):
    super().__init__()
    self.setAutoFillBackground(True)

    palette = self.palette()
    palette.setColor(QPalette.Window, QColor("#aaa"))
    self.setPalette(palette)
    
    self.quantity = QLabel("Resistance:")
    self.quantity.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.valueEdit = QLineEdit()
    self.valueEdit.textChanged.connect(self.updateValue)
    self.unity = QLabel("Ohm")
    self.tensions = QLabel()
    self.current = QLabel() 

    self.layout = QHBoxLayout(self)
    self.layout.addStretch(6)
    self.layout.addWidget(self.quantity, stretch=2)
    self.layout.addWidget(self.valueEdit, stretch=2)
    self.layout.addWidget(self.unity, stretch=1)
    self.layout.addWidget(self.tensions, stretch=3)
    self.layout.addWidget(self.current, stretch=3)
    self.layout.addStretch(6)

    self.setComponent(None)

  def setComponent(self, component: Component):
    self.component = component
    if component == None:
      self.quantity.setVisible(False)
      self.valueEdit.setVisible(False)
      self.unity.setVisible(False)
      self.tensions.setVisible(False)
      self.current.setVisible(False)
      return

    self.quantity.setVisible(True)
    self.valueEdit.setVisible(True)
    self.unity.setVisible(True)
    self.tensions.setVisible(True)
    self.current.setVisible(True)

    if component.getType() == ComponentType.wire:
      self.quantity.setVisible(False)
      self.valueEdit.setVisible(False)
      self.unity.setVisible(False)
    elif component.getType() == ComponentType.resistance:
      self.quantity.setText("Resistance:")
      self.valueEdit.setText(str(component.getResistance()))
      self.unity.setText("\u03A9")
    elif component.getType() == ComponentType.generator:
      self.quantity.setText("Tension:")
      self.valueEdit.setText(str(component.getTension()))
      self.unity.setText("V")

    node1 = component.getNodes()[0]
    node2 = component.getNodes()[1]

    if node1.getCalculated() and node2.getCalculated():
      if node1.position[1] == node2.position[1]:
        left = 0.0
        right = 0.0
        if node1.position[0] < node2.position[0]:
          left = node1.getTension()
          right = node2.getTension()
        else:
          left = node2.getTension()
          right = node1.getTension()
        self.tensions.setText(f"Tensions - Left: {left}V Right: {right}V")
        if ((node1.position[0] < node2.position[0] and component.getCurrent() >= 0) or 
            (node1.position[0] > node2.position[0] and component.getCurrent() <= 0)):
          self.current.setText(f"Current - Left to Right: {abs(component.getCurrent())}A")
        else:
          self.current.setText(f"Current - Right to Left: {abs(component.getCurrent())}A")
      else:
        top = 0.0
        bottom = 0.0
        if node1.position[1] < node2.position[1]:
          top = node1.getTension()
          bottom = node2.getTension()
        else:
          top = node2.getTension()
          bottom = node1.getTension()
        self.tensions.setText(f"Tensions - Top: {top}V Bottom: {bottom}V")
        if ((node1.position[1] < node2.position[1] and component.getCurrent() >= 0) or 
            (node1.position[1] > node2.position[1] and component.getCurrent() <= 0)):
          self.current.setText(f"Current - Top to Bottom: {abs(component.getCurrent())}A")
        else:
          self.current.setText(f"Current - Bottom to Top: {abs(component.getCurrent())}A")
    else:
      self.tensions.setText("")
      self.current.setText("")

  def updateValue(self):
    try:
      n = float(self.valueEdit.text())
      if self.component.getType() == ComponentType.resistance and n != self.component.getResistance():
        self.component.setResistance(n)
        self.component.setCalculated(False)
      if self.component.getType() == ComponentType.generator and n != self.component.getTension():
        self.component.setTension(n)
        self.component.setCalculated(False)
    except ValueError:
      return