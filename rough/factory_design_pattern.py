from abc import ABC, abstractmethod

class Coffe(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Latte(Coffe):
    def prepare(self):
        print("Latte is prepared")

class Cappuccino(Coffe):
    def prepare(self):
        print("Cappuccino is prepared")

class CoffeeFactory:
    def create_coffee(self, coffee_type):
        if coffee_type == "latte":
            return Latte()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Invalid coffee type")

factory = CoffeeFactory()
