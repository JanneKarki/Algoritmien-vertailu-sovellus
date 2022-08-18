from functionalities.visualization import visualization
from algorithms.maze import Maze
from algorithms.wall_follower import WallFollower
from algorithms.tremaux import Tremaux
import tkinter as tk
from tkinter import ttk, StringVar
from PIL import Image


class UI:
    def __init__(self, root):
        """Käyttöliittymäluokka joka vastaa näkymän näyttämisestä.

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self.class_maze = None
        self.generated_maze = None
        self.air_directed_maze = None
        self.maze_label = ttk.Label(master=self._frame, image=None)
        self.size_entry = None

        self.wall_follower_time = None
        self.wall_follower_time_label = None
        self.wall_follower_steps = None
        self.wall_follower_steps_label = None

        self.maze_time = None
        self.maze_time_label = None

        self.tremaux_time = None
        self.tremaux_time_label = None
        self.tremaux_steps = None
        self.tremaux_steps_label = None

    def start(self):
        """Alustaa sovelluksen näkymän.
        """

        solve_label = ttk.Label(
            master=self._frame, text="Ratkaise labyrintti:")
        self._frame.pack()
        s = ttk.Style()
        s.configure("TFrame", background="DarkSeaGreen1")
        s.configure("TLabel", background="DarkSeaGreen1")
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)

        # wall_follower_time label
        self.wall_follower_time = StringVar(self._frame)
        self.wall_follower_time_label = ttk.Label(
            master=self._frame,
            textvariable=self.wall_follower_time,
            foreground="red")
        # step label
        self.wall_follower_steps = StringVar(self._frame)
        self.wall_follower_steps_label = ttk.Label(
            master=self._frame,
            textvariable=self.wall_follower_steps,
            foreground="red")
        # maze_time
        self.maze_time = StringVar(self._frame)
        self.maze_time_label = ttk.Label(
            master=self._frame,
            textvariable=self.maze_time,
            foreground="red")

        # tremaux_time
        self.tremaux_time = StringVar(self._frame)
        self.tremaux_time_label = ttk.Label(
            master=self._frame,
            textvariable=self.tremaux_time,
            foreground="red")
        # tremaux_steps
        self.tremaux_steps = StringVar(self._frame)
        self.tremaux_steps_label = ttk.Label(
            master=self._frame,
            textvariable=self.tremaux_steps,
            foreground="red")

        generate_maze_button = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=self.load_new_maze)

        wall_follower_button = ttk.Button(
            master=self._frame,
            text="Wall Follower",
            command=self.handle_wall_follower)
        tremaux_button = ttk.Button(
            master=self._frame,
            text="Tremaux",
            command=self.handle_tremaux)

        self.maze_label.grid(row=1, column=0, ipady=5, padx=5, pady=5)
        generate_maze_button.grid(row=4, column=0, padx=5, pady=10)
        self.maze_time_label.grid(row=5, column=0)
        solve_label.grid(row=6, column=0, pady=20)
        wall_follower_button.grid(row=7, column=0, padx=5, pady=5)

        size_label = ttk.Label(master=self._frame, text="Labyrintin koko:")
        size_label.grid(row=2, column=0, padx=5, pady=5)
        self.size_entry = ttk.Entry(master=self._frame)
        self.size_entry.grid(row=3, column=0)
        self.wall_follower_time_label.grid(row=8, column=0)
        self.wall_follower_steps_label.grid(row=9, column=0)
        tremaux_button.grid(row=10, column=0)
        self.tremaux_time_label.grid(row=11, column=0)
        self.tremaux_steps_label.grid(row=12, column=0)

    def handle_wall_follower(self):
        """Ratkaisee labyrintin "Wall Follower"-algoritmilla ja piirtää
           sen labyrintin kuvaan, sekä asettaa sen näykyville. 
        """
        wall_follower = WallFollower(self.air_directed_maze)
        self.wall_follower_time.set(
            str(wall_follower.elapsed_time) + " sekuntia")
        self.wall_follower_steps.set(
            str(len(wall_follower.solution)) + " askelta")
        self.wall_follower_time_label.grid()
        self.wall_follower_steps_label.grid()
        photo = tk.PhotoImage(file="src/data/solution_wall_follower.png")
        self.show_solution(photo)

    def handle_tremaux(self):
        """Ratkaisee labyrintin "Tremaux"-algoritmilla, piirtää
           sen labyrintin kuvaan ja asettaa sen näykyville. 
        """
        tremaux = Tremaux(self.air_directed_maze)
        self.tremaux_time.set(str(tremaux.elapsed_time) + " sekuntia")
        self.tremaux_steps.set(str(len(tremaux.solution)) + " askelta")
        self.tremaux_time_label.grid()
        self.tremaux_steps_label.grid()
        photo = tk.PhotoImage(file="src/data/solution_tremaux.png")
        self.show_solution(photo)

    def show_solution(self, photo):
        """Lataa piirretyn ratkaisun kuvan ja asettaa sen näkyviin.
        """

        self.maze_label.configure(image=photo)
        self._root.mainloop()

    def load_new_maze(self):
        """Lataa uuden labyrintin, tallentaa sen kuvana ja asettaa myös näkyville.
        """
        self.hide_results()
        maze_size = int(self.size_entry.get())
        self.class_maze = Maze(maze_size)
        self.generated_maze = self.class_maze.solution
        self.air_directed_maze = self.class_maze.air_directed_maze
        visualization.draw_maze_image(self.generated_maze, maze_size)
        photo = tk.PhotoImage(file="src/data/maze.png")
        self.maze_label.configure(image=photo)
        self.maze_time.set(
            "Aikaa kului " + str(self.class_maze.elapsed_time) + " sekuntia")
        self.maze_time_label.grid()
        self._root.mainloop()

    def hide_results(self):
        """Piilottaa ratkaisun tulokset
        """
        self.wall_follower_steps_label.grid_remove()
        self.wall_follower_time_label.grid_remove()
        self.tremaux_time_label.grid_remove()
        self.tremaux_steps_label.grid_remove()
