class my_boy:


    def __init__(self, name, age, hair):
        self.name = name
        self.age = age
        self.hair = hair

    def line(self):
        print(f"my boy {self.name}, who has a nice {self.hair} hair, his age is {self.age}")

boy = my_boy("john", 23, "blond")
# tesla.print_car_info()

boy.line()

print("")
print("-"*100)

class hotday(my_boy):

    def __init__(self, weather, girl, sunglass):
        super().__init__(weather, girl, sunglass)
        self.weather = weather
        self.girl = girl
        self.sunglass = sunglass

        print(f"on my holiday the, {self.weather} and this girl named {self.girl}, she had w")

class car(my_boy):
    def __init__(self,car1, car2, car3):
        super().__init__(car1, car2, car3)
        self.car1 = car1
        self.car2 = car2
        print(f"i drive {car1} or {car2}")

a1 = my_boy("yuval", 32, "brown")
a2 = hotday("clear skies", "betty", "ray band")
a3 = car("bmw","ferri", "honda")

objects = [a1, a2, a3]

for item in objects:
    item.line()
