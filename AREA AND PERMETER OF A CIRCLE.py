class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius
# Create an instance of the Circle class with a radius of 14
my_circle = Circle(14)

# Calculate the area of the circle
area = my_circle.area()
print(f"The area of the circle is: {area}")

# Calculate the perimeter (circumference) of the circle
perimeter = my_circle.perimeter()
print(f"The perimeter of the circle is: {perimeter}")
