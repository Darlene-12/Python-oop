# Base class
class Vehicle:
    def move(self):
        pass

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Example usage
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
