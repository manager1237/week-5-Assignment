class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = 100  # default battery percentage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%.")

    def use(self, hours):
        self.battery = max(0, self.battery - (hours * 10))
        print(f"{self.brand} {self.model} used for {hours}h, battery at {self.battery}%.")


# Derived class (Inheritance)
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        # Call the parent constructor
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    # Polymorphism: redefine method
    def use(self, hours):
        self.battery = max(0, self.battery - (hours * 7))  # more efficient battery use
        print(f"{self.brand} {self.model} (Pro) used for {hours}h, battery at {self.battery}%.")

    def take_photo(self):
        if self.battery > 5:
            self.battery -= 5
            print(f"📸 {self.brand} {self.model} took a {self.camera_megapixels}MP photo. Battery at {self.battery}%.")
        else:
            print("Battery too low to take a photo!")


# Testing the classes
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone2 = SmartPhonePro("Apple", "iPhone 15 Pro", 256, 48)

phone1.make_call("123-456-789")
phone1.use(3)
phone1.charge(20)

phone2.make_call("987-654-321")
phone2.take_photo()
phone2.use(3)
phone2.charge(15)


# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")


# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

