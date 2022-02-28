# everything in python is an object

num = '10'
print(type(num))  # <class 'str'>


class SampleClass():

    def __init__(self, name=""):  # instantiation method
        self.name = name


x = SampleClass(name="Test Name")
print(type(x))  # <class '__main__.SampleClass'>
print(x.name)


class Student():

    planet = "Earth"  # class object attribute (same for any instance)

    def __init__(self, name, gpa):
        self.name = name  # attributes
        self.gpa = gpa   # attributes


stu1 = Student(name="J", gpa=4.0)
stu2 = Student(name="K", gpa=3.2)

print(
    f'student_1 info; name: {stu1.name}, gpa: {stu1.gpa}, planet: {stu1.planet}')
print(f'student_2 info; name: {stu2.name}, gpa: {stu2.gpa}')


class Agent():
    origin = "USA"

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


y = Agent(name="A", height=6, weight=322)
print(f"name: {y.name}, weight: {y.weight}")
y.weight = 160
print(f"name: {y.name}, weight: {y.weight}")


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        return 2 * self.radius * Circle.pi

    def double_radius(self):
        self.radius = self.radius*2
        print(f'radius doubled to: {self.radius}')

    def multiply_radius(self, number=1):
        self.radius = self.radius*number
        print(f'raidus changed to: {self.radius}')


mycircle = Circle(radius=4)
print(
    f"radius: {mycircle.radius}, area: {mycircle.area()}, perimeter: {mycircle.perimeter()}")
print(f'initial radius: {mycircle.radius}')
mycircle.double_radius()
print(mycircle.radius)
mycircle.multiply_radius(number=2)
