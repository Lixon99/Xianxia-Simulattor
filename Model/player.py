import pyinputplus as pyip
from playerStats import PlayerStats
from qiRefining import CultivationQiRefining

def main():
    """   beginningStats: int = PlayerStats(10, 5, 4, 3, 20, 18, 81)
    print(beginningStats)

    currentStats: str = beginningStats.statsMultiplier(value=' ')
    print(beginningStats)
    """

    # Qi Refining
    playerQiRefining = CultivationQiRefining()

    while playerQiRefining.stage <= 5:
        while playerQiRefining.cultivationexp < playerQiRefining.requiredExp[playerQiRefining.stage]:
            cultivation: int = pyip.inputInt('Enter how long you would like to cultivatet for (Years): ')
            playerQiRefining.cultivate(cultivation)
            print(f'Current cultivators exp: {int(playerQiRefining.currentCultivationexp)}')

            if playerQiRefining.cultivationexp < playerQiRefining.requiredExp[playerQiRefining.stage]:
                print(f'Not enough cultivations exp to try and breakthrough to Stage: {playerQiRefining.stage + 1}')
        
        playerQiRefining.breakthroughRealmStage()
        print(f'Players realm: {playerQiRefining.stage}')

    
if __name__ == '__main__':
    main()