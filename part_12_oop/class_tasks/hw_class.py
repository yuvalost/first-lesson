class Entity:
    def __init__(self, attack:int):
        self.attack = attack
    def preform_attack(self):
        print(f"Attacking with {self.attack} damage")


class Monster(Entity):
    def __init__(self,attack:int, health:int, damage:int):
        super().__init__(attack)
        self.health = health
        self.damage = damage

    def damage_take_from_attack(self):
        print(f"A monster with {self.health-self.attack} health. ")

att = Entity(10)
dam = Monster(10,110,200)

att.preform_attack()
dam.damage_take_from_attack()