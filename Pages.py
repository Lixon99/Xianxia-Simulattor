import pygame
import random
from pygame.locals import *
from qirefining import CultivationQiRefining
from fight import Player, Enemy
from enemy import EnemyAI
from playermoves import playerAllMoves


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
    
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 48)

    # starting stat
    player = Player("Player", 30, 5)
    enemy = Enemy("Enemy", 20, 3)
    
    message = ""
    player_stunned = False
    enemy_stunned = False
    energy_blast_uses = 0
    max_energy_blast_uses = 2
    game_over = False

    # playermove buttons
    move_buttons = [
        {"rect": pygame.Rect(50, 400, 200, 50), "name": "punch", "label": "Punch"},
        {"rect": pygame.Rect(50, 460, 200, 50), "name": "block", "label": "Block"},
        {"rect": pygame.Rect(50, 520, 200, 50), "name": "energyblast", "label": f"Energy Blast ({max_energy_blast_uses-energy_blast_uses} left)"},
        {"rect": pygame.Rect(50, 580, 200, 50), "name": "heal", "label": "Heal"}
    ]

    clock = pygame.time.Clock()

    while True:
        screen.blit(FightBackground, (0, 0))
        screen.blit(BackButton, BackButtonPos)

        # hp
        player_hp_text = title_font.render(f"{player.name} HP: {player.hp}", True, (255, 255, 255))
        enemy_hp_text = title_font.render(f"{enemy.name} HP: {enemy.stats['Health']}", True, (255, 255, 255))
        screen.blit(player_hp_text, (50, 50))
        screen.blit(enemy_hp_text, (900, 50))

        #viser fight narration
        if message:
            msg_text = font.render(message, True, (255, 255, 0))
            screen.blit(msg_text, (50, 300))

        #playermove buttons
        for button in move_buttons:
            color = (100, 100, 100) if (button["name"] == "energyblast" and energy_blast_uses >= max_energy_blast_uses) else (70, 70, 70)
            pygame.draw.rect(screen, color, button["rect"])
            label = button["label"].replace(f"({max_energy_blast_uses-energy_blast_uses} left)", f"({max_energy_blast_uses-energy_blast_uses} left)") if "Energy Blast" in button["label"] else button["label"]
            move_text = font.render(label, True, (255, 255, 255))
            screen.blit(move_text, (button["rect"].x + 10, button["rect"].y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButtonPos.collidepoint(event.pos):
                    return "game"
                
                if game_over:
                    continue
                
                if player_stunned:
                    message = "You are stunned and can't move this turn!"
                    player_stunned = False
                    continue
                
                for button in move_buttons:
                    if button["rect"].collidepoint(event.pos):
                        # Deaktiver Energy Blast hvis brugt op
                        if button["name"] == "energyblast" and energy_blast_uses >= max_energy_blast_uses:
                            message = "You can't use Energy Blast anymore this fight!"
                            continue
                        
                        # players tur
                        if button["name"] == "punch":
                            enemy_move = enemy.chooseMove()
                            if enemy_move and enemy_move.get("name") == "dodge":
                                message = "Enemy dodged your punch!"
                            else:
                                if enemy_move and enemy_move.get("name") == "block":
                                    player_stunned = True
                                    message = "Enemy blocked your punch and stunned you!"
                                else:
                                    damage = 3
                                    enemy.stats['Health'] = max(enemy.stats['Health'] - damage, 0)
                                    message = f"You punched for {damage} damage!"
                        
                        elif button["name"] == "energyblast":
                            energy_blast_uses += 1
                            enemy_move = enemy.chooseMove()
                            damage = 8
                            if enemy_move and enemy_move.get("name") == "dodge":
                                message = "Enemy dodged your energy blast!"
                            else:
                                if enemy_move and enemy_move.get("name") == "block":
                                    damage = int(damage * 1.5)
                                    message = f"Enemy blocked but took 1.5x damage! Dealt {damage} damage!"
                                else:
                                    message = f"You used Energy Blast for {damage} damage!"
                                enemy.stats['Health'] = max(enemy.stats['Health'] - damage, 0)
                        
                        elif button["name"] == "block":
                            message = "You prepared to block!"
                        
                        elif button["name"] == "heal":
                            heal_amount = 5
                            player.hp += heal_amount
                            message = f"You healed for {heal_amount} HP!"
                        
                        # Enemys tur (hvis ikke stunned og stadig i live)
                        if not enemy_stunned and enemy.stats['Health'] > 0:
                            enemy_move = enemy.chooseMove()
                            
                            if enemy_move is None:
                                message += " Enemy is stunned!"
                                enemy_stunned = False
                            elif enemy_move.get("name") == "dodge":
                                message += " Enemy dodged!"
                            else:
                                if enemy_move["name"] == "punch":
                                    damage = enemy_move["damage"]
                                    if button["name"] == "block":
                                        enemy_stunned = True
                                        message += " You blocked enemy's punch and stunned them!"
                                    else:
                                        player.hp = max(player.hp - damage, 0)
                                        message += f" Enemy punched for {damage} damage!"
                                
                                elif enemy_move["name"] == "slash":
                                    damage = enemy_move["damage"]
                                    if button["name"] == "block":
                                        damage = int(damage * 1.5)
                                        message += f" Enemy slashed through your block for {damage} damage!"
                                    else:
                                        message += f" Enemy slashed for {damage} damage!"
                                    player.hp = max(player.hp - damage, 0)
                                
                                elif enemy_move["name"] == "block":
                                    message += " Enemy is blocking!"
                        
                        # tjek om fight er slut
                        if enemy.stats['Health'] <= 0:
                            message = "You defeated the enemy!"
                            game_over = True
                        elif player.hp <= 0:
                            message = "You were defeated!"
                            game_over = True
                        
                        # opdaterer hvor mange energy blast du har tilbage
                        for btn in move_buttons:
                            if btn["name"] == "energyblast":
                                btn["label"] = f"Energy Blast ({max_energy_blast_uses-energy_blast_uses} left)"
        
        clock.tick(60)


def defeat_page(screen):
    background = pygame.Surface((1280, 720))
    background.fill((50, 0, 0))  # Mørkerød baggrund
    
    title_font = pygame.font.Font(None, 72)
    message_font = pygame.font.Font(None, 48)
    
    title_text = title_font.render("DEFEAT", True, (255, 255, 255))
    message_text = message_font.render("You succumbed to the ravages of time", True, (255, 255, 255))
    
    QuitButton = pygame.image.load('Quit.png')
    QuitButtonPos = QuitButton.get_rect(center=(640, 400))
    
    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text, (640 - title_text.get_width()//2, 150))
        screen.blit(message_text, (640 - message_text.get_width()//2, 250))
        screen.blit(QuitButton, QuitButtonPos)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QuitButtonPos.collidepoint(event.pos):
                    return "quit"  # Eller None hvis du vil lukke spillet


def cultivate_page(screen):
    player = CultivationQiRefining()
    background = pygame.Surface((1280, 720))
    background.fill((0, 100, 0))
    
    # Fonts
    title_font = pygame.font.Font(None, 72)
    info_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 32)
    message_font = pygame.font.Font(None, 28)
    
    # UI Elementer
    title_text = title_font.render("Cultivation Page", True, (255, 255, 255))
    BackButton = pygame.image.load('BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    # Input boks
    input_box = pygame.Rect(540, 330, 200, 32)
    input_color = pygame.Color('lightskyblue3')
    input_text = '1'
    input_active = False
    
    # Beskeder
    message = ""
    message_cooldown = 0
    
    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text, (640 - title_text.get_width()//2, 50))
        screen.blit(BackButton, BackButtonPos)
        
        # Vis status
        stage_text = info_font.render(f"Stage: Qi Refining {player.stage}/5", True, (255, 255, 255))
        exp_text = info_font.render(f"Exp: {int(player.currentCultivationexp)}/{player.requiredExp.get(player.stage, 0)}", True, (255, 255, 255))
        age_text = info_font.render(f"Age: {player.age} years (Max: {player.max_age[player.stage] if player.stage < 5 else 'Immortal'})", True, (255, 255, 255))
        
        screen.blit(stage_text, (50, 150))
        screen.blit(exp_text, (50, 200))
        screen.blit(age_text, (50, 250))
        
        # Vis besked
        if message and message_cooldown > 0:
            msg_lines = message.split('\n')
            for i, line in enumerate(msg_lines):
                msg_surface = message_font.render(line, True, (255, 255, 0))
                screen.blit(msg_surface, (50, 350 + i * 30))
            message_cooldown -= 1
        
        # Input boks
        pygame.draw.rect(screen, input_color, input_box, 2)
        txt_surface = button_font.render(input_text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        # Knapper
        cultivate_button = pygame.Rect(540, 400, 200, 50)
        breakthrough_button = pygame.Rect(540, 470, 200, 50)
        pygame.draw.rect(screen, (70, 70, 70), cultivate_button)
        pygame.draw.rect(screen, (70, 70, 70), breakthrough_button)
        
        cultivate_text = button_font.render("Cultivate", True, (255, 255, 255))
        breakthrough_text = button_font.render("Breakthrough", True, (255, 255, 255))
        screen.blit(cultivate_text, (cultivate_button.x + 50, cultivate_button.y + 15))
        screen.blit(breakthrough_text, (breakthrough_button.x + 20, breakthrough_button.y + 15))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButtonPos.collidepoint(event.pos):
                    return "game"
                    
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                    
                if cultivate_button.collidepoint(event.pos):
                    try:
                        years = int(input_text)
                        if years > 0:
                            result = player.cultivate(years)
                            if result == "died":
                                return "defeat"
                            message = f"Cultivated for {years} years.\nGained {years} experience."
                            message_cooldown = 120
                    except ValueError:
                        message = "Please enter a valid number"
                        message_cooldown = 60
                        
                if breakthrough_button.collidepoint(event.pos):
                    result = player.breakthroughRealmStage()
                    if result is True:
                        message = f"Breakthrough successful!\nReached stage {player.stage}!"
                        message_cooldown = 120
                    elif result is False:
                        if "failed_lost" in player.last_breakthrough_result:
                            lost_exp = player.last_breakthrough_result.split('_')[-2]
                            message = f"Breakthrough failed!\nLost {lost_exp} experience."
                        else:
                            message = "Breakthrough failed!"
                        message_cooldown = 120
                    else:
                        message = f"Not enough experience for breakthrough!\nNeed {player.requiredExp[player.stage]}."
                        message_cooldown = 60
            
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isdigit():
                    input_text += event.unicode