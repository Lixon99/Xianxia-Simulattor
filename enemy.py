import random
from errorHandling import errorHandling

# Denne fil håndterer fjendens AI
class EnemyAI:
    def __init__(self, name, stats, strategies, allMoves):
        self.stats: dict = stats
        self.name: str = name
        self.strategies = strategies
        self.allMoves: list = allMoves
    
    @errorHandling
    def chooseMove(self, playerAction, randomness=0.3): # Vælg tilfældig træk
        if random.random() < randomness: 
            return random.choice(list(self.allMoves.values()))
        
        # Vælg en strategi, hvis den eksister i variable strategies 
        if playerAction in self.strategies:
            strategyMoves = [self.allMoves[move] for move in self.strategies[playerAction]]
            return random.choice(strategyMoves)
        return random.choice(list(self.allMoves.values()))

    def __str__(self) -> str:
        return f'Enemy stats: {self.stats}'

allMoves = {
    "punch": {"name": "punch", "damage": 3, "energyCost": 1}, 
    "block": {"name": "block", "defenseBonus": 2, "energyCost": 1}, 
    "energyblast": {"name": "energyblast", "damage": 8, "energyCost": 3}, 
    "heal": {"name": "heal", "healAmount": 5, "energyCost": 2}
}

strategies = {
    "attack": ["punch", "block", "dodge"],
    "defense": ["punch", "energyblast", "heal"],
}

if __name__ == '__main__':
    # Lave en fjend objekt
    enemy = EnemyAI('Qi Cultivator', 
                    stats={'Health': 10, 'Strength': 10, 'Defense': 10, 'Energy': 10}, 
                    strategies=strategies, allMoves=allMoves )

    playerAction = "defense"
    aiMove = enemy.chooseMove(playerAction)
    print(f'{enemy.name} choose to use {aiMove["name"]}')
    print(f'It cost {aiMove["energyCost"]} energy')
