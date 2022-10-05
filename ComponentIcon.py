import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ComponentType import ComponentType

class ComponentIcon(ttk.Label):
  def __init__(self, container, type):
    self.path = "./assets/"

    if type == ComponentType.wire:
      self.path += "Wire"
    elif type == ComponentType.resistance:
      self.path += "Resistance"
    elif type == ComponentType.generator:
      self.path += "Generator"

    image = Image.open(self.path + ".png")
    image = image.resize((64, 64), Image.ANTIALIAS)
    #Prevents the image from being considered as garbage when the program exits the constructor
    self.image = ImageTk.PhotoImage(image=image)
    self.type = type

    super().__init__(container, image = self.image, padding=5)