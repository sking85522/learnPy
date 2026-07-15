# यह फ़ाइल ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग (OOP) के कॉन्सेप्ट सिखाती है।

class Car:
    # Constructor: जब भी कार का ऑब्जेक्ट बनेगा, यह फंक्शन अपने आप चलेगा
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    # Class Method
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} की गति अब {self.speed} km/h है।")

    def brake(self):
        self.speed = 0
        print(f"{self.brand} रुक गई है।")

# ऑब्जेक्ट्स बनाना
my_car = Car("Tata", "लाल")
friend_car = Car("Mahindra", "काला")

print(f"मेरी कार {my_car.color} रंग की {my_car.brand} है।")

# मेथड्स का उपयोग
my_car.accelerate(50)
my_car.accelerate(20)
my_car.brake()
