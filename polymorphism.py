class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        r = 5
        print("Circle:",3.14 * r * r)
class Rectangle(Shape):
    def area(self):
        l,b = 4,5
        print("Rectangle:",l * b)

c = Circle()
r = Rectangle()
c.area()
r.area()