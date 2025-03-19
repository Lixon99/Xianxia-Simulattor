import playerStats, playerMoves
import enemy

# Defienre spilleren og eenemy stats
player = playerStats.PlayerStats(10, 5, 4, 3, 20)
print(player)

enemy = enemy.EnemyAI('Qi Cultivator',
                      stats={'Health': 10, 'Strength': 10, 'Defense': 10, 'Speed': 10, 'Energy': 10}, 
                      strategies=enemy.strategies, allMoves=enemy.allMoves )
print(enemy)

# Kamp function
def fight(player, enemy):
    playerMove = playerMoves.PlayerMoves(playerMoves.playerAllMoves)

    while player.health > 0 and enemy.stats['Health'] > 0:
        # Spilleren vælger et træk
        playerAction = playerMove.playerChooseMove()
        match playerAction:
            case 'punch':
                enemy.stats['Health'] -= player.strength
            case 'block':
                player.defense += 2
            case 'dodge':
                pass
            case 'energyblast':
                enemy.stats['Health'] -= player.energy
            case 'heal':
                player.health += 5
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
                player.health -= enemy.stats['Strength']
            case 'block':
                enemy.stats['Defense'] += 2
            case 'dodge':
                pass
            case 'energyblast':
                player.health -= enemy.stats['Energy']
            case 'heal':
                enemy.stats['Health'] += 5
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

