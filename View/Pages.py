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
    
    # Font
    title_font = pygame.font.Font(None, 72)
    info_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 32)
    message_font = pygame.font.Font(None, 28)
    input_font = pygame.font.Font(None, 32)
    
    title_text = title_font.render("Cultivation Page", True, (255, 255, 255))
    title_pos = title_text.get_rect(center=(640, 50))
    
    BackButton = pygame.image.load('BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    # Buttons
    CultivateButton = pygame.Rect(540, 400, 200, 50)
    BreakthroughButton = pygame.Rect(540, 470, 200, 50)
    
    # Input box
    input_box = pygame.Rect(540, 330, 200, 32)
    input_color_inactive = pygame.Color('lightskyblue3')
    input_color_active = pygame.Color('dodgerblue2')
    input_color = input_color_inactive
    input_active = False
    input_text = '1'
    
    # Age tracking
    age = 16  # Starting age
    
    # Messages
    messages = []
    message_cooldown = 0
    
    while True:
        if message_cooldown > 0:
            message_cooldown -= 1
        else:
            messages = []
        
        # Current status - FIXED: Now shows current stage's requirement
        stage_text = info_font.render(f"Stage: Qi Refining {player.stage}/5", True, (255, 255, 255))
        exp_text = info_font.render(
            f"Exp: {int(player.currentCultivationexp)}/{player.requiredExp.get(player.stage, 0)}", 
            True, 
            (255, 255, 255)
        )
        age_text = info_font.render(f"Age: {age} years", True, (255, 255, 255))
        
        screen.blit(background, (0, 0))
        screen.blit(title_text, title_pos)
        screen.blit(stage_text, (50, 150))
        screen.blit(exp_text, (50, 200))
        screen.blit(age_text, (50, 250))
        screen.blit(BackButton, BackButtonPos)
        
        # Draw input box
        pygame.draw.rect(screen, input_color, input_box, 2)
        input_surface = input_font.render(input_text, True, (255, 255, 255))
        screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
        
        # Label for input box
        input_label = info_font.render("Years to cultivate:", True, (255, 255, 255))
        screen.blit(input_label, (input_box.x, input_box.y - 30))
        
        # Buttons
        pygame.draw.rect(screen, (70, 70, 70), CultivateButton)
        pygame.draw.rect(screen, (70, 70, 70), BreakthroughButton)
        
        cultivate_text = button_font.render("Cultivate", True, (255, 255, 255))
        breakthrough_text = button_font.render("Attempt Breakthrough", True, (255, 255, 255))
        
        screen.blit(cultivate_text, (CultivateButton.x + 50, CultivateButton.y + 15))
        screen.blit(breakthrough_text, (BreakthroughButton.x + 10, BreakthroughButton.y + 15))
        
        # Messages
        for i, message in enumerate(messages):
            msg_text = message_font.render(message, True, (255, 255, 0))
            screen.blit(msg_text, (50, 300 + i * 30))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle input box active state
                if input_box.collidepoint(event.pos):
                    input_active = True
                    input_color = input_color_active
                else:
                    input_active = False
                    input_color = input_color_inactive
                    
                if BackButtonPos.collidepoint(event.pos):
                    return "game"
                    
                if CultivateButton.collidepoint(event.pos):
                    try:
                        years = int(input_text)
                        if years > 0:
                            player.cultivate(years)
                            age += years
                            messages = [f"You cultivated for {years} years and gained experience!", f"Your age is now {age}"]
                            message_cooldown = 180
                        else:
                            messages = ["Please enter a positive number of years"]
                            message_cooldown = 120
                    except ValueError:
                        messages = ["Please enter a valid number"]
                        message_cooldown = 120
                        
                if BreakthroughButton.collidepoint(event.pos):
                    if player.cultivationexp >= player.requiredExp[player.stage]:
                        old_stage = player.stage
                        old_exp = player.cultivationexp
                        player.breakthroughRealmStage()
                        
                        # FIXED: Immediately update display after breakthrough
                        if player.stage > old_stage:
                            messages = ["Breakthrough successful! You reached a new stage!"]
                        else:
                            messages = [f"Breakthrough failed! Lost {old_exp} experience."]
                        message_cooldown = 120
                    else:
                        messages = [f"Not enough experience for breakthrough! Need {player.requiredExp[player.stage]}."]
                        message_cooldown = 120
                        
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    input_color = input_color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode
        
        pygame.time.Clock().tick(60)