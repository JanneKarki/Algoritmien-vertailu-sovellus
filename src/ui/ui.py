import tkinter as tk
from tkinter import StringVar, ttk, constants
from turtle import bgcolor

class UI:
    def __init__(self, root):
        """Käyttöliittymäluokka joka vastaa näkymän näyttämisestä.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
        """
        
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        
     
        
    def start(self):
        """Alustaa ja näyttää sovelluksen näkymän.
        """
        heading_label = ttk.Label(master=self._frame, text="Hello")
        heading_label.grid(row=0, column=0)
        
        s = ttk.Style()
        s.configure("TFrame", background="DarkSeaGreen1")
        s.configure("TLabel", background="DarkSeaGreen1")
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)
        self._frame.pack()
        
        
