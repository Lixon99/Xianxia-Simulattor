import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Unnamed cultivation game')

    backgroundPicture = pygame.image.load('Forside.png')
    StartButton = pygame.image.load('StartButton.png')
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

       
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to our Unnamed Cultivation game ", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (720/4)

    StartButtonPos = StartButton.get_rect()
    StartButtonPos.centerx = background.get_rect().centerx
    StartButtonPos.centery = background.get_rect().centery
    

    while True:
        pygame.display.flip()
        clock.tick(60)
        screen.blit(backgroundPicture, (0, 0))
        screen.blit(text, textpos)
        screen.blit(StartButton, StartButtonPos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__': 
    main()