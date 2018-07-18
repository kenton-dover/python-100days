

class Monster:
    def __init__(self, name, health, lvl, kind):
        self.name = name
        self.health = health
        self.lvl = lvl
        self.kind = kind

    def attack(self, defendingKind):
        damage = self.lvl
        if self.kind == "FIRE" and defendingKind == "GRASS":
            damage = damage * 2
        elif self.kind == "WATER" and defendingKind == "FIRE":
            damage = damage * 2
        elif self.kind == "GRASS" and defendingKind == "WATER":
            damage = damage * 2
        elif self.kind == "WATER" and defendingKind == "GRASS":
            damage = damage * .5
        elif self.kind == "GRASS" and defendingKind == "FIRE":
            damage = damage * .5
        elif self.kind == "FIRE" and defendingKind == "WATER":
            damage = damage * .5
        return damage

    def defense(self, damageDone):
        if self.health <= damageDone:
            self.health = 0
        elif self.health > damageDone:
            self.health = self.health - damageDone
