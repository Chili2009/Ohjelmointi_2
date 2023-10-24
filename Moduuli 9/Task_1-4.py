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

""""
Toyota = Car("ABC-1", 142)
Toyota.print_info()
Toyota.accelerate(30)
Toyota.accelerate(70)
Toyota.accelerate(50)
Toyota.print_info()
Toyota.accelerate(-200)
Toyota.traveled(1.5)
Toyota.print_info()

"""
cars = []
for i in range(10):         #str muuttaa kokonaisluvun
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
    print(car.print_info())


















