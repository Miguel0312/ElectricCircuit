import tkinter as tk
from tkinter import ttk
import screeninfo

class Grid(ttk.Frame):
  def __init__(self, container: tk.Tk):
    super().__init__(container)
