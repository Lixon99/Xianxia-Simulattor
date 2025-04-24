import random
from enemy import EnemyAI
from errorHandling import errorHandling

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

class Player(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.energy_blast_uses = 0
        self.max_energy_blast_uses = 2

class Enemy(EnemyAI):
    def __init__(self, name, hp, attack):
        stats = {
            'Health': hp,
            'Strength': attack,
            'Defense': 2, 
            'Energy': 15  
        }
        super().__init__(name, stats)

# Kamp function
@errorHandling
def fight(player, enemy):
    while player.hp > 0 and enemy.stats['Health'] > 0:
        # Spillerens tur
        print("\nAvailable moves:")
        print("1. Punch (3 damage)")
        print("2. Block (defense)")
        print(f"3. Energy Blast (8 damage) - {player.max_energy_blast_uses - player.energy_blast_uses} left")
        print("4. Heal (5 HP)")
        
        choice = input("Choose your move (1-4): ")
        
        if choice == "1":  # Punch
            enemy_move = enemy.chooseMove()
            if enemy_move and enemy_move.get("name") == "dodge":
                print("Enemy dodged your punch!")
            else:
                if enemy_move and enemy_move.get("name") == "block":
                    print("Enemy blocked your punch and stunned you!")
                    # Player stunned næste tur
                else:
                    enemy.stats['Health'] -= 3
                    print(f"You punched enemy for 3 damage!")
        
        elif choice == "2":  # Block
            print("You prepare to block!")
            # Block logik her
            
        elif choice == "3":  # Energy Blast
            if player.energy_blast_uses >= player.max_energy_blast_uses:
                print("You can't use Energy Blast anymore this fight!")
                continue
                
            enemy_move = enemy.chooseMove()
            if enemy_move and enemy_move.get("name") == "dodge":
                print("Enemy dodged your energy blast!")
            else:
                damage = 8
                if enemy_move and enemy_move.get("name") == "block":
                    damage = int(damage * 1.5)
                    print(f"Enemy blocked but took 1.5x damage! Dealt {damage} damage!")
                else:
                    print(f"You used Energy Blast for {damage} damage!")
                enemy.stats['Health'] -= damage
                player.energy_blast_uses += 1
                
        elif choice == "4":  # Heal
            player.hp += 5
            print(f"You healed for 5 HP!")
        
        else:
            print("Invalid choice. Try again.")
            continue

        # Fjendens tur (hvis ikke død)
        if enemy.stats['Health'] > 0:
            enemy_move = enemy.chooseMove()
            if enemy_move is None:
                print("Enemy is stunned and can't move!")
            elif enemy_move.get("name") == "dodge":
                print("Enemy dodged!")
            else:
                if enemy_move["name"] == "punch":
                    damage = enemy_move["damage"]
                    # Tjek om player blokerede
                    if choice == "2":  # Player blokerede
                        print("You blocked enemy's punch and stunned them!")
                        # Enemy stunned næste tur
                    else:
                        player.hp -= damage
                        print(f"Enemy punched you for {damage} damage!")
                
                elif enemy_move["name"] == "slash":
                    damage = enemy_move["damage"]
                    if choice == "2":  # Player blokerede
                        damage = int(damage * 1.5)
                        print(f"Enemy slashed through your block for {damage} damage!")
                    else:
                        print(f"Enemy slashed you for {damage} damage!")
                    player.hp -= damage
                
                elif enemy_move["name"] == "block":
                    print("Enemy is blocking!")

        # Vis status
        print(f"\nPlayer HP: {player.hp}")
        print(f"Enemy HP: {enemy.stats['Health']}")

    # Kamp resultat
    if player.hp <= 0:
        print("You were defeated!")
    else:
        print("You defeated the enemy!")

if __name__ == '__main__':
    player = Player("Player", 30, 5)
    enemy = Enemy("Enemy", 20, 3)
    fight(player, enemy)