import tkinter as tk
from tkinter import ttk
from Menu import Menu
from Grid import Grid
from DragManager import DragManager

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        self.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, 0, 0))
        self.title("Electric Circuit Solver")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=16)
        self.columnconfigure(0 , weight=1)

        self.style = ttk.Style()
        self.style.configure("Menu.TFrame", background="#aaa")

        components = []

        dm = DragManager(self, components)

        menu = Menu(self, dm)
        grid = Grid(self)

        menu.grid(row=0, column=0, sticky="NSEW")
        grid.grid(row=1, column=0, sticky="NSEW")