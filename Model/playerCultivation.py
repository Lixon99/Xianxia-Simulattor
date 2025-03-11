from player import PlayerStats
import pyinputplus as pyip

class PlayerCultivation:
    def __init__(self):
        self.cultivationexp = 0
        self.stage = 0
        self.multiplier = {'Stage1': 1, 'Stage2': 2, 'Stage3': 3, 'Stage4': 4, 'Stage5': 5}

    def multipliers(self):
        if self.cultivationexp <= 100:
            self.stage = 1
        elif self.cultivationexp <= 500 > 100:
            self.stage = 2
        elif self.cultivationexp <= 1500 > 500:
            self.stage = 3
        elif self.cultivationexp <= 3000 > 1500:
            self.stage = 4
        elif self.cultivationexp < 5000 > 3000:
            self.stage = 5

    def cultivate(self, n: int):
        for self.cultivationexp in range(n):
            self.cultivationexp += 1
            self.cultivationexp *= self.stage
            self.multipliers()
        return self.cultivationexp
    
    def qiRefiningBreakthrough(self):
        if cultivation >= 100:
            print('Breakthrough')
        else:
            print('No')


    def breakthroughRealm(self):
        pass

if __name__ == '__main__':
    player: PlayerCultivation = PlayerCultivation()

    cultivation: int = player.cultivate(pyip.inputInt('Enter how long you would like to cultivatet for (Year): '))
    print(cultivation)

"""   breakThrough = PlayerCultivaion.qiRefiningBreakthrough(cultivation)
    print(breakThrough) """