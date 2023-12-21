class MyCar:
    year = 2023
    brand = "Tesla"

    def car_drive(self):
        print("Car is driving")

    def go_faster(self, max_speed: int):
        print("Accelerate up to ", max_speed)

    # def happy_meal(self, what_meal_do_you_want: input()):
    #     print("what happy meal you want? ", what_meal_do_you_want)


#
tesla = MyCar()
print(type(tesla))

print(tesla.year)
print(tesla.brand)
print(type("Alex"))
tesla.car_drive()
tesla.go_faster(230)
# tesla.happy_meal(chips)