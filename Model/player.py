import pyinputplus as pyip

class playerStats:
    def __init__(self, health, strength, defense, speed, energy, currentLife, maxLife):
        self.health = int(health)
        self.strength = int(strength)
        self.defense = int(defense)
        self.speed = int(speed)
        self.energy = int(energy)
        self.currentLife = int(currentLife)
        self.maxLife = int(maxLife)
    
    def __str__(self):
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
    
    def statsMultiplier(self):
        response = pyip.inputStr('Choose which stats to multiply')
        if response == 'health':
            self.health *= 5


beginnerStats = playerStats(10, 5, 4, 3, 20, 18, 81)
print(beginnerStats)

playerStats.statsMultiplier(beginnerStats)
currentStats = beginnerStats
print(currentStats)