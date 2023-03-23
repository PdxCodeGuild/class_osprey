import pygame
import sys
from random import choice
from charclasses import Player, Enemy, Spritesheet
from buttonclass import Button

#------Initializing
pygame.init()
DISPLAY_WIDTH = 512
DISPLAY_HEIGHT = 480
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('FOREST FIGHT !')
FONT = pygame.font.SysFont('Courier', 20)
fps = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
#------Starting game attributes
turn_counter = []
playerhp = 100
playeratk = 20
stats = [playerhp, playeratk]
#------COLORS
BACKGROUND = (40, 36, 15)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
#------Game loops
start_menu = True
game_run = False
end_screen = False

#---------------------#GAME FUNCTIONS#-------------------------------------------#
#------takes in sprites and doubles size for display
def upres(image):
    load_in = pygame.image.load(image)
    fullsize = pygame.transform.scale(load_in, (load_in.get_width()*2 , load_in.get_height()*2))
    return fullsize

#------all displayed text in the game
def text_gen(text, color, x, y):
    phrase = FONT.render(text, False, color)
    screen.blit(phrase, (x, y))
    
#------background setup
def set_background():
    screen.blit(forest, (0,0))
    screen.blit(menu, (0, 320))

#------combat functions
def enemy_turn():
    monster.status = 'attack'
    monster.frame_index = 6
    monster.update()
    hero.status = 'hurt'
    hero.frame_index = 18
    hero.update()
    damagecalc_e = monster.attack(hero)
    pygame.mixer.Sound.play(enemyattack)
    return damagecalc_e
    
def attack_turn():
    hero.status = 'attack'
    hero.frame_index = 6
    hero.update()
    damagecalc_p = hero.attack(monster)
    monster.status = 'hurt'
    monster.frame_index = 12
    monster.update()
    pygame.mixer.Sound.play(sword)
    return damagecalc_p

def heal_turn():
    pygame.mixer.Sound.play(healsound)
    hero.status = 'heal'
    hero.frame_index = 12
    init_health = hero.health
    hero.heal()
    amount = hero.health-init_health
    hero.update()
    return amount

def magic_turn():
    pygame.mixer.Sound.play(fire)
    hero.status = 'magic'
    hero.frame_index = 22
    hero.update()
    damagecalc_m = hero.magic(monster)
    monster.status = 'hurt'
    monster.frame_index = 12
    monster.update()
    return damagecalc_m

#------end of round win/lose
def game_end():
    if hero.check_alive():
        return 'win'
    if not hero.check_alive():
        return 'lose'

#---------------------#VISUAL ASSETS#--------------------------------------------#
#------Sprite Setup#
start = upres('code\\liam\\python\\minicapstone\\sprites\\start.png')
forest = upres('code\\liam\\python\\minicapstone\\sprites\\forest_bg.png')
menu = upres('code\\liam\\python\\minicapstone\\sprites\\mainmenu.png')
win_card = upres('code\\liam\\python\\minicapstone\\sprites\\winframe.png')
lose_card = upres('code\\liam\\python\\minicapstone\\sprites\\loseframe.png')
#------buttons
st_btn = Button('code\\liam\\python\\minicapstone\\sprites\\startbutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\startbutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\startbutton_p.png', 210, 300)
qt_btn = Button('code\\liam\\python\\minicapstone\\sprites\\quitbutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\quitbutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\quitbutton_p.png', 210, 340)
yes = Button('code\\liam\\python\\minicapstone\\sprites\\yesbutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\yesbutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\yesbutton_p.png', 140, 150)
no = Button('code\\liam\\python\\minicapstone\\sprites\\nobutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\nobutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\nobutton_p.png', 260, 150)
atk_btn = Button('code\\liam\\python\\minicapstone\\sprites\\atkbutton.png',
                 'code\\liam\\python\\minicapstone\\sprites\\atkbutton_h.png',
                 'code\\liam\\python\\minicapstone\\sprites\\atkbutton_p.png', 50, 385)
hl_btn = Button('code\\liam\\python\\minicapstone\\sprites\\healbutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\healbutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\healbutton_p.png', 50, 410)
mg_btn = Button('code\\liam\\python\\minicapstone\\sprites\\magicbutton.png',
                'code\\liam\\python\\minicapstone\\sprites\\magicbutton_h.png',
                'code\\liam\\python\\minicapstone\\sprites\\magicbutton_p.png', 50, 435)
#------heal effect prep
healanim = []
animation_steps = 6
last_update = pygame.time.get_ticks()
frame_duration = 100
healframe = 0
heal = upres('code\\liam\\python\\minicapstone\\sprites\\hero\\magic\\heal.png') 
healsheet = Spritesheet(heal)
for x in range(7):
    healanim.append(healsheet.get_sprite(x, 32, 32, 1))

#-------------------------------#AUDIO#-----------------------------------------#
#------Music
pygame.mixer.init()
pygame.mixer.music.load('code\\liam\\python\\minicapstone\\sound\\song.mid')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
#------SFX
sword = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\sword.mp3')
healsound = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\heal.mp3')
fire = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\fire.mp3')
bite = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\bite.mp3')
ghostyell = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\yell.mp3')
punch = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\punch.mp3')
winsound = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\win.mp3')
losesound = pygame.mixer.Sound('code\\liam\\python\\minicapstone\\sound\\lose.mp3')

#---------------------------#GAME LOOP#---------------------------------------#
while True:
    fps.tick(60)
    screen.fill(BACKGROUND)
    #keep track of rounds
    turn_counter.append('x')
    #increase player stats for holding more wins
    if turn_counter.count('w') > 0:
        upgrade = choice(stats)
        if upgrade == stats[0]:
            playerhp+=10
        else:
            playeratk+=1
    #character setup and placements
    hero = Player('hero', 75, 75, 235, playerhp, playeratk)
    enemy_types = {
        'ghost' : [120, 15, ghostyell],
        'hand' : [80, 26, punch],
        'dog' : [170, 13, bite],
    }
    enemy = choice(list(enemy_types))
    enemyhp = enemy_types[enemy][0]
    enemyatk = enemy_types[enemy][1]
    enemyattack = enemy_types[enemy][2]
    monster = Enemy(f'{enemy}', 365, 365, 235, enemyhp, enemyatk)
    #set turn-based combat variables
    player_turn = 'Player'
    loop = 0
    #------START MENU
    while start_menu:
        fps.tick(60)
        screen.blit(start, (0,0))

        if st_btn.display(screen):
            start_menu = False
            game_run = True
        if qt_btn.display(screen):
            start_menu = False

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                start_menu = False
        pygame.display.update()

    #------CORE GAME LOOP
    while game_run:
        fps.tick(60)
        #set background images
        set_background()

        #MENU - PLAYER
        text_gen(f'HERO', WHITE, 70, 340)
        text_gen(f'HP: {hero.health}', WHITE, 60, 360)
        #MENU - ENEMY
        text_gen(f'MONSTER', WHITE, 350, 340)
        text_gen(f'HP: {monster.health}', WHITE, 340, 360)

        #display single sprite frame in designated location
        hero.update()
        hero.display(screen)

        monster.update()
        monster.display(screen)

        #player turn
        if player_turn == 'Player':
            text_gen(f'Your turn:', WHITE, 185, 338)
            if hero.frame_index >= 0 and hero.frame_index <=5:
                if atk_btn.display(screen,'Attack with your sword!',180,395):
                    dealt = attack_turn() 
                    loop+=1
                if hl_btn.display(screen,'Concentrate and heal 5-25 HP',180,395):
                    healed = heal_turn()
                    loop +=1
                if mg_btn.display(screen,'Could do a little or a lot',180,395):
                    magic_dealt = magic_turn()
                    loop +=1
            if loop > 0:
                if hero.frame_index < 12 and hero.frame_index > 5:
                    text_gen(f'You attack!', WHITE, 170, 390)
                    text_gen(f'Enemy takes {dealt} damage.', WHITE, 130, 420)
                if hero.frame_index > 11 and hero.frame_index <= 17:
                    text_gen(f'Healed for {healed}.', WHITE, 170, 405)
                if hero.frame_index <= 27 and hero.frame_index >= 22:
                    text_gen(f'You cast fire!', WHITE, 160, 390)
                    text_gen(f'Enemy takes {magic_dealt} damage.', WHITE, 130, 420)
                if hero.frame_index == 11 or hero.frame_index == 17 or hero.frame_index == 27:
                    last_turn = player_turn
                    if monster.check_alive():
                        player_turn = 'wait'
                    else:
                        player_turn = 'game_over'
        #enemy turn
        if player_turn == 'Enemy':
            if monster.frame_index == 5:
                loop+=1
            if loop < 2:
                text_gen(f'Enemy\'s turn!', WHITE, 165, 338)
            if loop == 3:
                damage = enemy_turn()
                loop+=1
            if loop > 3:
                if monster.frame_index <= 11 and monster.frame_index > 5:
                    text_gen(f'Enemy attacks you!', WHITE, 150, 390)
                    text_gen(f'You take {damage} damage.', WHITE, 140, 420) #AMOUNT
                if monster.frame_index == 11:
                    last_turn = player_turn
                    if hero.check_alive():
                        player_turn = 'wait'
                    else:
                        player_turn = 'game_over'
        #wait to alternate turns
        if player_turn == 'wait':
            if hero.status == 'idle' and monster.status == 'idle' and last_turn == 'Player':
                player_turn = 'Enemy'
            if hero.status == 'idle' and monster.status == 'idle' and last_turn == 'Enemy':
                loop = 0
                player_turn = 'Player'
        #round ends
        if player_turn == 'game_over':
            if not hero.check_alive(): 
                pygame.mixer.Sound.play(losesound, 0)
                game_end()
                end_screen = True
                game_run = False
            elif not monster.check_alive():
                pygame.mixer.Sound.play(winsound, 0)
                game_end()
                end_screen = True
                game_run = False

        # show heal fx
        if hero.frame_index >= 12 and hero.frame_index <= 17:
            heal_time = pygame.time.get_ticks()
            if heal_time - last_update >= frame_duration:
                healframe += 1
                last_update = heal_time
                if healframe >= len(healanim):
                    healframe = 0
                screen.blit(healanim[healframe], (80,240))

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_run = False

        pygame.display.update()
    #------END SCREEN
    while end_screen:
        fps.tick(60)
        if game_end() == 'win':
            turn_counter[-1] = 'w'
            screen.blit(win_card, (0,0))
            text_gen('YOU WON!', WHITE, 205, 205)
        if game_end() == 'lose':
            turn_counter[-1] = 'l'
            screen.blit(lose_card, (0,0))
            text_gen('YOU DIED...', WHITE, 195, 205)

        text_gen(f'Rounds played: {len(turn_counter)}', WHITE, 165, 70)
        text_gen('Play again?', WHITE, 185, 100)
        text_gen(f'Wins: {turn_counter.count("w")}', WHITE, 145, 0)
        text_gen(f'Losses: {turn_counter.count("l")}', WHITE, 245, 0)

        if yes.display(screen):
            game_run = True
            end_screen = False
        if no.display(screen):
            end_screen = False

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                end_screen = False
        
        pygame.display.update()
    if not start_menu and not game_run and not end_screen:
        sys.exit()