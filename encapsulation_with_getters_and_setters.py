class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def display_info(self):
        print(f"Brand: {self.__brand}, Model: {self.__model}")

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

car = Car("Toyota", "Corolla")
print(car.get_brand())
car.set_brand("Honda")
print(car.get_brand())
