"""Task 4"""


class Car:
    """Car class"""

    def __init__(self, make, year, speed):
        self.make = make
        self.year = year
        self.speed = speed
        Showroom.all_cars.append(self)

    def __str__(self):
        return f"Make: {self.make}, year: {self.year}, speed: {self.speed}"

    def __repr__(self):
        return f"Make: {self.make}, year: {self.year}, speed: {self.speed}"


class Showroom:
    """Showroom class"""

    all_cars = []

    @staticmethod
    def show_all_cars() -> str:
        """Print all available cars"""
        if not Showroom.all_cars:
            return "Sorry we don't have any cars"

        return f"You can buy cars from the list: {Showroom.all_cars}"



    @staticmethod
    def buy_car(car) -> None:
        """Delete car from the cars list"""
        if car in Showroom.all_cars:
            print("Congrats! You bought: ", car)
            Showroom.all_cars.remove(car)


first_car = Car("Nissan", 2014, 180)
second_car = Car("Suzuki", 2018, 280)
third_car = Car("Tesla", 2023, 470)


print(Showroom.all_cars)

Showroom.buy_car(first_car)

print(Showroom.all_cars)
