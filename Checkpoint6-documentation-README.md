# Checkpoint 6 Documentation

### What do we use Classes for in Python?
Python is a programming language that supports object-oriented programming (OOP) and classes are the building blocks of OOP. Classes serve as a template for creating objects. Classes are used to define and bundle the shared attributes and functionality of the objects together. Classes provide a way to organize and structure code, making it more modular, reusable, and maintainable.Once a class is defined, multiple objects or instances of that class can be created. This mallows for the code to be reused without repetition.
A class can be created bu using the keyword `class`. Lets look at a simple example of creating a class called `MyClass`.
```python
class MyClass:
    def greeting(self):
        return "Hi there"


greet_one = MyClass()  # create an instance of a class
print(greet_one.greeting())
```
##### OUTPUT
```
Hi there
```

Inside the class we define the `greeting` method,, and `self` is a reference to the current instance of the class,and is used to access variables that belongs to the class. To create an instance of the  `MyClass` and use its method. We create a new  `greet_one` object, and then call the `greeting()` method on the object. The use of Classes in Python along with more examples will be provided in the next section.  

### Which method is automatically executed when a class is instantiated?
The __init__ method (pronounced “dunder init”) is a special method in Python. It is automatically executed when a  an object is created from a class or in other words a class is instantiated.
#### The `__init__ ()` method

The `__init__ ` method is a special method used to initialize the object's attributes when it is created. This allows you to set the initial state of the object, which can be useful for setting up the object's properties, or other operations and ensuring that the object is in a valid state. By using the `__init__` method, every instance of the class starts with the same initial state ensuring consistency in the code. The `__init__()` method should be used to carry out any necessary setup or initialization logic for the object, which includes assigning values to instance variables, performing calculations or initializing other objects needed by the class.  The `__init__()`  method is a useful method for enhancing code flexibility as it allows you to accept different arguments and perform different initialization logic based on the specific needs of the object being created.

Lets look at an example and create a `Car` class to represent different cars with their attributes such as brand, model, and year.
```python
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
print(car1.display_info()) 
print(car2.year)  
```
 

##### OUTPUT
```
2020 Toyota Camry
2018
```
In this example the `__init__` initializes the object's attributes (brand, model, and year) with the values passed during object creation.`self.brand`, `self.model`, and `self.year` are instance variables that store the specific values for each instance of the class (self refers to the current instance of the class). The `display_info(self)` method takes `self` as its first 
parameter, representing the current instance of the class, and when called, it returns a formatted string containing the car's year, brand, and model.
This class allows us to create any number of objects by calling the class `Car` with specific values for brand, model, and year.The attributes and methods of these objects can then be accessed directly by calling `object_name.method()` or `object_name.attribute`

In summary, the `Car` class encapsulates the properties and behavior of a car. It allows us to create multiple instances of cars with different characteristics and provides methods to interact with these objects. This demonstrates the power of classes in Python for modeling real-world entities and organizing code effectively.

### What is an API?
An API (Application Programming Interface) is a set of protocols that allow one applications to interact with another. It defines how the different components of a software should communicate with each other, enabling seamless data transmission and functionality sharing. It can be thought of as a messenger that takes a request, processes it, and then returns the response. Let's take an example of  the weather app on our phone, the app makes an API call to a weather database to retrieve the current weather information for the location of the phone. Here the API acts as an intermediary, that takes your request, communicates with the weather database, and returns the response back to your app display.
API`s provide access to data from external sources such as databases, web services, or IoT devices. APIs are used by developers to extend the functionality of an applications by integrating with third-party services or libraries.
Some Examples of APIs are:

1. Google Maps API: Developers use this to embed maps, geolocation, and directions in their apps.
2. OpenWeatherMap API: Provides weather data for any location worldwide.
3. GitHub API: Provides access to GitHub's features like repositories, issues, and pull requests.

The syntax of an API request depends on the specific API being used. Typically request (most common request methods include GET (retrieve data), POST (send data), PUT (update data), and DELETE (remove data)) is sent to an API endpoint, which is a specific URL. and the API responds with data, usually in JSON or XML format, which developers can parse and use in their applications. Many APIs also require authentication to access their services securely.
Here’s a simple example using the OpenWeatherMap API:
```
GET https://api.openweathermap.org/data/2.5/weather?q=Seattle&appid=YOUR_API_KEY
```
Here `GET` is the API request method, `https://api.openweathermap.org/data/2.5/weather` is the endpoint  URL, and  `weather?q=Seattle&appid=YOUR_API_KEY` defines the parameters of the request, which is location and API key in this example. 
A simplified version of the response(in JSON) of such an API request would then look like 
```
{
    "coord": { "lon": -122.33, "lat": 47.61 },
    "weather": [{ "main": "Clear", "description": "Sunny" }],
    "main": { "temp": 72.5, "humidity": 50 }
}
```

### What are the three API verbs?
The API verbs provide a standardized way for clients to interact with resources, ensuring uniformity across applications. Since each verb has a specific purpose, the verbs make it easier for developers to understand the intended action. These verbs form the backbone of communication between clients and servers, enabling the creation, retrieval, and modification of resources in a structured and consistent manner.
The three fundamental API verbs commonly used in development are as follows: 
#### `GET`
Used to retrieve data from the server, without modifying any data, its purely for read only.
For example we have a server that stores weather data of different areas of a state. We can use a get request to fetch a list of the weather data as follow: 
```
GET /api/weather
```
Here `api` could be any any server, for example a local server, then the api request can be written as follows:
```
GET http://localhost:5000/weather
```  
The `GET` request will return a list of available weather data. The lists are usually returned in JSON format.   

#### `POST`
Used to create new data or resources on the server. For example, Let's say we want to add weather of another location to the server. A `POST` request can be used as follows:
```
POST http://localhost:5000/weather
Content-Type: application/json
Body:
{
  "location": "new town",
  "title": "30C"
}
``` 
This will add a new data entry to the server.
#### `PUT`
Used to update an existing resource or replace the current data with the new data provided. For example, Let's say we want to replace one of the location's on the server with another. A `PUT` request can be used as follows:
```
PUT http://localhost:5000/weather/1
``` 
The `/1` after the data selects the exact data entry we want to replace, a `GET` request can be used first to ensure the we are replacing the correct data entry. 
The new data can be updated in the Body of the `PUT` request as follows: 
```
{
  "location": "other new town",
  "title": "28C"
}
``` 
Another API verb that is often used is  `DELETE`, which is used to remove data or resource from the server. The syntax is as follows: ``` DELETE http://localhost:5000/weather/1 ```. This request will delete the first data entry from the server. 


### Is MongoDB a SQL or NoSQL database?
MongoDB is a NoSQL  type of database management system. Which means, unlike traditional SQL databases, which use tables and rows to store data, MongoDB uses a flexible, JSON-like documents. MongoDB is used for storing and managing large volumes of unstructured or semi-structured data. It's particularly well-suited for applications with rapidly evolving data requirements or where flexibility in data modeling is important. MongoDB's flexible schema allows for easy iteration and modification of data models as application requirements change.

MongoDB stores data in JSON like documents, such that data consists of key-value pairs similar to JSON objects. Fields in a document can vary, making MongoDB schema-less. Documents can also be nested to express hierarchical relationships and store arrays. Here's an example of a document in MongoDB:
```
[
  {
    _id: ObjectId('661fe0838bf7c0aedf117b7f'),
    name: 'Confident Ruby',
    startDate: ISODate('2024-04-17T14:45:23.335Z'),
    authors: [ { name: 'Avdi Grimm' } ]
  },
  {
    _id: ObjectId('661fe0838bf7c0aedf117b80'),
    title: 'The War of Arts',
    startDate: ISODate('2024-04-17T14:45:23.335Z'),
    authors: [ { name: 'Steven Pressfield' } ]
  },
  {
    _id: ObjectId('6620b6d29d3dde593e117b7c'),
    name: 'Blink',
    publishedDate: ISODate('2024-04-18T05:59:46.874Z'),
    authors: [
      { name: 'Malcolm Gladwell', active: 'true' },
      { name: 'Ghost Writer', active: 'true' }
    ]
  }
]
```
As can be seen no schema is required for objects in MongoDB and a unique id is automatically assigned to each object in the document.  
Collections in MongoDB further provide a flexible and scalable way to organize and manage related documents. Like documents, collections do not enforce a fixed schema, so documents within a single collection can have different fields and data types.
New collections are automatically created when data is stored in them for the first time, without the need to explicitly create them.
A collection can be created explicitly by using the `db.createCollection()` method.
Some common MongoDB shell commands and their functionalities are listed below:

- `show dbs` and `show collections`: list all the available databases and collections, respectively.
- `use my_database`: create and select the database to use.
- `db.createCollection('my_collection')`: create a collection.
- `db.my_collection.insertOne()` and `db.my_collection.insertMany()`: insert one or more document into the collection
- `db.my_collection.find()` and `db.my_collection.findOne()`: query to fins a document from the collection.
In Summary, MongoDB is a NoSQL database that offers flexible and scalable document-oriented approach with JSON-like syntax making it well-suited for modern application development, especially in environments with rapidly changing data requirements.

### What is Postman?
Postman is a popular tool for API development that helps developers build, test, and document APIs more efficiently. Postman provides a user-friendly interface for sending HTTP requests, viewing responses, and managing API workflows, making it easy to verify that the API is working correctly.Postman uses a graphical user interface (GUI) for creating and managing requests, so there isn't specific syntax. However these are some key features of the postman user interface.
- Collections: Groups of related API requests can be organized together in a collection and can help manage workflows of API developers.
- Request: Allows to create and send API requests (such as GET, POST, PUT, DELETE)
- Responses: Responses in Postman show the data returned by an API after sending a request. This includes the HTTP status code, headers, and body of the response.

Postman also supports scripting using JavaScript, allowing developers to add dynamic behavior to their API requests and collections, such as authentication, data manipulation, and testing. 
 
 As an example, to make a `GET` request in Postman. We would select the `GET` verb in the request panel and provide the endpoint API URL like `https://pokeapi.co/api/v2/pokemon/ditto`. If everything is working correctly the Postman UI will display the HTTP response status code `200 (OK)` indicating that the request has been processed successfully on the server. 
For a `GET` request in particular, it means that the requested resource has been fetched and transmitted in the message body. The response in the body will look something like this (partial response shown here)
```
{
  "abilities": [
    {
      "ability": {
        "name": "limber",
        "url": "https://pokeapi.co/api/v2/ability/7/"
      },
      "is_hidden": false,
      "slot": 1
    },
    {
      "ability": {
        "name": "imposter",
        "url": "https://pokeapi.co/api/v2/ability/150/"
      },
      "is_hidden": true,
      "slot": 3
    }
  ]
}
```
### What is polymorphism?

Polymorphism means “many forms”. In programming, it refers to the ability of different objects or classes to share the same method name but behave differently based on their specific context. Polymorphism  is a fundamental concept in object-oriented programming (OOP). 
Polymorphism is mainly used in OOP to increase code reausability as it allows programmers to reuse code across different classes, reducing redundancy and promoting modular design. It also enables programmers to write more flexible and adaptable code that can accommodate changes in requirements or the addition of new classes. 
Polymorphism in Python can be achieved through inheritance, where child classes redefines methods inherited from parent classes to provide specialized behavior.  Let’s create a parent class called `Vehicle` and make `Car`, `Boat`, and `Plane` its child classes. The child classes not only inherit the `move()` method but can also override it:
```python
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
for x in (car1, boat1, plane1):
    print(x.brand, x.model)
    x.move()
```

##### OUTPUT
```
Ford Mustang
Drive!
Ibiza Touring 20
Sail!
Boeing 747
Fly!
````
n this example, the child classes inherit properties and methods from the parent class `Vehicle`. The `Boat` and `Plane` classes override the `move()` method, demonstrating the power of polymorphism.

Polymorphism can also be achieved by creating functions can can take any  object. For example the Python provides built-in functions that demonstrate polymorphism. For example, the `len` function in python returns the length or the number of items in an object and can be used with various data types such as strings, lists, tuples, and dictionaries. Similarly users can also define their own polymorphic functions. For example let's define an `add` function 
```python
def add(x, y, z=0):
    return x + y + z


print(add(6, 4))
print(add(6, 4, 6))
```
##### OUTPUT
```
10
16
```
Here, the add function provides the flexibility to use the same function  to handle both two-operand and three-operand addition.

### What is a dunder method?

Dunder methods ("double underscore" methods) are special methods in Python that start and end with double underscores (__) which allows to deeply customize the behaviour of objects in Python. One of the primary advantages of using dunder methods is that they provide a simple way to make objects behave like built-in types, enabling developers to avoid complex and nonstandard ways of performing basic operators.  By defining dunder methods in custom classes, developers can control how instances of their classes behave in different contexts. The three most common dunder methods are `__init__` and `__repr__`.

##### `__init__` Method 
The `__init__()` method works as an initializer because it allows you to  initialize the object's attributes or perform any setup that's necessary before the object can be used. It essentially sets up the initial state of an object. For example let's define a `Person` class:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Tom", 25)
person2 = Person("Tina", 30)
print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
```
##### OUTPUT
```
Tom
25
Tina
30
```
The ` `function is called automatically whenever a new object of the class is created. In this example the `__init__` method takes two parameters: `name` and `age`. Whenever a new Person object is created, and values for these parameters is provided, the `self.name` and `self.age` assigns the values to the `name` and `age` attribute of the object. The `__init__` method plays a crucial role in object-oriented programming by facilitating object initialization and customization.

##### `__repr__` Method 
Answer
The `__repr__` function in Python is a special method used to represent objects of a class as strings. The primary purpose of `__repr__` is to assist developers in debugging and maintaining code by offering a clear and informative view of the object. Lets look at an example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


person1 = Person("Tom", 25)
print(repr(person1))
```
##### OUTPUT
```
Person(name=Tom, age=25)
```
In these examples, the `__repr__ ` method is defined within the class `Person` to provide a string representation of the object's attributes. Similar to the `__repr__` method, th `__str__` method can also be used to return a string representation of an object. The difference being that the `__repr__` is essential for debugging, logging, and understanding the state of an object, while `__str__` focuses more on human readability.


### What is a python decorator ?
Python decorators are functions that take another function as an argument and extend their functionality without changing their core definition. Decorators are denoted by the `@decorator_name` symbol placed above the function definition, provideing a clean and concise way to modify or extend the behavior of functions without altering their original code. Let's look at an example:
```python
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello, I am a decorated function.")


say_hello()
```
##### OUTPUT
```
Before the function is called.
Hello, I am a decorated function.
After the function is called
```

In this example, `@my_decorator` is a simple decorator that wraps the `say_hello()` function. The `wrapper()` function inside `my_decorator` adds behavior before and after calling the `say_hello()` function. Python decorators are often used to add functionalities like logging, timing, and authentication, etc, without modifying the original function. Let's look at a practical example:
```python

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


print(calculate_square([8, 6, 4]))
```
##### OUTPUT
```
Execution time for calculate_square: 4.0531158447265625e-06 seconds
[64, 36, 16]
```

Here, the `@time_it` decorator calculates the execution time of the `calculate_square` function. The decorator function wraps around `calculate_square`, executes code to record the start and end times, and prints the execution time.

Decorators are a key concept in Python programming that can significantly improve the structure and functionality of your code. By understanding decorators, developers can write more efficient and maintainable Python code.





