import math

rows = 50
cols = 50
width = 800 / cols
height = 800 / rows
infinity = 9999999


# Helper function to determine if given point is in range of grid
def in_range(x, y):
    return 0 <= x < cols and 0 <= y < rows


class AStarPathfinder():

    def __init__(self, grid, start_x, start_y, end_x, end_y, screen):
        self.grid = grid
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.screen = screen
        self.visited_points = []
        self.path_found = False
        self.shortest_distance = {}
        self.agenda = {}
        self.previous = None
        self.f_cost = {}
        for row in grid:
            for point in row:
                if in_range(point.x, point.y) and not point.is_wall():
                    if in_range(point.x, point.y):
                        if point.x == start_x and point.y == start_y:
                            self.shortest_distance[point] = 0
                            self.agenda[point] = 0
                            self.f_cost[point] = 0
                        else:
                            self.shortest_distance[point] = infinity
                            self.f_cost[point] = infinity

    def solve(self):
        if self.path_found:
            if self.previous is not self.grid[self.start_x][self.start_y]:
                self.previous.optimal_path = True
                self.previous.draw()
                self.previous = self.previous.previous_node
            else:
                return True
        else:
            if not self.is_empty():
                while True:
                    current_point = min(self.f_cost, key=self.f_cost.get)
                    if self.visited_points.count(current_point) == 0:
                        break
                if self.f_cost[current_point] == infinity:
                    print("No Path.")
                    return True
                self.f_cost.pop(current_point)
                self.visited_points.append(current_point)
                for neighbor in self.get_neighbors(current_point):
                    neighbor.is_neighbor = True
                    alternate_distance = self.shortest_distance.get(current_point) \
                                         + self.get_distance(current_point, neighbor)
                    if alternate_distance < self.shortest_distance.get(neighbor):
                        self.shortest_distance.update({neighbor: alternate_distance})
                        self.agenda.update({neighbor: alternate_distance})
                        g_cost = self.shortest_distance[neighbor]
                        h_cost = self.get_euclidean_distance(neighbor)
                        f_cost = g_cost + h_cost
                        if f_cost < self.f_cost[neighbor]:
                            self.f_cost.update({neighbor: f_cost})
                        neighbor.set_previous(current_point)
                        if neighbor.x == self.end_x and neighbor.y == self.end_y:
                            self.previous = self.grid[self.end_x][self.end_y].previous_node
                            self.path_found = True
                current_point.mark_visited()

    def is_empty(self):
        return len(self.agenda) == 0

    def get_distance(self, current_point, neighbor):
        if not (current_point.is_wall() and neighbor.is_wall()) and (
                current_point.x - 1 == neighbor.x and current_point.y - 1 == neighbor.y) \
                or (current_point.x + 1 == neighbor.x and current_point.y - 1 == neighbor.y) \
                or (current_point.x - 1 == neighbor.x and current_point.y + 1 == neighbor.y) \
                or (current_point.x + 1 == neighbor.x and current_point.y + 1 == neighbor.y):
            return math.sqrt(2)
        else:
            return 1

    def get_euclidean_distance(self, neighbor):
        if not neighbor.is_wall():
            return math.sqrt(math.pow((neighbor.x - self.end_x), 2) + math.pow((neighbor.y - self.end_y), 2))

    def get_neighbors(self, point):
        neighbors = []
        for i in range(point.x - 1, point.x + 2):
            for j in range(point.y - 1, point.y + 2):
                if in_range(i, j) and not self.grid[i][j].is_wall() and not (i == point.x and j == point.y):
                    neighbors.append(self.grid[i][j])
        return neighbors
