class Animals:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    def make_sound(self):
        print("generic sound")

class Mammal(Animals):
    pass

class Lion(Mammal):
    def make_sound(self):
        print(f"{self.name} the Lion, aged {self.age}, makes a roar!")

class Elephant(Mammal):
    def make_sound(self):
            print(f"{self.name} the elephant, his age is {self.age}, makes a tott!")


class Bird(Animals):
    pass
class Eagle(Bird):
    def make_sound(self):
        print(f"{self.name} the bold Eagle, his age is {self.age}, makes a hell yeah merica sound!")

class Parrot(Bird):
    def make_sound(self):
         print(f"{self.name} the Parrot, his age is {self.age}, copies the Egale  and says hell yeah merica!")


lion = Lion("simba", 5)
elephant = Elephant("dambo", 10)
parrot = Parrot("spike", 3)
egale = Eagle("merica", 10)


lion.make_sound()
elephant.make_sound()
parrot.make_sound()
egale.make_sound()