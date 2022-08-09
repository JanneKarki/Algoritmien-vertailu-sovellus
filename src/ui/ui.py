from visualization import visualization
from maze import maze
import tkinter as tk
from tkinter import StringVar, ttk, constants
from turtle import bgcolor
from PIL import Image


class UI:
    def __init__(self, root):
        """Käyttöliittymäluokka joka vastaa näkymän näyttämisestä.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
        """
        self.photo_image = tk.PhotoImage(file="src/data/maze.png")
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self.maze = maze.maze_in_air_directions()
        self.image = visualization.draw_maze_image(self.maze)
        

    def start(self):
        """Alustaa ja näyttää sovelluksen näkymän.
        """

        heading_label = ttk.Label(master=self._frame, text="Labyrintti")
        heading_label.grid(row=0, column=0)
        maze_label = ttk.Label(master=self._frame, image=self.photo_image)
        maze_label.grid(row=1, column=0 )

        s = ttk.Style()
        s.configure("TFrame", background="DarkSeaGreen1")
        s.configure("TLabel", background="DarkSeaGreen1")
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)
        self._frame.pack()
        
        
