from visualization import visualization
from maze import Maze
from wall_follower import WallFollower
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


    def start(self):
        """Alustaa sovelluksen näkymän.
        """     
        
        solve_label = ttk.Label(master=self._frame, text="Ratkaise labyrintti:")
        self._frame.pack()
        s = ttk.Style()
        s.configure("TFrame", background="DarkSeaGreen1")
        s.configure("TLabel", background="DarkSeaGreen1")
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)
        

        #time label
        self.wall_follower_time = StringVar(self._frame)
        self.wall_follower_time_label = ttk.Label(
            master=self._frame,
            textvariable=self.wall_follower_time,
            foreground="red")
        #step label
        self.wall_follower_steps = StringVar(self._frame)
        self.wall_follower_steps_label = ttk.Label(
            master=self._frame,
            textvariable=self.wall_follower_steps,
            foreground="red")
        
        generate_maze_button = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=self.load_new_maze)

        wall_follower_button = ttk.Button(
            master=self._frame,
            text="Wall Follower",
            command=self.wall_follower)

        self.maze_label.grid(row=1, column=0, ipady=5, padx=5, pady=5)
        generate_maze_button.grid(row=4, column=0, padx=5, pady=10)
        solve_label.grid(row=5, column=0, pady=20)
        wall_follower_button.grid(row=6, column=0, padx=5, pady=5)


        size_label = ttk.Label(master=self._frame, text="Labyrintin koko:")
        size_label.grid(row=2, column=0, padx=5, pady=5)
        self.size_entry = ttk.Entry(master=self._frame)
        self.size_entry.grid(row=3, column=0)
        self.wall_follower_time_label.grid(row=7, column=0)
        self.wall_follower_steps_label.grid(row=8, column=0)


      

    def wall_follower(self):
        wall_follower = WallFollower(self.air_directed_maze)
        wall_follower.draw_solution()
        
        self.wall_follower_time.set(str(wall_follower.elapsed_time) + " sekuntia")
        self.wall_follower_steps.set(str(len(wall_follower.solution))+ " askelta")
        self.wall_follower_time_label.grid()
        self.wall_follower_steps_label.grid()
        self.show_solution()
        


    def show_solution(self):
        photo = tk.PhotoImage(file="src/data/solution.png")
        self.maze_label.configure(image=photo)
        self._root.mainloop()
        
        
    def load_new_maze(self):
        maze_size = int(self.size_entry.get())
        self.class_maze = Maze(maze_size)
        self.generated_maze = self.class_maze.solution
        self.air_directed_maze = self.class_maze.air_directed_maze
        visualization.draw_maze_image(self.generated_maze, maze_size)
        photo = tk.PhotoImage(file="src/data/maze.png")
        self.maze_label.configure(image=photo)
        self._root.mainloop()

  
        