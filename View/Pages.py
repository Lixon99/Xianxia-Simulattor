import pygame
from pygame.locals import *

def main_page(screen):
    backgroundPicture = pygame.image.load('Forside.jpg')
    StartButton = pygame.image.load('StartButton.png')
    QuitButton = pygame.image.load('Quit.png')

    StartButtonPos = StartButton.get_rect(center=(640, 500))
    QuitButtonPos = QuitButton.get_rect(center=(640, 600))
    
    while True:
        screen.blit(backgroundPicture, (0, 0))
        screen.blit(StartButton, StartButtonPos)
        screen.blit(QuitButton, QuitButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButtonPos.collidepoint(event.pos):
                    return "game"
                if QuitButtonPos.collidepoint(event.pos):
                    pygame.quit()
                    return None
    
def game_page(screen):
    gameBackground = pygame.image.load('GamePage.png')
    FightButton = pygame.image.load('FightButton.png')
    CultivationIMG = pygame.image.load('meditateImg.png')
    CultivateButton = pygame.image.load('CultivateButton.png')
    BackButton = pygame.image.load('BackButton.png')

    CultivationIMGPos = CultivationIMG.get_rect(center=(240, 340))
    CultivateButtonPos = CultivateButton.get_rect(center=(244, 650))
    FightButtonPos = FightButton.get_rect(center=(640, 180))
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    font = pygame.font.Font(None, 48)
    text = font.render("Game Page", True, (255, 255, 255))
    textpos = text.get_rect(center=(640, 40))

    while True:
        screen.blit(gameBackground, (0, 0))
        screen.blit(text, textpos)
        screen.blit(FightButton, FightButtonPos)
        screen.blit(CultivationIMG, CultivationIMGPos)
        screen.blit(CultivateButton, CultivateButtonPos)
        screen.blit(BackButton, BackButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FightButtonPos.collidepoint(event.pos):
                    return "fight"
                if BackButtonPos.collidepoint(event.pos):
                    return "main"
                if CultivateButtonPos.collidepoint(event.pos):
                    return "cultivate"

def fight_page(screen):
    FightBackground = pygame.image.load('FightPage.png')
    BackButton = pygame.image.load('BackButton.png')
    
    BackButtonPos = BackButton.get_rect(center=(1220, 35))

    while True:
        screen.blit(FightBackground, (0, 0))
        screen.blit(BackButton, BackButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButtonPos.collidepoint(event.pos):
                    return "game"

def cultivate_page(screen):
    background = pygame.Surface((1280, 720))
    background.fill((0, 100, 0))  # Green background for cultivation
    font = pygame.font.Font(None, 72)
    text = font.render("Cultivation Page", True, (255, 255, 255))
    textpos = text.get_rect(center=(640, 360))
    
    BackButton = pygame.image.load('BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))

    while True:
        screen.blit(background, (0, 0))
        screen.blit(text, textpos)
        screen.blit(BackButton, BackButtonPos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButtonPos.collidepoint(event.pos):
                    return "game"
                
