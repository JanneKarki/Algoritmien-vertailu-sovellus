from visualization import visualization
from maze import Maze
from wall_follower import WallFollower
import tkinter as tk
from tkinter import ttk
from PIL import Image


class UI:
    def __init__(self, root):
        """Käyttöliittymäluokka joka vastaa näkymän näyttämisestä.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
        """
      
        self._root = root
        self.class_maze = Maze(10)
        self._frame = ttk.Frame(master=self._root)
        self.maze = self.class_maze.maze_by_kruskal()
        self.maze_air_directed = self.class_maze.maze_in_air_directions(self.maze)
        self.wall_follower = WallFollower(self.maze_air_directed)
        self.image = visualization.draw_maze_image(self.maze, 10)
        self.image = self.wall_follower.draw_solution()
        self.photo_image = tk.PhotoImage(file="src/data/maze.png")
        self.maze_label = ttk.Label(master=self._frame, image=self.photo_image)


    def start(self):
        """Alustaa ja näyttää sovelluksen näkymän.
        """

        heading_label = ttk.Label(master=self._frame, text="Labyrintti")
        heading_label.grid(row=0, column=0)
   
        self.maze_label.grid(row=1, column=0 )
        solve_label = ttk.Label(master=self._frame, text="Ratkaise labyrintti:")

        s = ttk.Style()
        s.configure("TFrame", background="DarkSeaGreen1")
        s.configure("TLabel", background="DarkSeaGreen1")
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)
        self._frame.pack()
        
        generate_maze_button = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command="")

        wall_follower_button = ttk.Button(
            master=self._frame,
            text="Wall Follower",
            command=self.load_photo)        


        generate_maze_button.grid(row=3, column=0, padx=5, pady=5)
        solve_label.grid(row=4, column=0)
        wall_follower_button.grid(row=5, column=0, padx=5, pady=5)
        
      

    def load_solved_maze(self):
        solved_maze = tk.PhotoImage(file="src/data/solution.png")
        print(solved_maze)
        self.photo_variable.set(solved_maze)

    def load_photo(self):
        photo = tk.PhotoImage(file="src/data/solution.png")
        self.maze_label.configure(image=photo)
        self._root.mainloop()