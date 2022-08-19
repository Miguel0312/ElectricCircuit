import tkinter as tk
from tkinter import ttk
from Menu import Menu

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        windowWidth = 1080
        windowHeight = 608
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = int(screenWidth/2 - windowWidth/2)
        y = int(screenHeight/2 - windowHeight/2)

        self.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))
        self.title("Electric Circuit Solver")

        menu = Menu(self)
        menu.pack()