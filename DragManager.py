import tkinter as tk
from tkinter import Image, ttk
from GridComponent import GridComponent

#TODO: use x and y relative to the window instead of relative to screen

class DragManager():
    def __init__(self, mainContainer, components) -> None:
        self.mainContainer = mainContainer
        self.components = components

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        x,y = event.widget.winfo_pointerxy()
        self.selected = event.widget.winfo_containing(x,y)

        self.moving = ttk.Label(self.mainContainer, image=self.selected.image)

        self.imageWidth = self.selected.image.width()
        self.imageHeight = self.selected.image.height()

        self.moving.place(x=x-self.imageWidth/2, y=y-self.imageHeight)

    def on_drag(self, event):
        x,y = event.widget.winfo_pointerxy()

        for c in self.components:
            if(pow(x+self.imageWidth/2-c.node1[0], 2)+pow(y - self.imageHeight/2 - c.node1[1], 2) <= 50):
                x = c.node1[0] - self.imageWidth/2
                y = c.node1[1] + self.imageHeight/2
                break
            if(pow(x-self.imageWidth/2-c.node2[0], 2)+pow(y - self.imageHeight/2 - c.node2[1], 2) <= 50):
                x = c.node2[0] + self.imageWidth / 2
                y = c.node2[1] + self.imageHeight/2
                break

        self.moving.place(x=x-self.imageWidth/2, y=y-self.imageHeight)

    def on_drop(self, event):
        #TODO: find nearest node and place a circuit component there
        x,y = event.widget.winfo_pointerxy()

        fc = GridComponent(self.mainContainer, self.selected.type)

        for c in self.components:
            if(pow(x+self.imageWidth/2-c.node1[0], 2)+pow(y - self.imageHeight/2 - c.node1[1], 2) <= 50):
                x = c.node1[0] - self.imageWidth/2
                y = c.node1[1] + self.imageHeight/2
                break
            if(pow(x-self.imageWidth/2-c.node2[0], 2)+pow(y - self.imageHeight/2 - c.node2[1], 2) <= 50):
                x = c.node2[0] + self.imageWidth / 2
                y = c.node2[1] + self.imageHeight/2
                break

        fc.place(x=x-self.imageWidth/2, y=y-self.imageHeight)
        
        self.components.append(fc)

        self.moving.destroy()
        
