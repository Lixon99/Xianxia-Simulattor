import pyinputplus as pyip
import random

class CultivationNascentSoul:
    def __init__(self):
        # Initialisere variablerne
        self.cultivationexp: int = 0
        self.currentCultivationexp: int = 0
        self.stage: int = 1

    def cultivate(self, n: int):
        for _ in range(n):
            self.cultivationexp += 1 # cultivationexp værdi er 0, så 1 eksister, så tallet kan gå rigtig op hvert iteration
        self.checkMultiplier()
        return self.currentCultivationexp
    
    def checkMultiplier(self):
        match self.stage:
            case 1:
                self.currentCultivationexp = self.cultivationexp * 16
            case 2:
                self.currentCultivationexp = self.cultivationexp * 16
            case 3:
                self.currentCultivationexp = self.cultivationexp * 16
            case 4:
                self.currentCultivationexp = self.cultivationexp * 16
            case 5:
                self.currentCultivationexp = self.cultivationexp * 16
        return self.currentCultivationexp
                
    def breakthroughRealmStage(self):
        requiredExp = {1: 650000, 2: 825000, 3: 1025000, 4: 1250000, 5: 1500000}   
        if self.cultivationexp >= requiredExp[self.stage]: # Henter værdi fra requiredexp dict
            checkChance = random.randint(0, 1)
            if checkChance == 1:
                print('Breakthrough Sucess!')
                self.stage += 1
                self.cultivationexp = 0
            else:
                print('BreakThrough Failed!')
                self.cultivationexp = 0

if __name__ == '__main__':
    player = CultivationNascentSoul()
    requiredExp = {1: 650000, 2: 825000, 3: 1025000, 4: 1250000, 5: 1500000}   

    while player.stage <= 5:
        while player.cultivationexp < requiredExp[player.stage]:
            cultivation: int = pyip.inputInt('Enter how long you would like to cultivatet for (Years): ')
            print(f'Not enough cultivations exp to try and breakthrough to Stage: {player.stage + 1}')
            player.cultivate(cultivation)
            print(f'Current cultivators exp: {player.currentCultivationexp}')
        
        player.breakthroughRealmStage()
        print(f'Players realm: {player.stage}')