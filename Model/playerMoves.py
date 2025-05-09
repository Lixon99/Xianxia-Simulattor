import pyinputplus as pyip
from errorHandling import errorHandling

# Denne fil håndterer spillerens træk
class PlayerMoves:
    def __init__(self, playerAllMoves):
        self.playerAllMoves: dict = playerAllMoves
    
    @errorHandling
    def playerChooseMove(self):
        print('Choose a move:')
        for move in self.playerAllMoves: # Printer alle træk
            print(move.capitalize())
        playerMove = pyip.inputStr('Enter move: ')
        x = playerMove.lower()
        if x not in self.playerAllMoves:
            print('Invalid move. Please enter a valid move.')
            return self.playerChooseMove()
        return x
    
    def __str__(self):
        return f'Player moves: {self.playerAllMoves}'

# Dette er alle spillerens træk
playerAllMoves = {
    "punch": {"name": "punch", "damage": 3, "energyCost": 1}, 
    "block": {"name": "block", "defenseBonus": 2, "energyCost": 1}, 
    "energyblast": {"name": "energyblast", "damage": 8, "energyCost": 3}, 
    "heal": {"name": "heal", "healAmount": 5, "energyCost": 2}
}

if __name__ == '__main__':
    player = PlayerMoves(playerAllMoves)
    print(player)
    playerMove = player.playerChooseMove()
    print(f'Player choose to use {playerMove} \n')