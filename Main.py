from tkinter import messagebox

import pygame
from tkinter import *
from math import *
from Point import Point
from DFS import DFS
from BFS import BFS
from Dijkstra import Dijkstra
from AStarPathfinder import AStarPathfinder

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 800))

# Title and Icon
pygame.display.set_caption("Algorithms")
icon = pygame.image.load('grid.png')
pygame.display.set_icon(icon)

# Declare variables to make grid
side_length = 800
rows = 50
cols = 50
width = side_length / cols
height = side_length / rows
grid = [[Point(y, x, screen) for x in range(rows)] for y in range(cols)]

window = Tk()

button_clicked = False
grid_cleared = True


def clear_board():
    global grid_cleared
    for row in grid:
        for point in row:
            pygame.draw.rect(screen, (0, 0, 0), (point.x * height, point.y * width, width, height), 0)
            point.clear_point()
            point.draw()
            pygame.display.update()
            grid_cleared = True


# Define Button's Action
def buttonClick():
    global pathfinder_identified
    pathfinder_identified = False
    global pathfinder
    pathfinder = None
    global pathfinder_done
    pathfinder_done = False
    global start_x
    start_x = x1.get()
    global start_y
    start_y = y1.get()
    global end_x
    end_x = x2.get()
    global end_y
    end_y = y2.get()
    if not (start_x.isnumeric() and start_y.isnumeric() and end_x.isnumeric() and end_y.isnumeric()):
        messagebox.showerror("Error", "Please enter numbers.")
        return
    if not (in_range(start_x) and in_range(start_y) and in_range(end_x) and in_range(end_y)):
        messagebox.showerror("Error", "Please enter numbers within the given range.")
        return
    if start_x == end_x and start_y == end_y:
        messagebox.showerror("Error", "Start and end coordinates cannot be the same.")
        return
    if not grid_cleared:
        msg = messagebox.askquestion('Grid Not Cleared', 'The grid has not been cleared. Do you wish to continue?', icon='warning')
        if msg == 'no':
            print("{{P{")
            return
    global algorithm_type
    algorithm_type = algorithms.get()
    grid[int(x1.get())][int(y1.get())].start = True
    grid[int(x2.get())][int(y2.get())].end = True
    global button_clicked
    button_clicked = True
    window.withdraw()
    window.quit()


# Options for dropdown menu
algorithms = StringVar()

algorithms.set("Depth-First Search")
options = [
    "Depth-First Search",
    "Breadth-First Search",
    "Dijkstra's Algorithm",
    "A* Pathfinder"
]

# Starting Menu
x1 = Entry(window, width=3, borderwidth=2)
y1 = Entry(window, width=3, borderwidth=2)
x2 = Entry(window, width=3, borderwidth=2)
y2 = Entry(window, width=3, borderwidth=2)
dropdown = OptionMenu(window, algorithms, *options)

Label(window, text="Choose Start and End Coordinates (0-49)").grid(row=0, column=0)
Label(window, text="Start:").grid(row=1, column=0)
Label(window, text="x: ").grid(row=2, column=0)
x1.grid(row=2, column=1)
Label(window, text="y: ").grid(row=2, column=2)
y1.grid(row=2, column=3)
Label(window, text="End:").grid(row=3, column=0)
Label(window, text="x: ").grid(row=4, column=0)
x2.grid(row=4, column=1)
Label(window, text="y: ").grid(row=4, column=2)
y2.grid(row=4, column=3)
Button(window, text="Confirm", padx=0, command=buttonClick, fg="black", bg="#00FF00").grid(row=5, column=2)
Button(window, text="Clear Grid", padx=0, command=clear_board, fg="white", bg="#000000").grid(row=0, column=2)
dropdown.grid(row=5, column=0, padx=30)


# Helper function to check if block is in range
def block_in_range(coordinates):
    return 0 <= coordinates[0] <= side_length and 0 <= coordinates[1] <= side_length


# Helper function to check if input is in range
def in_range(x):
    return 0 <= int(x) < rows


# Get x and y coordinates of a block pressed on by the mouse
def get_position(coords):
    i = floor(coords[0] / height)
    j = floor(coords[1] / width)
    return [i, j]


# Function to choose algorithm to perform
def identify_pathfinder(name):
    if name == "Depth-First Search":
        solver = DFS(grid, int(start_x), int(start_y), int(end_x), int(end_y), screen)
        solver.agenda.append(grid[int(start_x)][int(start_y)])
    elif name == "Breadth-First Search":
        solver = BFS(grid, int(start_x), int(start_y), int(end_x), int(end_y), screen)
        solver.agenda.append(grid[int(start_x)][int(start_y)])
    elif name == "Dijkstra's Algorithm":
        solver = Dijkstra(grid, int(start_x), int(start_y), int(end_x), int(end_y), screen)
    elif name == "A* Pathfinder":
        solver = AStarPathfinder(grid, int(start_x), int(start_y), int(end_x), int(end_y), screen)
    return solver


# Game Loop
pathfinder_identified = False
pathfinder = None
hold = False
running = True
pathfinder_done = False
while running:
    try:
        window.winfo_ismapped()
    except TclError:
        running = False
    if pathfinder_done:
        button_clicked = False
        grid_cleared = False
        try:
            window.deiconify()
        except TclError:
            running = False
    for i in range(rows):
        for j in range(cols):
            grid[i][j].draw()
    if hold:
        coordinates = get_position(pygame.mouse.get_pos())
        if not (grid[coordinates[0]][coordinates[1]].end or grid[coordinates[0]][coordinates[1]].start):
            grid[coordinates[0]][coordinates[1]].wall = True
            grid[coordinates[0]][coordinates[1]].draw()
    if pathfinder_identified and not pathfinder_done:
        pathfinder_done = pathfinder.solve()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if block_in_range(pygame.mouse.get_pos()):
                hold = True
        if event.type == pygame.MOUSEBUTTONUP:
            hold = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pathfinder_identified:
                pathfinder = identify_pathfinder(algorithm_type)
                pathfinder_identified = True
    pygame.display.update()
    if not button_clicked:
        window.mainloop()