class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car = Car("Toyota", "Corolla")
print(car.brand)
print(car.model)
car.display_info()
