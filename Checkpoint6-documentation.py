# Classes in Python


class MyClass:
    def greeting(self):
        return "Hi there"


greet_one = MyClass()  # create an instance of a class
# print(greet_one.greeting())


# Which method is automatically executed when a class is instantiated?
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


# Creating car objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2018)

# Accessing attributes and calling methods
# print(car1.display_info())
# print(car2.year)


# What is polymorphism?


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


# Create instances of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Execute the overridden method for all classes
# for x in (car1, boat1, plane1):
#     print(x.brand, x.model)
#     x.move()


def add(x, y, z=0):
    return x + y + z


# print(add(6, 4))
# print(add(6, 4, 6))


# Dunder methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# person1 = Person("Tom", 25)
# person2 = Person("Tina", 30)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)
# print(repr(person1))


# Python decorators
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello, I am a decorated function.")


# say_hello()


def time_it(my_function):
    import time

    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = my_function(*args, **kwargs)
        end_time = time.time()
        print(
            f"Execution time for {my_function.__name__}: {end_time - start_time} seconds"
        )
        return result

    return wrapper_function


@time_it
def calculate_square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result


# print(calculate_square([8, 6, 4]))
