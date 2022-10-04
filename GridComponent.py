import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ComponentType import ComponentType

class GridComponent(ttk.Label):
  def __init__(self, container, type):
    path = "./assets/"

    if type == ComponentType.wire:
      path += "Wire"
    elif type == ComponentType.resistance:
      path += "Resistance"
    elif type == ComponentType.generator:
      path += "Generator"

    image = Image.open(path + ".png")
    image = image.resize((64, 64), Image.ANTIALIAS)
    #Prevents the image from being considered as garbage when the program exits the constructor
    self.image = ImageTk.PhotoImage(image=image)
    self.type = type

    super().__init__(container, image = self.image)

  def place(self, x, y):
    super().place(x=x, y=y)
    self.node1 = [x, y+self.image.height()/2]
    self.node2 = [x + self.image.width(), y+self.image.height()/2]