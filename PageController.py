import pygame
import Pages
from qirefining import CultivationQiRefining

class Controller:
    def __init__(self):
        self.current_page = "main"
        self.cultivation = CultivationQiRefining()
        self.death_info = None  # Initialiserer death_info
    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Xianxia')
        self.clock = pygame.time.Clock()

        while True:
            result = None
            if self.current_page == "main":
                result = Pages.main_page(self.screen)
            elif self.current_page == "game":
                result = Pages.game_page(self.screen, self.cultivation)
            elif self.current_page == "fight":
                result = Pages.fight_page(self.screen, self.cultivation)
            elif self.current_page == "cultivate":
                result = Pages.cultivate_page(self.screen, self.cultivation)
            elif self.current_page == "defeat":
                result = Pages.defeat_page(self.screen, self.death_info)
            
            if isinstance(result, list) and result[0] == "defeat":
                self.current_page = "defeat"
                self.death_info = result
            elif result is None:
                break
            else:
                self.current_page = result
                self.death_info = None  # Nulstil death_info når vi skifter side
                
            self.clock.tick(60)
            
if __name__ == "__main__":
    app = Controller()
    app.run()
    