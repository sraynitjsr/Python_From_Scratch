# 1. Variables and Data Types
name = "Rajesh"
age = 25
is_student = True
height = 5.9

# 2. Basic Input/Output
print("Namaste,", name)
age = int(input("Apki umar kya hai? "))
print("Aap", age, "saal ke hain.")

# 3. Conditional Statements
if age >= 18:
    print("Aap bade ho.")
else:
    print("Aap chhote hain.")

# 4. Loops
for i in range(5):
    print("Daur", i+1)

# 5. Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["seb", "kela", "santra"]

# 6. List Operations
print("Numbers ki lambai:", len(numbers))
print("3 ki shreni numbers me:", numbers.index(3))
print("4 ki ginta numbers me:", numbers.count(4))

# 7. Tuple
coordinates = (10, 20)

# 8. String Operations
message = "Namaste, Duniya!"
print("Pehle paanch akshar:", message[:5])
print("Aakhri paanch akshar:", message[-5:])
print("Message ki lambai:", len(message))
print("Uppercase:", message.upper())

# 9. Dictionary
person = {"naam": "Anita", "umar": 30, "shahar": "Mumbai"}

# 10. Dictionary Operations
print("Keys:", person.keys())
print("Values:", person.values())
print("Person ki umar:", person["umar"])

# 11. Functions
def greet(name):
    print("Namaste,", name)

greet("Anita")

# 12. Function with return
def add(a, b):
    return a + b

result = add(3, 5)
print("Jodne ka parinaam:", result)

# 13. Classes
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
print("Mera car:", my_car.make, my_car.model)

# 14. Class Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

my_electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
print("Electric car battery capacity:", my_electric_car.battery_capacity)

# 15. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Zero se bhag nahi kiya ja sakta.")

# 16. File Handling
with open("example.txt", "w") as f:
    f.write("Yeh ek udaharan fail hai.")

with open("example.txt", "r") as f:
    content = f.read()
    print("File ka content:", content)

# 17. Importing Modules
import math
print("Pi ki maan:", math.pi)

# 18. Lambda Functions
square = lambda x: x * x
print("5 ka square:", square(5))

# 19. List Comprehensions
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# 20. Generators
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_sequence = fibonacci(10)
print("Fibonacci Sequence:", list(fib_sequence))

# 21. Set
my_set = {1, 2, 3, 4, 5}
my_set = {4, 5, 6, 7, 8}

# 22. Set Operations
print("Union:", my_set.union(my_set))
print("Intersection:", my_set.intersection(my_set))

# 23. Decorators
def decorator(func):
    def wrapper():
        print("Function ka pahle hissa")
        func()
        print("Function ka baad ka hissa")
    return wrapper

@decorator
def say_hello():
    print("Namaste!")

say_hello()
