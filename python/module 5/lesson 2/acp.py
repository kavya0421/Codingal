# create class
class Circle():

    # constructor
    def __init__(self):
        self.radius = 0

    # function to get input from user
    def get_Radius(self):
        self.radius = float(input("Enter Radius : "))

    # function to calculate area and perimeter
    def calculate(self):
        area = 3.14 * self.radius * self.radius
        perimeter = 2 * 3.14 * self.radius

        print("Area of Circle :", area)
        print("Perimeter of Circle :", perimeter)

# Object creation
c1 = Circle()

# Call functions
c1.get_Radius()
c1.calculate()