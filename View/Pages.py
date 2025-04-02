import pygame
from pygame.locals import *
from qirefining import CultivationQiRefining


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
    
    player = CultivationQiRefining()
    background = pygame.Surface((1280, 720))
    background.fill((0, 100, 0))
    
    #Font
    title_font = pygame.font.Font(None, 72)
    info_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 32)
    message_font = pygame.font.Font(None, 28)
    

    title_text = title_font.render("Cultivation Page", True, (255, 255, 255))
    title_pos = title_text.get_rect(center=(640, 50))
    
    BackButton = pygame.image.load('BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    CultivateButton = pygame.Rect(540, 400, 200, 50)
    BreakthroughButton = pygame.Rect(540, 470, 200, 50)
    
    #Beskeder
    messages = []
    message_cooldown = 0
    
    while True:
        if message_cooldown > 0:
            message_cooldown -= 1
        else:
            messages = []
        
        #Current status
        stage_text = info_font.render(f"Stage: Qi Refining {player.stage}/5", True, (255, 255, 255))
        exp_text = info_font.render(f"Exp: {int(player.currentCultivationexp)}/{player.requiredExp.get(player.stage, 0)}", True, (255, 255, 255))
        
        screen.blit(background, (0, 0))
        screen.blit(title_text, title_pos)
        screen.blit(stage_text, (50, 150))
        screen.blit(exp_text, (50, 200))
        screen.blit(BackButton, BackButtonPos)
        
        #Knapper
        pygame.draw.rect(screen, (70, 70, 70), CultivateButton)
        pygame.draw.rect(screen, (70, 70, 70), BreakthroughButton)
        
        cultivate_text = button_font.render("Cultivate (1 Year)", True, (255, 255, 255))
        breakthrough_text = button_font.render("Attempt Breakthrough", True, (255, 255, 255))
        
        screen.blit(cultivate_text, (CultivateButton.x + 10, CultivateButton.y + 15))
        screen.blit(breakthrough_text, (BreakthroughButton.x + 10, BreakthroughButton.y + 15))
        
        for i, message in enumerate(messages):
            msg_text = message_font.render(message, True, (255, 255, 0))
            screen.blit(msg_text, (50, 250 + i * 30))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButtonPos.collidepoint(event.pos):
                    return "game"
                if CultivateButton.collidepoint(event.pos):
                    player.cultivate(1)
                    messages = ["You cultivated for 1 year and gained experience!"]
                    message_cooldown = 120  # 2 seconds at 60 FPS
                if BreakthroughButton.collidepoint(event.pos):
                    if player.cultivationexp >= player.requiredExp[player.stage]:
                        old_stage = player.stage
                        player.breakthroughRealmStage()
                        if player.stage > old_stage:
                            messages = ["Breakthrough successful! You reached a new stage!"]
                        else:
                            messages = ["Breakthrough failed! You lost all your cultivation experience."]
                        message_cooldown = 120
                    else:
                        messages = ["Not enough experience for a breakthrough!"]
                        message_cooldown = 120
        
        pygame.time.Clock().tick(60)