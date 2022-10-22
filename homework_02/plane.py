"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions



class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value : int):
        if self.max_cargo < self.cargo + value:
            raise exceptions.CargoOverload
        else:
            self.cargo += value

    def remove_all_cargo(self) -> int:
        cargo = self.cargo
        self.cargo = 0
        return cargo