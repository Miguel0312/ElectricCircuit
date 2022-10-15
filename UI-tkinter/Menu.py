import tkinter as tk
from tkinter import ttk
from ComponentIcon import ComponentIcon
from ComponentType import ComponentType
from DragManager import DragManager

class Menu(ttk.Frame):
  def __init__(self, container, dm: DragManager):
    super().__init__(container, style="Menu.TFrame")

    self.rowconfigure(0, weight=1)

    self.columnconfigure(0, weight=7)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)
    self.columnconfigure(3, weight=1)
    self.columnconfigure(4, weight=7)

    wireIcon = ComponentIcon(self, ComponentType.wire)
    resistanceIcon = ComponentIcon(self, ComponentType.resistance)
    generatorIcon = ComponentIcon(self, ComponentType.generator)

    dm.add_dragable(wireIcon)
    dm.add_dragable(resistanceIcon)
    dm.add_dragable(generatorIcon)

    wireIcon.grid(row=0, column=1)
    resistanceIcon.grid(row=0, column=2)
    generatorIcon.grid(row=0, column=3)