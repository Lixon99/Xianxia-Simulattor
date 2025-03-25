import pyinputplus as pyip
from errorHandling import errorHandling

# Denne fil håndterer spillerens stats
class PlayerStats:
    def __init__(self, health, strength, defense, speed, energy) -> int:
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.energy = energy
    
    @errorHandling
    def __str__(self) -> str:
        return f'''
        Player Stats
        Health: {self.health}
        Strength: {self.strength}
        Defense: {self.defense}
        Speed: {self.speed}
        Energy: {self.energy}
        '''
    
    @errorHandling
    def statsMultiplier(self, value: str) -> int:
        while True:
            value = pyip.inputStr("Input a value from player's stats to multiply by: ")
            value = value.lower()
            match value:
                case 'health':  
                    print('Multiplying health...')
                    self.health *= 2
                    return f'Updated health: {self.health}' 
                case 'strength':
                    print('Multiplying strength...')
                    self.strength *= 2
                    return f'Updated strength: {self.strength}'
                case 'defense':
                    print('Multiplying defense...')
                    self.defense *= 2
                    return f'Updated defense: {self.defense}'
                case 'speed':
                    print('Multiplying speed...')
                    self.speed *= 2
                    return f'Updated speed: {self.speed}'
                case 'energy':
                    print('Multiplying energy...')
                    self.energy *= 2
                    return f'Updated energy: {self.energy}'
                case _:
                    print('Invalid input. Please input a valid stats.')

if __name__ == '__main__':
    beginnerStats: int = PlayerStats(10, 5, 4, 3, 20)
    print(beginnerStats)

    currentStats: str = beginnerStats.statsMultiplier(value=' ')
    print(beginnerStats)