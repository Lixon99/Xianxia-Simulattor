import pygame
from pygame.locals import *

def main_page(screen):
    backgroundPicture = pygame.image.load('Forside.jpg')
    StartButton = pygame.image.load('StartButton.png')

    StartButtonPos = StartButton.get_rect(center=(640, 500))
    
    while True:
        screen.blit(backgroundPicture, (0, 0))
        screen.blit(StartButton, StartButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButtonPos.collidepoint(event.pos):
                    return "game"
    
def game_page(screen):
    gameBackground = pygame.image.load('GamePage.png')
    FightButton = pygame.image.load('FightButton.png')
    CultivationIMG = pygame.image.load('meditateImg.png')
    CultivateButton = pygame.image.load('CultivateButton.png')

    CultivationIMGPos = CultivationIMG.get_rect(center=(240, 340))
    CultivateButtonPos = CultivateButton.get_rect(center=(244, 650))
    FightButtonPos = FightButton.get_rect(center=(640, 180))
    
    font = pygame.font.Font(None, 48)
    text = font.render("Game Page", True, (255, 255, 255))
    textpos = text.get_rect(center=(640, 40))

    while True:
        screen.blit(gameBackground, (0, 0))
        screen.blit(text, textpos)
        screen.blit(FightButton, FightButtonPos)
        screen.blit(CultivationIMG, CultivationIMGPos)
        screen.blit(CultivateButton, CultivateButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
def fight_page(screen):
    pass
    # Skal lave fight page et andet tidspunkt
def cultivate_page(screen):
    pass
    # Skal lave cultivate page på et andet tidspunkt