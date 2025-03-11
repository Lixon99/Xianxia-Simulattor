from playerStats import PlayerStats

def main():
    beginningStats: int = PlayerStats(10, 5, 4, 3, 20, 18, 81)
    print(beginningStats)

    currentStats: str = beginningStats.statsMultiplier(value=' ')
    print(beginningStats)

if __name__ == '__main__':
    main()