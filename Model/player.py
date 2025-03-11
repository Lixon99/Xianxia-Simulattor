import pyinputplus as pyip

class PlayerStats:
    def __init__(self, health, strength, defense, speed, energy, currentLife, maxLife) -> int:
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.energy = energy
        self.currentLife = currentLife
        self.maxLife = maxLife
    
    def __str__(self) -> str:
        return f'''¨
        Player Stats
        Health: {self.health}
        Strength: {self.strength}
        Defense: {self.defense}
        Speed: {self.speed}
        Energy: {self.energy}
        Current Life: {self.currentLife}
        Max Life: {self.maxLife}
        '''
    
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
                case 'currentlife':
                    print('Multiplying current life...')
                    self.currentLife *= 2
                    return f'Updated current life: {self.currentLife}'
                case 'maxlife':
                    print('Multiplying max life...')
                    self.maxLife *= 2
                    return f'Updated max life: {self.maxLife}'
                case _:
                    print('Invalid input. Please input a valid stats.')

beginnerStats: int = PlayerStats(10, 5, 4, 3, 20, 18, 81)
print(beginnerStats)

currentStats: str = beginnerStats.statsMultiplier(value='')

print(beginnerStats)