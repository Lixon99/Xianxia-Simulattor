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
    CultivateButton = pygame.image.load('CultivateButton.png')
    FightButton = pygame.image.load('FightButton.png')

    CultivateButtonPos = CultivateButton.get_rect(center=(244, 592))
    FightButtonPos = FightButton.get_rect(center=(640, 180))
    
    font = pygame.font.Font(None, 48)
    text = font.render("game page", True, (255, 255, 255))
    textpos = text.get_rect(center=(640, 360))

    while True:
        screen.blit(gameBackground, (0, 0))
        screen.blit(text, textpos)
        screen.blit(CultivateButton, CultivateButtonPos)
        screen.blit(FightButton, FightButtonPos)
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