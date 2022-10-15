from math import sin, cos, radians
from re import I
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
from ComponentType import ComponentType

class GridComponent(ttk.Label):
  def __init__(self, container, type):
    self.neighbours = []
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

    super().__init__(container, image = self.image, borderwidth=0)

  def place(self, x, y, angle):
    super().place(x=x-self.image.width()/2, y=y-self.image.height())
    self.node1 = [x + self.image.width()/2*cos(radians(angle)), y + self.image.height()/2*sin(radians(angle))]
    self.node2 = [x - self.image.width()/2*cos(radians(angle)), y - self.image.height()/2*sin(radians(angle))]
    self.x = x
    self.y = y
    self.angle = angle
    if self.angle % 180 != 0:
      self.image = ImageTk.PhotoImage(self.getImage([]))
      self.configure(image=self.image)
      self.lift()


  def addNeighbour(self, neighbour):
    #TODO: rework the determination of the neighbours
    self.neighbours.append(neighbour)
    if(self.angle % 180 == 0):
      return
    corners = []
    for n in self.neighbours:
      tmp = ""
      if n.y < self.y:
        tmp += "t"
      else:
        tmp += "b"
      if n.x < self.x:
        tmp += "l"
      else:
        tmp += "r"
      corners.append(tmp)

    image = self.getImage(corners)
    self.image = ImageTk.PhotoImage(image)
    self.configure(image=self.image)

    if self.angle % 180 != 0:
      self.lift()

  def getImage(self, corners):
    path = "./assets/"

    if self.type == ComponentType.wire:
      path += "Wire"
    elif self.type == ComponentType.resistance:
      path += "Resistance"
    elif self.type == ComponentType.generator:
      path += "Generator"

    extension = ""
    angle = 0
    mirror = False

    if len(corners) == 0:
      extension = ""
      angle = 90
    elif len(corners) == 1:
      extension = "L"
      if corners[0] == "tr":
        angle = -90
      if corners[0] == "bl":
        angle = 90
      if corners[0] == "tl":
        angle = -90
        mirror = True
      if corners[0] == "br":
        angle = 90
        mirror = True
    elif len(corners) == 2:
      if corners[0][0] != corners[1][0] and corners[0][1] != corners[1][1]:
        extension = "Z"
      elif corners[0][0] == corners[1][0]:
        extension = "T"
      else:
        extension = "U"

      if extension == "Z":
        angle = -90
        if "tl" in corners and "br" in corners:
          mirror = True

      if extension == "T":
        if corners[0][0] == "t":
          angle = -90
        else:
          angle = 90
      
      if extension == "U":
        if corners[0][1] == "r":
          angle = -90
        else:
          angle = 90
        
    elif len(corners) == 3:
      out = [x for x in ["bl", "br", "tl", "tr"] if x not in corners][0]
      extension = "H"
      if out == "br":
        angle = -90
      elif out == "tl":
        angle = 90
      elif out == "bl":
        angle = -90
        mirror = True
      elif out == "tr":
        angle = 90
        mirror = True
    elif len(corners) == 4:
      extension = "I"
      angle = -90

    image = Image.open(path + extension + ".png")
    image = image.resize((64, 64), Image.ANTIALIAS)
    image = image.rotate(angle)
    if mirror:
      image = ImageOps.mirror(image)
    return image