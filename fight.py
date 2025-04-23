import playerstats, playermoves
import playerStats, playerMoves, enemy
from errorHandling import errorHandling

# Defienre spilleren og eenemy stats
player = playerStats.PlayerStats(10, 5, 4, 10)
print(player)

enemy = enemy.EnemyAI('Qi Cultivator',
                      stats={'Health': 10, 'Strength': 5, 'Defense': 4, 'Energy': 10}, 
                      strategies=enemy.strategies, 
                      allMoves=enemy.allMoves 
                      )
print(enemy)

# Kamp function
@errorHandling
def fight(player, enemy):
    playerMove = playerMoves.PlayerMoves(playerMoves.playerAllMoves)

    while player.health > 0 and enemy.stats['Health'] > 0:
        # Spilleren vælger et træk
        playerAction = playerMove.playerChooseMove()
        match playerAction:
            case 'punch':
                print('---------------------- \nPlayer uses punch')
                enemy.stats['Health'] -= player.strength
                player.energy -= 1
            case 'block':
                print('---------------------- \nPlayer uses block')
                player.defense += 2
            case 'energyblast':
                print('---------------------- \nPlayer uses energyblast')
                enemy.stats['Health'] -= player.strength + (0.5 * player.strength)
                player.energy -= 5
            case 'heal':
                print('---------------------- \nPlayer uses heal')
                player.health += 5
                player.energy -= 2
            case _:
                print('Invalid move. Please try again.')
                continue

        if enemy.stats['Health'] <= 0:
            print('You win!')
            break
        
        # AI vælger et træk4
        aiMove = enemy.chooseMove(playerAction)
        match aiMove['name']:
            case 'punch':
                print('---------------------- \nenemy uses punch')
                player.health -= enemy.stats['Strength']
                enemy.stats['Energy'] -= 1
            case 'block':
                print('---------------------- \nenemy uses block')
                enemy.stats['Defense'] += 2
            case 'energyblast':
                print('---------------------- \nenemy uses energyblast')
                enemy.stats['Health'] -= enemy.stats['Strength'] + (0.5 * enemy.stats['Strength'])
                enemy.stats['Energy'] -= 5
            case 'heal':
                print('---------------------- \nenemy uses heal')
                enemy.stats['Health'] += 5
                enemy.stats['Energy'] -= 2
            case _:
                print('Invalid move. Please try again.')
                continue

        if player.health <= 0:
            print('You lose!')
            break
            
        print(f'{player}')
        print(f'{enemy}')

if __name__ == '__main__': 
    fight(player, enemy)