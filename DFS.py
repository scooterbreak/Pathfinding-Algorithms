rows = 50
cols = 50
width = 800 / cols
height = 800 / rows


# Helper function to determine if given point is in range of grid
def in_range(x, y):
    return 0 <= x < cols and 0 <= y < rows


class DFS():

    def __init__(self, grid, start_x, start_y, end_x, end_y, screen):
        self.grid = grid
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.screen = screen
        self.agenda = []

    def solve(self):
        if not self.is_empty():
            temporary = self.peek()
            self.remove()
            self.add_points(temporary)
            if temporary.x == self.end_x and temporary.y == self.end_y:
                print("Path Found.")
                return True
            temporary.mark_visited()
        else:
            print("No Path.")
            return True

    def remove(self):
        self.agenda.pop()

    def peek(self):
        return self.agenda[len(self.agenda) - 1]

    def is_empty(self):
        return len(self.agenda) == 0

    def add(self, point):
        self.agenda.append(point)

    def add_points(self, point):
        if in_range(point.x, point.y + 1):
            point1 = self.grid[point.x][point.y + 1]
            if not point1.is_wall() and not point1.has_been_visited():
                self.add(point1)
        if in_range(point.x, point.y - 1):
            point2 = self.grid[point.x][point.y - 1]
            if not point2.is_wall() and not point2.has_been_visited():
                self.add(point2)
        if in_range(point.x - 1, point.y):
            point3 = self.grid[point.x - 1][point.y]
            if not point3.is_wall() and not point3.has_been_visited():
                self.add(point3)
        if in_range(point.x + 1, point.y):
            point4 = self.grid[point.x + 1][point.y]
            if not point4.is_wall() and not point4.has_been_visited():
                self.add(point4)
