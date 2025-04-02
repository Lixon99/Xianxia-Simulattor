import pyinputplus as pyip
import random
from Model.errorHandling import errorHandling

# Denne fil håndterer cultivation og breakthrough for Qi Refining
class CultivationQiRefining:
    def __init__(self):
        # Initialisere variablerne
        self.cultivationexp: int = 0
        self.currentCultivationexp: int = 0
        self.stage: int = 1
        self.requiredExp = {1: 100, 2: 500, 3: 1500, 4: 3000, 5: 5000}  
    
    @errorHandling
    def cultivate(self, n: int):
        for _ in range(n):
            self.cultivationexp += 1 # cultivationexp værdi er 0, så 1 eksister, så tallet kan gå rigtig op hvert iteration
        self.checkMultiplier()
        return self.currentCultivationexp
    
    @errorHandling
    def checkMultiplier(self):
        match self.stage:
            case 1:
                self.currentCultivationexp = self.cultivationexp * 1
            case 2:
                self.currentCultivationexp = self.cultivationexp * 1.2
            case 3:
                self.currentCultivationexp = self.cultivationexp * 1.3
            case 4:
                self.currentCultivationexp = self.cultivationexp * 1.5
            case 5:
                self.currentCultivationexp = self.cultivationexp * 1.6
        return self.currentCultivationexp

    @errorHandling       
    def breakthroughRealmStage(self):
        if self.cultivationexp >= self.requiredExp[self.stage]: # Henter værdi fra requiredexp dict
            checkChance = random.randint(0, 1)
            if checkChance == 1:
                print('Breakthrough Sucess!')
                self.stage += 1
                self.cultivationexp = 0
            else:
                print('BreakThrough Failed!')
                self.cultivationexp = 0

if __name__ == '__main__':
    player = CultivationQiRefining() 

    while player.stage <= 5:
        while player.cultivationexp < player.requiredExp[player.stage]:
            cultivation: int = pyip.inputInt('Enter how long you would like to cultivatet for (Years): ')
            print(f'Not enough cultivations exp to try and breakthrough to Stage: {player.stage + 1}')
            player.cultivate(cultivation)
            print(f'Current cultivators exp: {player.currentCultivationexp}')
        
        player.breakthroughRealmStage()
        print(f'Players realm: {player.stage}')

        if player.stage > 5:
            print('You have reached the maximum stage for Qi Refining')
            break