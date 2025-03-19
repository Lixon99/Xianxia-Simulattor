import pygame
from pygame.locals import *

def main_page(screen):
    backgroundPicture = pygame.image.load('Forside.png')
    StartButton = pygame.image.load('StartButton.png')
    
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to our Unnamed Cultivation game ", 1, (10, 10, 10))
    textpos = text.get_rect(center=(640, 200))

    StartButtonPos = StartButton.get_rect(center=(640, 400))
    
    while True:
        screen.blit(backgroundPicture, (0, 0))
        screen.blit(text, textpos)
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
    font = pygame.font.Font(None, 48)
    text = font.render("game page testning", True, (255, 255, 255))
    textpos = text.get_rect(center=(640, 360))
    
    while True:
        screen.fill((255, 255, 255))
        screen.blut(text, textpos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None


    