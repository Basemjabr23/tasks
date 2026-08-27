# Task 1


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


person1 = Person("Ali", 20)
person2 = Person("Sara", 22)

person1.introduce()
person2.introduce()


# Task 2


class Employee(Person):
    def __init__(self, name, age, salary, job_title):
        super().__init__(name, age)
        self.salary = salary
        self.job_title = job_title

    def show_salary(self):
        print(f"Salary: ${self.salary}")

    def introduce(self):
        print(
            f"Hi, I'm {self.name}, I'm {self.age} years old, and I'm a {self.job_title}."
        )


employee = Employee("Omar", 25, 5000, "Backend Developer")

employee.introduce()
employee.show_salary()


# Task 3


class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand


class SportsCar(Car):
    def __init__(self, speed, brand, top_speed):
        super().__init__(speed, brand)
        self.top_speed = top_speed

    def boost(self):
        self.speed += 20

        if self.speed > self.top_speed:
            self.speed = self.top_speed


sports_car = SportsCar(100, "BMW", 250)

print(sports_car.speed)
sports_car.boost()
print(sports_car.speed)


# Task 4


class Camera:
    def take_photo(self):
        print("Taking a photo")


class Phone:
    def make_call(self):
        print("Making a call")


class SmartPhone(Camera, Phone):
    pass


smartphone = SmartPhone()

smartphone.take_photo()
smartphone.make_call()


# Task 5


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(10, 4), Circle(3), Rectangle(7, 2)]

for shape in shapes:
    print(shape.area())


# Task 6


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - ${self.price}"


class EBook(Book):
    def __init__(self, title, price, file_size_mb):
        super().__init__(title, price)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"{self.title} - ${self.price} - {self.file_size_mb} MB"


book = Book("Clean Code", 30)
ebook = EBook("Python Crash Course", 25, 15)

print(book)
print(ebook)

















# Task 1


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


student1 = Student("Ali", 20)
student1.introduce()


# Task 2


class Student:
    school = "Mansoura University"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ali", 20)
print(student1.school)
print(Student.school)


# Task 3


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1


student1 = Student("Ali", 20)
student1.have_birthday()
print(student1.age)


# Task 4


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


student = Student("Omar", "Computer Science")
teacher = Teacher("Dr. Ahmed", "Physics")

student.introduce()
student.study()

teacher.introduce()
teacher.teach()


# Task 5


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.", end=" ")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I am in grade {self.grade}.")


student = Student("Sara", 10)
student.introduce()


# Task 6


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at speed {self.speed}")


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")


class SportsCar(Car):
    def __init__(self, speed, brand, turbo):
        super().__init__(speed, brand)
        self.turbo = turbo

    def use_turbo(self):
        print(f"Turbo enabled: {self.turbo}")


sports_car = SportsCar(200, "Ferrari", True)
sports_car.move()
sports_car.show_brand()
sports_car.use_turbo()


# Task 7


class Flyer:
    def fly(self):
        print("Flying in the sky")


class Swimmer:
    def swim(self):
        print("Swimming in the water")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
duck.swim()


# Task 8


class Animal:
    def sound(self):
        print("Some generic sound")


class Mammal(Animal):
    def feed_milk(self):
        print("Feeding milk")


class Walker:
    def walk(self):
        print("Walking on four legs")


class Dog(Mammal, Walker):
    pass


dog = Dog()
print(Dog.__mro__)
