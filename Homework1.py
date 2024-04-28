import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            return self.a + self.b + self.c
        else:
            return None
    
    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            p = self.perimeter() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return None
 
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b
        
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def area(self):
        try:
            return ((self.a + self.b) / 2) * math.sqrt((self.c**2) - (((self.b - self.a)**2 + self.c**2 - self.d**2)) / (2*(self.b - self.a))**2)
        except ValueError:
            return None
        except ZeroDivisionError:
            return None

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.h

class Circle:
    def __init__(self, r):
        self.r = r
    
    def circumference(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r ** 2


def read_input(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            figure_type = data[0]
            parameters = list(map(float, data[1:]))
            figures.append((figure_type, parameters))
    return figures


figures_data = []
for filename in ["input01.txt", "input02.txt", "input03.txt"]:
    figures_data.extend(read_input(filename))

max_area = 0
max_perimeter = 0
max_area_figure = None
max_perimeter_figure = None

for figure_type, parameters in figures_data:
    area = None
    perimeter = None
    if figure_type == 'Triangle':
        triangle = Triangle(*parameters)
        area = triangle.area()
        perimeter = triangle.perimeter()
    elif figure_type == 'Rectangle':
        rectangle = Rectangle(*parameters)
        area = rectangle.area()
        perimeter = rectangle.perimeter()
    elif figure_type == 'Trapeze':
        trapezoid = Trapeze(*parameters)
        area = trapezoid.area()
        perimeter = trapezoid.perimeter()
    elif figure_type == 'Parallelogram':
        parallelogram = Parallelogram(*parameters)
        area = parallelogram.area()
        perimeter = parallelogram.perimeter()
    elif figure_type == 'Circle':
        circle = Circle(*parameters)
        area = circle.area()
        perimeter = circle.circumference()
    
    if area is not None and perimeter is not None:
        if area > max_area:
            max_area = area
            max_area_figure = (figure_type, area)
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_figure = (figure_type, perimeter)

print("Фігура з найбільшою площею:", max_area_figure)
print("Фігура з найбільшим периметром:", max_perimeter_figure)

