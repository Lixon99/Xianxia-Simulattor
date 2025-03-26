import unittest
from playerStats import PlayerStats
from enemy import EnemyAI, allMoves, strategies
from fight import fight
from playerMoves import PlayerMoves, playerAllMoves

class TestXianxiaSimulator(unittest.TestCase):
    # Setup spilleren og enemy objekter
    def setUp(self):
        self.player = PlayerStats(health=10, strength=5, defense=4, energy=10)
        self.enemy = EnemyAI(
            name="Qi Cultivator",
            stats={"Health": 10, "Strength": 5, "Defense": 4, "Energy": 10},
            strategies=strategies,
            allMoves=allMoves,
        )
        self.playerMoves = PlayerMoves(playerAllMoves)
    
    # Test om spilleren og enemy er initialiseret korrekt
    def testPlayerInitialization(self):
        self.assertEqual(self.player.health, 10)
        self.assertEqual(self.player.strength, 5)
        self.assertEqual(self.player.defense, 4)
        self.assertEqual(self.player.energy, 10)
    
    # Test om enemy er initialiseret korrekt
    def testEnemyInitialization(self):
        self.assertEqual(self.enemy.name, "Qi Cultivator")
        self.assertEqual(self.enemy.stats["Health"], 10) 
        self.assertEqual(self.enemy.stats["Strength"], 5)
        self.assertEqual(self.enemy.stats["Defense"], 4)
        self.assertEqual(self.enemy.stats["Energy"], 10)
    
    # Test om spillerens træk er initialiseret korrekt
    def testPlayerMoveSelection(self):
        valid_move = "punch"
        self.assertIn(valid_move, self.playerMoves.playerAllMoves)
    
    # Tester om spilleren og enemy kan vælge et træk
    def testFightSimulation(self):
        # Simulere en punch fra spilleren
        self.enemy.stats["Health"] -= self.player.strength
        self.assertEqual(self.enemy.stats["Health"], 5)

        # Simulate en punch fra  enemy
        self.player.health -= self.enemy.stats["Strength"]
        self.assertEqual(self.player.health, 5)
    
    # Test om fight functionen kører uden fejl
    def testFightFunction(self):
        try:
            fight(self.player, self.enemy)
        except Exception as e:
            self.fail(f"fight function raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()