import pyinputplus as pyip
import random
from errorHandling import errorHandling

# Denne fil håndterer cultivation og breakthrough for Qi Refining
import random

import random

import random

class CultivationQiRefining:
    _instance = None  # Singleton pattern
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.cultivationexp = 0
            self.currentCultivationexp = 0
            self.stage = 1
            self.age = 16  # Startalder
            self.requiredExp = {1: 50, 2: 300, 3: 1000, 4: 2200, 5: 5000}
            self.max_age = {1: 100, 2: 250, 3: 1000, 4: 2000, 5: float('inf')}
            self._initialized = True
            self.last_breakthrough_result = None
    
    def cultivate(self, years):
        self.cultivationexp += years
        self.age += years
        self.checkMultiplier()
        
        if self.age > self.max_age[self.stage]:
            return "died"
        return "success"
    
    def checkMultiplier(self):
        multipliers = {1: 1.0, 2: 1.2, 3: 1.3, 4: 1.5, 5: 1.6}
        self.currentCultivationexp = self.cultivationexp * multipliers.get(self.stage, 1.0)
    
    def breakthroughRealmStage(self):
        if self.currentCultivationexp >= self.requiredExp[self.stage]:
            if random.random() < 0.7:  # 70% success chance
                self.stage = min(self.stage + 1, 5)
                self.cultivationexp = 0
                self.last_breakthrough_result = "success"
                return True
            else:
                # Mist 25% af XP for nuværende stage
                lost_exp = int(self.requiredExp[self.stage] * 0.25)
                self.cultivationexp = max(0, self.cultivationexp - lost_exp)
                self.checkMultiplier()
                self.last_breakthrough_result = f"failed_lost_{lost_exp}_exp"
                return False
        self.last_breakthrough_result = "not_enough_exp"
        return None