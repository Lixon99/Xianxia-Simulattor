import pygame
import View.Pages

class Controller:
    def __init__(self):
        self.current_page = "main"
    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Xianxia')
        self.clock = pygame.time.Clock()

        while True:
            if self.current_page == "main":
                self.current_page = View.Pages.main_page(self.screen)
            elif self.current_page == "game":
                print("Skiftet til game page")
                self.current_page = View.Pages.game_page(self.screen)

            self.clock.tick(60)
            
if __name__ == "__main__":
    app = Controller()
    app.run()
