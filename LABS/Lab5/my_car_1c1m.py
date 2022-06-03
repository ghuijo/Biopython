# my_car_1c1m

from car_1c1m import Car

new_car = Car("audi", "a4", 2016)
print(new_car.get_descriptive_name())

new_car.odometer_reading = 23
new_car.read_odometer()


# my_electric_car

from car_3c1m import ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2016)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# my_cars1

import car_3c1m

my_beetle = car_3c1m.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_3c1m.ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())


# my_cars2

from car_3c1m import *

my_beetle = car_3c1m.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_3c1m.ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())

