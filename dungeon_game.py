import random
import time



# ------------------ PLAYER CLASS ------------------

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100
        self.energy = 100
        self.gold = 20
        self.inventory = []

        if role == "Warrior":
            self.attack = 15
            self.defense = 10
        elif role == "Mage":
            self.attack = 20
            self.defense = 5
        else:
            self.attack = 10
            self.defense = 8
        
    def show_stats(self):
        print("\n===== PLAYER STATS =====")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"HP: {self.hp}")
        print(f"Energy: {self.energy}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")
        print("========================\n")


# ------------------ ENEMY CLASS ------------------

class Enemy:
    def __init__(self):
        self.hp = random.randint(40,80)
        self.attack = random.randint(8,18)


# ------------------ GAME FUNCTIONS ------------------

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def fighht(player):
    enemy = Enemy()
    slow_print("\n⚔️ An enemy appears!")

    while enemy.hp > 0 and player.hp > 0:
        print(f"\nEnemy HP: {enemy.hp}")
        print(f"Your HP: {player.hp}")

        choice+ input("1. Attack\n2. Run\nChoice: ")

        if choice == "1":
            damage = player.attack + random.randint(-3, 5)
            enemy.hp -=damage 
            print(f"You deal {damage} damage!")

            if enemy.hp > 0:
                enemy_damage = enemy.attack - player.defense
                enemy_damage = max(0, enemy_damage)
                player.hp -= enemy_damage 
                print(f"Enemy hits you for {enemy_damage} damage!")
                
            elif choice == "2":
                if random.random() < 0.5:
                    print("You escaped successfully!")
                    return
                else:
                    print("Escape failed!")
                    player.hp -= enemy.attack

    if player.hp <= 0:
        slow_print("💀 You died...")
        exit()

    slow_print("🏆 You defeated the enemy!")
    reward = random.randint(10,30)
    player.gold +=reward
    print(f"You found {reward} gold!")


def explore(player):
    event = random.choice(["fight", "treasure", "nothing"])