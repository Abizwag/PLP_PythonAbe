# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        return f"Calling {number} using {self.brand} {self.model}."

    def charge(self, hours):
        self.battery_life += hours * 2  # simple charging logic
        return f"Charged for {hours} hours. Battery life now {self.battery_life} hours."

    def __str__(self):
        return f"{self.brand} {self.model} with {self.battery_life}h battery"

# Inherited class with extended behavior (inheritance + encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu_model):
        super().__init__(brand, model, battery_life)
        self.gpu_model = gpu_model

    def play_game(self, game_name):
        self.battery_life -= 2  # gaming drains battery faster
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu_model} GPU."

    # Override __str__ method (polymorphism)
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, GPU: {self.gpu_model}"

# Usage
phone = Smartphone("Samsung", "Galaxy S21", 20)
gaming_phone = GamingPhone("ASUS", "ROG Phone 5", 15, "Adreno 660")

print(phone.call("123-456-7890"))
print(phone.charge(3))
print(phone)

print(gaming_phone.play_game("Call of Duty"))
print(gaming_phone.charge(1))
print(gaming_phone)
