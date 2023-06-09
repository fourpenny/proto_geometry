# Imports
import math

# Classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'x: {self.x}, y: {self.y}'

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.length = euclidian_distance(p1, p2)

    def get_midpoint(self) -> Point:
        midpoint = Point(
            x = (self.p1.x + self.p2.x) / 2,
            y = (self.p1.y + self.p2.y) / 2
        )
        return midpoint

class Circle:
    def __init__(self, center: Point, radius: float):
        self.c = center
        self.radius = radius

    def is_point_inside(self, point: Point) -> bool:
        distance_to_center = euclidian_distance(self.c, point)
        if distance_to_center < self.radius:
            return True
        else:
            return False
    
    def get_equally_spaced_points(self, num_points: int) -> list:
        if num_points < 2:
            raise ValueError
        points = []
        spacing = (2 * math.pi) / num_points
        start = 0
        for p in range(num_points):
            points.append(
                draw_line_from_point(
                    self.c, self.radius, start + (p * spacing)
                ).p2
            )
        return points
    
class Arc:
    def __init__(self, p1, p2, radius):
        self.p1 = p1
        self.p2 = p2
        self.radius = radius
        # Get center
        # Get angle
        return
    
    def get_equally_spaced_points(self, num_points: int) -> list:
        return
    
    def is_point_inside():
        return
    
    def does_point_intersect():
        return

# Functions

def draw_line_from_point(start: Point, length: float, angle: float) -> Line:
    endpoint = Point(
        x = start.x + (length * math.cos(angle)),
        y = start.y + (length * math.sin(angle))
    )
    line = Line(start, endpoint)

    return line

def euclidian_distance(p1: Point, p2: Point):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))

def get_arc(center, radius, angle):
    return