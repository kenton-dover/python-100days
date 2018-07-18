from monters import Monster
import random


def getPlayerMove():
    return input("Do you want to [A]ttack or [R]un: ")


def gameLoop(playerMonster, monsters):
    while monsters and playerMonster.health != 0:
        monster = random.choice(monsters)
        print(
            f"A lvl {playerMonster.lvl} {playerMonster.name} found a lvl {monster.lvl} {monster.name}")
        move = getPlayerMove()
        if move is "A":
            damage = playerMonster.attack(monster.kind)
            monster.defense(damage)
            print(
                f"{playerMonster.name} did {damage}. {monster.name} has {monster.health} health left")
            if monster.health > 0:
                damage = monster.attack(playerMonster.kind)
                playerMonster.defense(damage)
                print(
                    f"{monster.name} did {damage}. {playerMonster.name} has {playerMonster.health} health left")
            else:
                print(f"{monster.name} has fainted!")
                monsters.remove(monster)
        elif move is "R":
            continue


def buildOpponents():
    listOfMonsters = []
    listOfMonsters.append(Monster("Bulbasaur", 15, 5, "GRASS"))
    listOfMonsters.append(Monster("Charmander", 15, 5, "FIRE"))
    listOfMonsters.append(Monster("Squirtle", 15, 5, "WATER"))
    return listOfMonsters


def getPlayerMonster():
    name = input("Please enter a name: ")
    health = int(input("Please enter amount of health: "))
    lvl = int(input("Please enter the lvl: "))
    kind = input("Please enter a kind: ")

    return Monster(name, health, lvl, kind)


def print_header():
    print("---------------------------------")
    print("           Monster Game          ")
    print("---------------------------------")
    print()


def main():
    print_header
    playerMonster = getPlayerMonster()
    monsters = buildOpponents()
    gameLoop(playerMonster, monsters)


if __name__ == '__main__':
    main()
