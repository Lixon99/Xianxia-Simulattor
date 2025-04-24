import pygame
import random
from pygame.locals import *
from qirefining import CultivationQiRefining
from fight import Player, Enemy
from enemy import EnemyAI
from playermoves import playerAllMoves


def main_page(screen):
    backgroundPicture = pygame.image.load('Xianxia-Simulattor-Gab/Forside.jpg')
    StartButton = pygame.image.load('Xianxia-Simulattor-Gab/StartButton.png')
    QuitButton = pygame.image.load('Xianxia-Simulattor-Gab/Quit.png')

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
    
def game_page(screen, cultivation=None):
    if cultivation is None:
        cultivation = CultivationQiRefining()
    
    gameBackground = pygame.image.load('Xianxia-Simulattor-Gab/GamePage.png')
    FightButton = pygame.image.load('Xianxia-Simulattor-Gab/FightButton.png')
    CultivationIMG = pygame.image.load('Xianxia-Simulattor-Gab/meditateImg.png')
    CultivateButton = pygame.image.load('Xianxia-Simulattor-Gab/CultivateButton.png')
    BackButton = pygame.image.load('Xianxia-Simulattor-Gab/BackButton.png')

    CultivationIMGPos = CultivationIMG.get_rect(center=(240, 340))
    CultivateButtonPos = CultivateButton.get_rect(center=(244, 550))
    FightButtonPos = FightButton.get_rect(center=(640, 180))
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 28)
    
    # Stats tekst
    status_lines = [
        f"Stage: Qi Refining {cultivation.stage}/5",
        f"EXP: {int(cultivation.currentCultivationexp)}/{cultivation.requiredExp.get(cultivation.stage, 0)}",
        f"Age: {cultivation.age} years",
        f"Max Age: {cultivation.max_age[cultivation.stage] if cultivation.stage < 5 else 'Immortal'}"
    ]

    while True:
        screen.blit(gameBackground, (0, 0))
        
        # Placering af stats på game page
        for i, line in enumerate(status_lines):
            status_text = small_font.render(line, True, (255, 255, 255))
            screen.blit(status_text, (50, 100 + i * 30))
        
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


def fight_page(screen, cultivation=None):
    if cultivation is None:
        cultivation = CultivationQiRefining()
    
    FightBackground = pygame.image.load('Xianxia-Simulattor-Gab/FightPage.png')
    BackButton = pygame.image.load('Xianxia-Simulattor-Gab/BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)

    # EXP belønningssystem
    stage_exp_rewards = {1: 20, 2: 50, 3: 75, 4: 100, 5: 150}
    current_exp_reward = stage_exp_rewards.get(cultivation.stage, 0)
    exp_reward_text = small_font.render(f"Victory reward: {current_exp_reward} EXP", True, (200, 255, 200))

    # starting stat
    player = Player("Player", 30, 5)
    enemy = Enemy("Enemy", 20, 3)
    
    message = ""
    player_stunned = False
    enemy_stunned = False
    energy_blast_uses = 0
    max_energy_blast_uses = 2
    heal_used = False  # Ny variabel til at tracke heal brug
    game_over = False
    last_enemy_attack = None

    # playermove buttons
    move_buttons = [
        {"rect": pygame.Rect(50, 400, 200, 50), "name": "punch", "label": "Punch"},
        {"rect": pygame.Rect(50, 460, 200, 50), "name": "block", "label": "Block"},
        {"rect": pygame.Rect(50, 520, 200, 50), "name": "energyblast", "label": f"Energy Blast ({max_energy_blast_uses-energy_blast_uses} left)"},
        {"rect": pygame.Rect(50, 580, 200, 50), "name": "heal", "label": "Heal (1 left)" if not heal_used else "Heal (0 left)"}
    ]

    clock = pygame.time.Clock()

    while True:
        screen.blit(FightBackground, (0, 0))
        screen.blit(BackButton, BackButtonPos)
        screen.blit(exp_reward_text, (900, 100))

        # hp
        player_hp_text = title_font.render(f"{player.name} HP: {player.hp}", True, (255, 255, 255))
        enemy_hp_text = title_font.render(f"{enemy.name} HP: {enemy.stats['Health']}", True, (255, 255, 255))
        screen.blit(player_hp_text, (50, 50))
        screen.blit(enemy_hp_text, (900, 50))

        # viser fight narration
        if message:
            msg_text = font.render(message, True, (255, 255, 0))
            screen.blit(msg_text, (50, 300))

        # playermove buttons
        for button in move_buttons:
            color = (100, 100, 100) if (
                (button["name"] == "energyblast" and energy_blast_uses >= max_energy_blast_uses) or
                (button["name"] == "heal" and heal_used)
            ) else (70, 70, 70)
            pygame.draw.rect(screen, color, button["rect"])
            
            # Opdater labels
            if button["name"] == "energyblast":
                label = f"Energy Blast ({max_energy_blast_uses-energy_blast_uses} left)"
            elif button["name"] == "heal":
                label = "Heal (1 left)" if not heal_used else "Heal (0 left)"
            else:
                label = button["label"]
            
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
                        # Deaktiver move hvis brugt op
                        if (button["name"] == "energyblast" and energy_blast_uses >= max_energy_blast_uses) or \
                           (button["name"] == "heal" and heal_used):
                            message = f"You can't use {button['name'].capitalize()} anymore this fight!"
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
                            heal_used = True  # Marker heal som brugt
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
                                    last_enemy_attack = "punch"  # Gem angrebstype
                                    if button["name"] == "block":
                                        enemy_stunned = True
                                        message += " You blocked enemy's punch and stunned them!"
                                    else:
                                        player.hp = max(player.hp - damage, 0)
                                        message += f" Enemy punched for {damage} damage!"
                                
                                elif enemy_move["name"] == "slash":
                                    damage = enemy_move["damage"]
                                    last_enemy_attack = "slash"  # Gem angrebstype
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
                            cultivation.cultivationexp += current_exp_reward
                            cultivation.checkMultiplier()
                            message = f"You defeated the enemy! Gained {current_exp_reward} EXP!"
                            game_over = True
                        elif player.hp <= 0:
                            return ["defeat", last_enemy_attack]
        
        clock.tick(60)


def defeat_page(screen, death_info=None):
    death_cause = death_info[1] if death_info and len(death_info) > 1 else "unknown" #
    
    death_messages = {
        "punch": "You got punched to death by a Rogue",
        "slash": "You got slashed to death by a Rogue",
        "old_age": "You succumbed to the ravages of time",
        "unknown": "You were defeated"
    }
    
    death_message = death_messages.get(death_cause, death_messages["unknown"])
    
    background = pygame.Surface((1280, 720))
    background.fill((50, 0, 0))
    
    title_font = pygame.font.Font(None, 72)
    message_font = pygame.font.Font(None, 48)
    sub_font = pygame.font.Font(None, 36)
    
    title_text = title_font.render("YOU DIED", True, (255, 255, 255))
    message_text = message_font.render(death_message, True, (255, 255, 255))
    sub_text = sub_font.render("Your cultivation journey ends here", True, (200, 200, 200))
    
    QuitButton = pygame.image.load('Xianxia-Simulattor-Gab/Quit.png')
    QuitButtonPos = QuitButton.get_rect(center=(640, 400))
    
    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text, (640 - title_text.get_width()//2, 150))
        screen.blit(message_text, (640 - message_text.get_width()//2, 250))
        screen.blit(sub_text, (640 - sub_text.get_width()//2, 320))
        screen.blit(QuitButton, QuitButtonPos)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QuitButtonPos.collidepoint(event.pos):
                    return "quit"


def cultivate_page(screen, cultivation=None):
    if cultivation is None:
        cultivation = CultivationQiRefining()
    
    FPS = 60
    SHORT_MESSAGE_COOLDOWN = int(FPS * 1)  # 1 sekund
    LONG_MESSAGE_COOLDOWN = int(FPS * 2)   # 2 sekunder
    
    background = pygame.image.load("Xianxia-Simulattor-Gab/CultivatePageIMG.jpg")
    background = pygame.transform.scale(background, (1280, 720))
    breakthrough_chances = {1: 95, 2: 80, 3: 70, 4: 60, 5: 50}
    current_chance = breakthrough_chances.get(cultivation.stage, 50)
    
    title_font = pygame.font.Font(None, 72)
    info_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 32)
    message_font = pygame.font.Font(None, 28)
    small_font = pygame.font.Font(None, 24)
    
    title_text = title_font.render("Cultivation Page", True, (255, 255, 255))
    BackButton = pygame.image.load('Xianxia-Simulattor-Gab/BackButton.png')
    BackButtonPos = BackButton.get_rect(center=(1220, 35))
    
    input_box = pygame.Rect(540, 330, 200, 32)
    input_color = pygame.Color('lightskyblue3')
    input_text = '1'
    input_active = False
    
    message = ""
    message_cooldown = 0
    
    tip_box = pygame.Rect(900, 150, 350, 60)
    tip_text = "Tip: Fighting bandits gives EXP too"
    
    
    breakthrough_chance_box = pygame.Rect(900, 220, 350, 80) # Breakthrough chance boks
    breakthrough_chance = 70  # 70% chance som standard
    
    clock = pygame.time.Clock()

    while True:
        # Beregn progression i procent
        if cultivation.requiredExp[cultivation.stage] > 0:
            progress_percent = min(100, int((cultivation.currentCultivationexp / cultivation.requiredExp[cultivation.stage]) * 100))
        else:
            progress_percent = 100
        
        screen.blit(background, (0, 0))
        overlay = pygame.Surface((1280, 720))
        overlay.set_alpha(50)  # Justér gennemsigtighed (0-255)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        screen.blit(title_text, (640 - title_text.get_width()//2, 50))
        screen.blit(BackButton, BackButtonPos)
        
        # Vis status
        stage_text = info_font.render(f"Stage: Qi Refining {cultivation.stage}/5", True, (255, 255, 255))
        exp_text = info_font.render(f"Exp: {int(cultivation.currentCultivationexp)}/{cultivation.requiredExp.get(cultivation.stage, 0)}", True, (255, 255, 255))
        age_text = info_font.render(f"Age: {cultivation.age} years (Max: {cultivation.max_age[cultivation.stage] if cultivation.stage < 5 else 'Immortal'})", True, (255, 255, 255))
        progress_text = info_font.render(f"Breakthrough ready: {progress_percent}%", True, (255, 255, 255))
        
        screen.blit(stage_text, (50, 150))
        screen.blit(exp_text, (50, 200))
        screen.blit(age_text, (50, 250))
        screen.blit(progress_text, (50, 300))
        
        # Vis besked hvis aktiv
        if message and message_cooldown > 0:
            msg_lines = message.split('\n')
            for i, line in enumerate(msg_lines):
                msg_surface = message_font.render(line, True, (255, 255, 0))
                screen.blit(msg_surface, (50, 350 + i * 30))
        
        # Input boks
        pygame.draw.rect(screen, (30, 30, 30), input_box)  # Fyld
        pygame.draw.rect(screen, input_color, input_box, 2)  # Kant

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
        
        # Tip boks
        pygame.draw.rect(screen, (50, 50, 70), tip_box)
        pygame.draw.rect(screen, (100, 100, 120), tip_box, 2)
        tip_surface = small_font.render(tip_text, True, (200, 200, 255))
        screen.blit(tip_surface, (tip_box.x + 10, tip_box.y + 20))
        
        # Breakthrough chance boks
        pygame.draw.rect(screen, (70, 50, 50), breakthrough_chance_box)
        pygame.draw.rect(screen, (120, 80, 80), breakthrough_chance_box, 2)
        
        # Vis kun chance hvis spilleren har nok EXP
        if cultivation.currentCultivationexp >= cultivation.requiredExp[cultivation.stage]:
            chance_text = small_font.render(f"Breakthrough chance: {current_chance}%", True, (255, 200, 200))
            risk_text = small_font.render(f"Failure penalty: -25% EXP", True, (255, 180, 180))
        else:
            chance_text = small_font.render("Reach 100% EXP to see", True, (200, 200, 200))
            risk_text = small_font.render("breakthrough chance", True, (200, 200, 200))
        
        screen.blit(chance_text, (breakthrough_chance_box.x + 10, breakthrough_chance_box.y + 15))
        screen.blit(risk_text, (breakthrough_chance_box.x + 10, breakthrough_chance_box.y + 40))
        
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
                            result = cultivation.cultivate(years)
                            if result == "died":
                                return ["defeat", "old_age"]  # Tilføj her
                            message = f"Cultivated for {years} years.\nGained {years} experience."
                                
                            message_cooldown = LONG_MESSAGE_COOLDOWN
                    except ValueError:
                        message = "Please enter a valid number"
                        message_cooldown = SHORT_MESSAGE_COOLDOWN
                        
                if breakthrough_button.collidepoint(event.pos):
                    result = cultivation.breakthroughRealmStage()
                    if result is True:
                        message = f"Breakthrough successful!\nReached stage {cultivation.stage}!"
                        message_cooldown = LONG_MESSAGE_COOLDOWN
                    elif result is False:
                        if "failed_lost" in cultivation.last_breakthrough_result:
                            lost_exp = cultivation.last_breakthrough_result.split('_')[-2]
                            message = f"Breakthrough failed!\nLost {lost_exp} experience."
                        else:
                            message = "Breakthrough failed!"
                        message_cooldown = LONG_MESSAGE_COOLDOWN
                    else:
                        message = f"Not enough experience for breakthrough!\nNeed {cultivation.requiredExp[cultivation.stage]}."
                        message_cooldown = SHORT_MESSAGE_COOLDOWN
            
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isdigit():
                    input_text += event.unicode
        
        # Opdater message cooldown
        if message_cooldown > 0:
            message_cooldown -= 1
        
        # Hold konstant FPS
        clock.tick(FPS)
