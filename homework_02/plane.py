"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo: int):
        if new_cargo + self.cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += new_cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
