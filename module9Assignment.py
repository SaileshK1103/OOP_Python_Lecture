# 1. Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.
'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return (
            f"The registration number of car is {self.registration_number}, maximum speed {self.maximum_speed}, current speed {self.current_speed}, travelled distance {self.travelled_distance}"
        )
# main program
car1 = Car("ABC-123", 142)
car2 = Car("XYZ-123", 142)
print(car1)
print(car2)

'''
from random import random, randint

# 2.  Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return (
            f"The registration number of car is {self.registration_number}, \n"
            f"maximum speed {self.maximum_speed}, \n"
            f"current speed {self.current_speed}, \n"
            f"travelled distance {self.travelled_distance}"
        )
    def accelerate(self, changeSpeed):
        self.current_speed += changeSpeed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed += 0

# main program
car1 = Car("ABC-123", 142)
car2 = Car("XYZ-123", 142)
print(car1)
car1.accelerate(30)
print(f"Speed of car increased by +{car1.current_speed}")
car1.accelerate(50)
print(f"Speed of car increased by +{car1.current_speed}")
car1.accelerate(70)
print(f"Speed of car increased by +{car1.current_speed}")
car1.accelerate(-200)
print(f"emergency brake {car1.current_speed}")
'''

# 3. Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.
'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return (
            f"The registration number of car is {self.registration_number}, \n"
            f"maximum speed {self.maximum_speed}, \n"
            f"current speed {self.current_speed}, \n"
            f"travelled distance {self.travelled_distance}"
        )
    def accelerate(self, changeSpeed):
        self.current_speed += changeSpeed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed += 0

    def drive(self, hours):
        self.travelled_distance = 2000
        self.travelled_distance += self.current_speed * hours

# main program
car = Car("ABC-123", 142)
print(car)
car.accelerate(60)
print(f"Speed of car increased by +{car.current_speed}")
car.drive(1.5)
print(f"The travelled distance is {car.travelled_distance}")
'''

# 4. Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
# One per every hour of the race, the following operations are performed:
    # The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
    # This is done using the accerelate method.
    # Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.
'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def __str__(self):
        return (
            f"The registration number of car is {self.registration_number}, \n"
            f"maximum speed {self.maximum_speed}, \n"
            f"current speed {self.current_speed}, \n"
            f"travelled distance {self.travelled_distance}"
        )
    def accelerate(self, changeSpeed):
        self.current_speed += changeSpeed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed += 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# main program

cars = [Car(f"ABC-{i+1}", randint(100,200)) for i in range(10)]
#Race loop until one car reaches 10,0000 Km
race_in_progress = True
hours_passed = 0
while race_in_progress:
    # Each hour: adjust speed and drive for one hour
    for car in cars:
        # Change speed randomly between -10 and +15
        changeSpeed = randint(-10,15)
        car.accelerate(changeSpeed)
        # Drive for 1 hour
        car.drive(1)
        # Check if any car has reached 10,000 Km
        if car.travelled_distance >= 10000:
            race_in_progress = False
            break
        hours_passed += 1

print(f"\n{'Registration':<15}{'Max Speed (Km/h)':<20}{'Current Speed (Km/h)':<20}{'Travelled Distance (km)':<20}")
print("=" * 75)
for car in cars:
        print(f"{car.registration_number:<15}{car.maximum_speed:<20}{car.current_speed:<20}{car.travelled_distance:<20.1f}")
'''


