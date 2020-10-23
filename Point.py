import pygame

# Declare variables to make grid
rows = 50
cols = 50
width = 800 / cols
height = 800 / rows
infinity = 9999999


# Helper function to determine if given point is in range of grid
def in_range(x, y):
    return 0 <= x < cols and 0 <= y < rows


class Point:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.wall = False
        self.visited = False
        self.changed = False
        self.start = False
        self.end = False
        self.screen = screen
        self.previous_node = None
        self.optimal_path = False
        self.is_neighbor = False

    def draw(self):
        if not self.changed:
            if self.wall:
                pygame.draw.rect(self.screen, (93, 209, 190), (self.x * height, self.y * width, width, height), 0)
            elif self.start:
                pygame.draw.rect(self.screen, (11, 203, 31), (self.x * height, self.y * width, width, height), 0)
            elif self.end:
                pygame.draw.rect(self.screen, (219, 0, 0), (self.x * height, self.y * width, width, height), 0)
            else:
                if self.is_neighbor:
                    pygame.draw.rect(self.screen, (255, 100, 130), (self.x * height, self.y * width, width, height), 0)
                if self.has_been_visited():
                    pygame.draw.rect(self.screen, (255, 255, 255), (self.x * height, self.y * width, width, height), 0)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (self.x * height, self.y * width, width, height), 1)
                    return

        if self.optimal_path:
            pygame.draw.rect(self.screen, (0, 179, 255), (self.x * height, self.y * width, width, height), 0)
        self.changed = True

    def mark_visited(self):
        self.visited = True

    def has_been_visited(self):
        return self.visited

    def is_wall(self):
        return self.wall

    def set_previous(self, point):
        self.previous_node = point

    def clear_point(self):
        self.wall = False
        self.visited = False
        self.changed = False
        self.start = False
        self.end = False
        self.previous_node = None
        self.optimal_path = False
        self.is_neighbor = False
