#Class leel attributes are shared across all instances of a class
#if we change their value, the change is visible to all objects of that type

class Point:

    #Class level attribute
    default_color = "red"

    def __init__(self, x, y):
        #Instance attributes
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point({self.x}, {self.y})")

Point.default_color = "yellow"
point = Point(1,2)
print(Point.default_color)
point.draw()