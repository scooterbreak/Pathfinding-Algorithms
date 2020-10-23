# Pathfinding-Algorithms
This program uses Python, Tkinter, and Pygame to allow users to input start and end coordinates and interact with a grid that visualizes the pathfinder. Algorithms include a depth-first search, breadth-first search, Dijkstra’s Algorithm, and an A* algorithm. As the program is meant to visualize algorithms in real-time, this implementation may be slightly different from traditional implementations. One of the challenges of this program was figuring out how to progress through the algorithm while continuously refreshing Pygame's graphical interface.

## INSTRUCTIONS

Once you have chosen the start coordinates, end coordinates, and type of pathfinder, click confirm. This will exit the Tkinter window and allow you to draw on the grid. Drawing on the grid creates walls that the pathfinder cannot pass through. Note: the depth-first and breadth-first searches are not allowed to travel through diagonals, but the Dijkstra and A* algorithms are.

Once the walls have been drawn, press spacebar to begin the search. The algorithm will begin at the start coordinate and look for a path to the end. Dijkstra's and the A* algorithm will show the shortest path to the endpoint, if one exists.

When exiting the application, exit through the TKinter window. Exiting through the Pygame window crashes the application and I haven't been able to fix this issue.

Included is a Pathfinding Algorithms.exe file which allows you to download an executable of the program. A "Pathfinding Algorithms" folder will appear in the location of installation and in that folder is a "Main.exe" executable which runs the program.


As this is my first project in Python, there may be a some unorthodox code, such as the way I use global variables and structure the different classes.


Created in summer 2020 when my summer research plans were cancelled due to COVID-19 and I had just decided to switch to a computer science major.
