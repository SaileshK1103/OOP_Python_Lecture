# 1. Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes.
# Create a print_information method to both subclasses for printing out all information of the publication in question.
# In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages).
# Print out all information of both publications using the methods you implemented.

'''
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"Book Title: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine Title: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

# main program
magazine = Magazine("Donald Duck", "AKi Hyppä")
book = Book("Compartment No 6", "Rosa Liksom", 192)
print("\nMagazine Information:")
magazine.print_information()
print("\nBook Information:")
book.print_information()
'''
from random import randint


# 2. Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as
# its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car
# (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of
# their kilometer counters.

'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed += 0
        else:
            self.current_speed = new_speed


    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_Volume = tank_volume
class Race:
    def __init__(self, name, distance_km,cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            # Random change in speed
            speed_change = randint(-10,15)
            car.accelerate(speed_change)
            # Each car drive for 1 hour
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':<12} {'Max Speed':<12} {'Current Speed':<15} {'Travelled Distance':<20}")
        print("="*60)
        for car in self.cars:
            print(f"{car.registration_number:<12} {car.maximum_speed:<12} {car.current_speed:<15} {car.travelled_distance:<20}")

    def race_finished(self):
        # Check if any car has travelled the required race distance
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
            else:
                return False
# main program
electric_car = ElectricCar("ABC-15", 180,52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(130)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car (Registration: {electric_car.registration_number}) - Travelled Distance: {electric_car.travelled_distance} km")
print(f"Gasoline Car (Registration: {gasoline_car.registration_number}) - Travelled Distance: {gasoline_car.travelled_distance} km")

cars = [Car(f"ABC-{i+1}", randint(100,200)) for i in range(10)]
# Create a race with an 8000-kilometer distance
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while  not race.race_finished():
    race.hour_passes()
    hours += 1
    # print status every 10 hours
    if hours % 10 == 0:
        print(f"\n--- Status after {hours} hours ---")
        race.print_status()
#Final status printout at the end of the race
print(f"\n--- Final Status  after {hours} hours ---")
race.print_status()
'''