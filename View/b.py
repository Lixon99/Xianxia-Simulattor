import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Unnamed cultivation game')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to Unnamed Cultivation game ", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': 
    main()