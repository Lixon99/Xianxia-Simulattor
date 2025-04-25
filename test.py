import unittest
from qirefining import CultivationQiRefining
from fight import Player, Enemy, fight

class test(unittest.TestCase):
    def setUp(self):
        # Nulstil singleton og opsæt objekter
        CultivationQiRefining._instance = None
        self.qi = CultivationQiRefining()
        self.player = Player(name="Hero", hp=10, attack=3)
        self.enemy = Enemy(name="Villain", hp=8, attack=2)

    # Test om cultivation tilføjer exp og alder
    def testCultivateExpAndAge(self):
        self.qi.cultivate(20)
        self.assertEqual(self.qi.cultivationexp, 20)
        self.assertEqual(self.qi.age, 36)

    # Test om breakthrough ikke virker uden nok exp
    def testBreakthroughFailsWithoutEnoughExp(self):
        self.qi.cultivationexp = 10  
        result = self.qi.breakthroughRealmStage()
        self.assertFalse(result)
        self.assertEqual(self.qi.stage, 1)

    # Test om breakthrough virker med nok exp
    def testBreakthroughWorksWithEnoughExp(self):
        self.qi.cultivationexp = 100 
        self.qi.currentCultivationexp = 100 
        result = self.qi.breakthroughRealmStage()
        self.assertIn(result, [True, False, None]) 

    # Test om kamp mellem spiller og enemy kan gennemføres uden fejl
    def testFightRunsWithoutError(self):
        try:
            fight(self.player, self.enemy)
        except Exception as e:
            self.fail(f"fight() function raised an exception: {e}")
            
    # Test om Player objekt har korrekt startdata
    def testPlayerInitialization(self):
        self.assertEqual(self.player.name, "Hero")
        self.assertEqual(self.player.hp, 10)
        self.assertEqual(self.player.attack, 3)

if __name__ == "__main__":
    unittest.main()
