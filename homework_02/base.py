from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started : bool = False

    def __init__(self, weight=5,  fuel=60, fuel_consumption=2):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started :
            pass
        else :
            if self.fuel <= 0:
                raise exceptions.LowFuelError
            else :
                self.started = True

    def move(self, dist : int):
        if self.fuel < self.fuel_consumption * dist:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel -= self.fuel_consumption * dist