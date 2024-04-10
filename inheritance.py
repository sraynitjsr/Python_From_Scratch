class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())
