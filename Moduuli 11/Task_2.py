import random

class Car:
    def __init__(self, register_Number, top_Speed):
        self.register_Number = register_Number
        self.top_Speed = top_Speed
        self.velocity = 0
        self.traveled_Distance = 0

    def print_info(self):
        print(f"Auton {self.register_Number} "
              f"huippunopeus {self.top_Speed} km/h "
              f"tämänhetkinen nopeus {self.velocity} km/h "
              f"kuljettu matka {self.traveled_Distance} km/h ")

    def accelerate(self, speed_Change):
        if 0 < self.velocity + speed_Change < self.top_Speed:
            self.velocity = self.velocity + speed_Change
        elif self.velocity + speed_Change <= 0:
            self.velocity = 0
        elif self.velocity + speed_Change > self.top_Speed:
            self.velocity = self.top_Speed

    def traveled(self, hours):
        self.traveled_Distance = self.velocity * hours + self.traveled_Distance

class ElectricCar(Car):
    def __init__(self, register_Number, top_Speed, battery_Capacity):
        super().__init__(register_Number, top_Speed)
        self.battery_Capacity = battery_Capacity

class GasolineCar(Car):
    def __init__(self, register_Number, top_Speed, fuel_Tank_Size):
        super().__init__(register_Number, top_Speed)
        self.fuel_Tank_Size = fuel_Tank_Size
    def print_info(self):
        super().print_info()
        print(f"")
# The corrected for loop with a closing parenthesis
cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

stop = False
while not stop:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.traveled(1)
        if car.traveled_Distance >= 10000:
            stop = True
            break

for car in cars:
    car.print_info()

electric_car = ElectricCar("JKW-15", 180, 52.5)
gasoline_car = GasolineCar("LFI-123", 165, 32.3)

electric_car.accelerate(150)
gasoline_car.accelerate(140)

for _ in range(3):
    electric_car.traveled(1)
    gasoline_car.traveled(1)

electric_car.print_info()
gasoline_car.print_info()
