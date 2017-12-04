from swampy.World import World

class Point(object):
    """Represents a point in 2D space."""

class Rectangle(object):
    """
    Represents a rectangle in 2D space.
    Attributes: width, height, corner
    """
class Circle(object):
    """
    Represents a circle in 2D space.
    Attributes: center, radius
    """
def draw_bangladesh():
    """
    Draws the bangladesh flag
    """
    bbox = [[-150, -100], [150, 100]]
    canvas.rectangle(bbox, outline='black', width=2, fill='green4')
    canvas.circle([-25, 0], 70, outline=None, fill='red')

def draw_rectangle(rect, canvas, color):
    lower_left = [rect.corner.x, rect.corner.y]
    upper_right = [rect.corner.x + rect.width, rect.corner.x + rect.height]
    rect = [lower_left, upper_right]
    canvas.rectangle(rect, outline='black', width=1, fill=color)

def draw_point(point, canvas):
    point = [point.x, point.y]
    canvas.circle(point, 0, outline='black', fill='black')


def draw_circle(circle, canvas):
    point = [circle.center.x, circle.center.y]
    canvas.circle(point, circle.radius, outline='black', fill='white')

def draw_1(canvas, width, height):
    """
    Draws the triangle of the czech flag
    """
    triangle_points = [[0, 0], [0, height], [width/3, height/2]]
    canvas.polygon(triangle_points, outline='black', fill='blue')

def draw_2(canvas, width, height):
    """
    Draws the lower polygon of the czech flag
    """
    lower_polygon = [[0, 0], [width, 0], [width, height/2], [width/3, height/2]]
    canvas.polygon(lower_polygon, outline='black', fill='red')

def draw_3(canvas, width, height):
    """
    Draws the upper polygon of the czech flag
    """
    upper_polygon = [[0, height], [width, height], [width, height/2], [width/3, height/2]]
    canvas.polygon(upper_polygon, outline='black', fill='white')

def draw_czech(canvas, width=400, height=200):
    """
    Draws the czech flag.
    """
    draw_1(canvas, width, height)
    draw_2(canvas, width, height)
    draw_3(canvas, width, height)

world = World()

canvas = world.ca(width=500, height=500, background='white')

# Defining some circle
circle = Circle()
circle.center = Point()
circle.center.x = -10
circle.center.y = 50
circle.radius = 20

# Defining some rectangle
box = Rectangle()
box.width = 100
box.height = 50
box.corner = Point()
box.corner.x = 5
box.corner.y = 2

# Defining some point
point = Point()
point.x = -1
point.y = 7

draw_czech(canvas)

world.mainloop()
