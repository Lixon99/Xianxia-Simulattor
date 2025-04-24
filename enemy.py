import random
from errorHandling import errorHandling

class EnemyAI:
    def __init__(self, name, stats):
        self.stats: dict = stats
        self.name: str = name
        self.stunned = False
    
    @errorHandling
    def chooseMove(self):
        # Hvis stunned, kan ikke angribe
        if self.stunned:
            self.stunned = False
            return None
        
        # 10% chance for at dodge (spærcialevne)
        if random.random() < 0.1:
            return {"name": "dodge", "effect": "dodge"}
        
        # Vælg move baseret på sandsynligheder
        rand = random.random()
        if rand < 0.4:
            return {"name": "punch", "damage": self.stats['Strength'], "energyCost": 1}
        elif rand < 0.8:
            return {"name": "slash", "damage": int(self.stats['Strength'] * 1.2), "energyCost": 2}
        else:
            return {"name": "block", "defenseBonus": 2, "energyCost": 1}

    def __str__(self) -> str:
        return f'Enemy stats: {self.stats}'

if __name__ == '__main__':
    # Eksempel på brug
    enemy = EnemyAI('Qi Cultivator', 
                   {'Health': 20, 'Strength': 5, 'Defense': 4, 'Energy': 15})
    
    # Test enemy moves
    for _ in range(10):
        move = enemy.chooseMove()
        if move:
            print(f"{enemy.name} chooses {move['name']}")
        else:
            print(f"{enemy.name} is stunned and skips turn")