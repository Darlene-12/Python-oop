# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_specs(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours of battery life."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

# Derived class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def display_specs(self):
        # Overriding the base method to add cooling system info
        return super().display_specs() + f" Equipped with a {self.cooling_system} cooling system."

    def game_mode(self):
        return f"{self.brand} {self.model} is now in gaming mode with enhanced performance."

# Example usage
basic_phone = Smartphone("Apple", "iPhone 14", 128, 20)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, 30, "liquid")

print(basic_phone.display_specs())  # Apple iPhone 14 with 128GB storage and 20 hours of battery life.
print(basic_phone.charge())         # Apple iPhone 14 is charging.

print(gaming_phone.display_specs()) # Asus ROG Phone 6 with 512GB storage and 30 hours of battery life. Equipped with a liquid cooling system.
print(gaming_phone.game_mode())     # Asus ROG Phone 6 is now in gaming mode with enhanced performance.
