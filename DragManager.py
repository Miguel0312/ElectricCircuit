from math import radians, cos, sin
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from GridComponent import GridComponent

#TODO: use x and y relative to the window instead of relative to screen

class DragManager():
    def __init__(self, mainContainer, components) -> None:
        self.mainContainer = mainContainer
        self.components = components
        self.angle = 0

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind_all("r", self.on_rotate)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        self.angle = 0
        x,y = event.widget.winfo_pointerxy()
        self.selected = event.widget.winfo_containing(x,y)

        self.movingImage = self.selected.image
        self.moving = ttk.Label(self.mainContainer, image=self.movingImage)

        self.imageWidth = self.selected.image.width()
        self.imageHeight = self.selected.image.height()

        self.moving.place(x=x-self.imageWidth/2, y=y-self.imageHeight)

    def on_drag(self, event):
        x,y = event.widget.winfo_pointerxy()

        node1 = [x + self.imageWidth/2*cos(radians(self.angle)), y + self.imageHeight/2*sin(radians(self.angle))]
        node2 = [x - self.imageWidth/2*cos(radians(self.angle)), y - self.imageHeight/2*sin(radians(self.angle))]

        for c in self.components:
            for node in [node1, node2]:
                for destNode in [c.node1, c.node2]:
                    if(pow(node[0] - destNode[0], 2) + pow(node[1] - destNode[1], 2) <= 50):
                        x = destNode[0] + (node1[0] + node2[0] - 2*node[0])/2
                        y = destNode[1] + (node1[1] + node2[1] - 2*node[1])/2
                        break

        self.moving.place(x=x-self.imageWidth/2, y=y-self.imageHeight)

    def on_drop(self, event):
        fc = GridComponent(self.mainContainer, self.selected.type)

        x,y = event.widget.winfo_pointerxy()

        node1 = [x + self.imageWidth/2*cos(radians(self.angle)), y + self.imageHeight/2*sin(radians(self.angle))]
        node2 = [x - self.imageWidth/2*cos(radians(self.angle)), y - self.imageHeight/2*sin(radians(self.angle))]

        for c in self.components:
            for node in [node1, node2]:
                for destNode in [c.node1, c.node2]:
                    if(pow(node[0] - destNode[0], 2) + pow(node[1] - destNode[1], 2) <= 50):
                        x = destNode[0] + (node1[0] + node2[0] - 2*node[0])/2
                        y = destNode[1] + (node1[1] + node2[1] - 2*node[1])/2
                        break
        
        fc.place(x=x, y=y, angle=self.angle)
        
        self.components.append(fc)

        self.moving.destroy()

    def on_rotate(self, event):
        image = Image.open(self.selected.path + ".png")
        image = image.resize((64, 64), Image.ANTIALIAS)
        self.angle = (self.angle - 90) % 360
        self.movingImage = ImageTk.PhotoImage(image.rotate(self.angle))
        self.moving.configure(image=self.movingImage) 
        
