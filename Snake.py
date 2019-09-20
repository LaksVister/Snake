""" Snake Version 1.0"""
import pygame
import random


def eat():
    """
    :return: 0..528
    """
    return random.randrange(529)


def get_eat():
    """
    Recursion
    :return eat not in li and eat not in spawn 3x3
    """
    global li
    ea = eat()
    if ea <= 519 and ea not in li:
        return li.append(ea)
    else:
        return get_eat()


def get_eat2():
    """
    Recursion
    :return eat not in li and eat not in snake
    """
    global li
    global eat_zone
    global memory
    ea = eat()
    if ea not in li and (eat_zone[ea][0], eat_zone[ea][1]) not in memory:
        return ea
    else:
        return get_eat2()


def random_color_eat():
    """
    :100% all:
    50% for green
    30% for blue
    19% for orange
    1% for pink
    :return: colour of eat
    """
    random_number = random.randrange(100) + 1
    if random_number <= 50:
        return 0  # GREEN
    if 50 < random_number <= 80:
        return 1  # BLUE
    if 80 < random_number <= 99:
        return 2  # ORANGE
    if 99 < random_number <= 100:
        return 3  # PINK


pygame.init()
pygame.display.set_caption("Snake v1.0")
size_screen = (1024, 768)
window = pygame.display.set_mode(size_screen)
running = True
menu_options = False
game_start = False
right_clicked = True
left_clicked = False
up_clicked = False
down_clicked = False
not_delete = True
game_over = False
inf = True
game_pause = False
skip = 1
with open('option.txt') as setting_option:
    li_gaming_keyboard = setting_option.readline().split()
    li_death_wall = setting_option.readline().split()
    li_music = setting_option.readline().split()
    li_sound = setting_option.readline().split()
    li_fast_speed = setting_option.readline().split()
gaming_keyboard = eval(li_gaming_keyboard[2])
death_wall = eval(li_death_wall[2])
music = eval(li_music[2])
sound = eval(li_sound[2])
fast_speed = eval(li_fast_speed[2])
paschal = True
change_music = True
start_music_in_game = True
game_again = False

# Colors
WHITE = (255, 255, 255)
GREEN = (54, 97, 37)
BLUE = (0, 72, 186)
ORANGE = (255, 165, 0)
PINK = (255, 105, 180)
color_eat = (GREEN, BLUE, ORANGE, PINK)
green = 1
blue = 10
orange = 50
pink = 100
LIME = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Options
class move_green_rect_on:
    """
    Settings attributes on
    """
    gaming_keyboard = 35
    death_wall = 151
    music = 280
    sound = 407
    fast_speed = 531


class move_green_rect_off:
    """
    Settings attributes off
    """
    gaming_keyboard = 35
    death_wall = 151
    music = 280
    sound = 407
    fast_speed = 531


def on_off(true_false):
    """
    Initial Settings
    :param true_false:
    :return: (on, off)
    """
    if true_false:
        return 0, 28
    else:
        return 28, 0


gaming_keyboard_on_off = on_off(death_wall)
death_wall_on_off = on_off(death_wall)
music_on_off = on_off(music)
sound_on_off = on_off(sound)
fast_speed_on_off = on_off(fast_speed)

# Record
with open('save.txt') as read:
    record = read.readline().rstrip()

# Snake
SKIN_OF_SNAKE = (61, 31, 81)
x = 16
y = 16
width = 32
height = 32
speed = 32
# size_snake = 3
re = 0

# Random eat:
size = (734 + 2 + 16, 734 + 2 + 16)
li = []
for _ in range(3):
    get_eat()
eat_zone = {}
i = size[0] - width
j = size[1]
s = 0
for _x in range(size[0] // width):
    for _y in range(size[1] // height):
        j -= height
        eat_zone[s] = (i, j, width, height)
        s += 1
    i -= width
    j = size[1]
ce1 = random_color_eat()
ce2 = random_color_eat()
ce3 = random_color_eat()

# Points
points = 0

# Memory of mouse down
memory_of_mouse = []

# Memory size of Snake
memory = []

# Smart Snake
memory_of_move = []

# Food basket
memory_of_eat = []

# Memory of pressed button
memory_of_button = []

# Music load

pygame.mixer.init()
pygame.mixer.music.load("musics/Kring _ www.wowa.me.mp3")

# Sound load

sound_posClick = pygame.mixer.Sound('sounds/Click.wav')
sound_Alien = pygame.mixer.Sound('sounds/Alien.wav')
sound_Eating = pygame.mixer.Sound('sounds/EatingApple.wav')

# Images load
image_Continue = pygame.image.load('buttons/continue/Continue.png').convert_alpha()
image_posContinue = pygame.image.load('buttons/continue/posContinue.png').convert_alpha()
image_presContinue = pygame.image.load('buttons/continue/presContinue.png').convert_alpha()
image_NewGame = pygame.image.load('buttons/new_game/NewGame.png').convert_alpha()
image_posNewGame = pygame.image.load('buttons/new_game/posNewGame.png').convert_alpha()
image_presNewGame = pygame.image.load('buttons/new_game/presNewGame.png').convert_alpha()
image_Options = pygame.image.load('buttons/options/Options.png').convert_alpha()
image_posOptions = pygame.image.load('buttons/options/posOptions.png').convert_alpha()
image_presOptions = pygame.image.load('buttons/options/presOptions.png').convert_alpha()
image_Exit = pygame.image.load('buttons/exit/Exit.png').convert_alpha()
image_posExit = pygame.image.load('buttons/exit/posExit.png').convert_alpha()
image_presExit = pygame.image.load('buttons/exit/presExit.png').convert_alpha()
image_GameOver = pygame.image.load('names/GameOver.png').convert()
n0 = pygame.image.load('numbers/0.png').convert()
n1 = pygame.image.load('numbers/1.png').convert()
n2 = pygame.image.load('numbers/2.png').convert()
n3 = pygame.image.load('numbers/3.png').convert()
n4 = pygame.image.load('numbers/4.png').convert()
n5 = pygame.image.load('numbers/5.png').convert()
n6 = pygame.image.load('numbers/6.png').convert()
n7 = pygame.image.load('numbers/7.png').convert()
n8 = pygame.image.load('numbers/8.png').convert()
n9 = pygame.image.load('numbers/9.png').convert()
numbers = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
image_Pause = pygame.image.load('buttons/pause/Pause.png').convert_alpha()
image_posPause = pygame.image.load('buttons/pause/posPause.png').convert_alpha()
image_presPause = pygame.image.load('buttons/pause/presPause.png').convert_alpha()
image_RECORD = pygame.image.load('names/RECORD.png').convert_alpha()
image_Death_wall = pygame.image.load('names/Death_wall.png').convert_alpha()
image_Music = pygame.image.load('names/Music.png').convert_alpha()
image_Sound = pygame.image.load('names/Sound.png').convert_alpha()
image_Fast_speed = pygame.image.load('names/Fast_speed.png').convert_alpha()
image_on = pygame.image.load('buttons/on_off/on.png').convert_alpha()
image_off = pygame.image.load('buttons/on_off/off.png').convert_alpha()
image_gaming_keyboard = pygame.image.load('names/Gaming_keyboard.png').convert_alpha()
image_slash = pygame.image.load('names/slash.png').convert_alpha()


def draw_window():
    """
    :return all draw on window
    """
    # Black background
    window.fill((0, 0, 0))

    # globals
    global gaming_keyboard_on_off
    global gaming_keyboard
    global game_again
    global start_music_in_game
    global change_music
    global paschal
    global fast_speed_on_off
    global music_on_off
    global sound_on_off
    global death_wall_on_off
    global fast_speed
    global sound
    global music
    global death_wall
    global memory_of_button
    global pink
    global orange
    global blue
    global green
    global record
    global skip
    global game_pause
    global right_clicked
    global left_clicked
    global down_clicked
    global up_clicked
    global memory_of_mouse
    global pos
    global ce1
    global ce2
    global ce3
    global points
    global color_eat
    global game_over
    global memory_of_move
    global memory
    global re
    global not_delete
    global size_snake
    global x
    global y
    global running
    global menu_options
    global game_start

    # Menu
    if not menu_options and not game_start and not game_over:

        # Continue
        Continue = window.blit(image_Continue, (424, 232))
        if Continue.collidepoint(pos):
            window.blit(image_posContinue, (424, 232))
        for button in memory_of_button:
            if button.key == pygame.K_RETURN:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presContinue, (424, 232))
                with open('save.txt') as r:
                    r.readline()
                    memory = eval(r.readline().rstrip())
                    size_snake = eval(r.readline().rstrip())
                    x = eval(r.readline().rstrip())
                    y = eval(r.readline().rstrip())
                    points = eval(r.readline().rstrip())
                    right_clicked = eval(r.readline().rstrip())
                    left_clicked = eval(r.readline().rstrip())
                    down_clicked = eval(r.readline().rstrip())
                    up_clicked = eval(r.readline())
                game_start = True
                game_pause = False
                memory_of_button = []
        if memory_of_mouse:
            if Continue.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presContinue, (424, 232))
                with open('save.txt') as r:
                    r.readline()
                    memory = eval(r.readline().rstrip())
                    size_snake = eval(r.readline().rstrip())
                    x = eval(r.readline().rstrip())
                    y = eval(r.readline().rstrip())
                    points = eval(r.readline().rstrip())
                    right_clicked = eval(r.readline().rstrip())
                    left_clicked = eval(r.readline().rstrip())
                    down_clicked = eval(r.readline().rstrip())
                    up_clicked = eval(r.readline())
                game_start = True
                game_pause = False
                memory_of_mouse = []

        # New game
        NewGame = window.blit(image_NewGame, (413, 291))
        if NewGame.collidepoint(pos):
            window.blit(image_posNewGame, (413, 291))
        for button in memory_of_button:
            if button.key == pygame.K_SPACE:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presNewGame, (413, 291))
                memory = []
                memory_of_move = []
                size_snake = 3
                x = 16
                y = 16
                points = 0
                right_clicked = True
                left_clicked = False
                down_clicked = False
                up_clicked = False
                game_start = True
                game_pause = False
        if memory_of_mouse:
            if NewGame.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presNewGame, (413, 291))
                memory = []
                memory_of_move = []
                size_snake = 3
                x = 16
                y = 16
                points = 0
                right_clicked = True
                left_clicked = False
                down_clicked = False
                up_clicked = False
                game_start = True
                game_pause = False

        # New game again
        if game_again:
            game_again = False
            game_start = True
            memory = []
            memory_of_move = []
            size_snake = 3
            x = 16
            y = 16
            points = 0
            right_clicked = True
            left_clicked = False
            down_clicked = False
            up_clicked = False
            game_start = True
            game_pause = False

        # Options
        Options = window.blit(image_Options, (430, 350))
        if Options.collidepoint(pos):
            window.blit(image_posOptions, (430, 350))
        for button in memory_of_button:
            if button.key == pygame.K_TAB:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presOptions, (430, 350))
                menu_options = True
                memory_of_button = []
        if memory_of_mouse:
            if Options.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presOptions, (430, 350))
                menu_options = True
                memory_of_mouse = []

        # Exit
        Exit = window.blit(image_Exit, (457, 409))
        if Exit.collidepoint(pos):
            window.blit(image_posExit, (457, 409))
        for button in memory_of_button:
            if button.key == pygame.K_ESCAPE:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 409))
                clock.tick(9)
                running = False
            memory_of_button = []
        if memory_of_mouse:
            if Exit.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 409))
                clock.tick(9)
                running = False
                memory_of_mouse = []

    # Options menu
    if menu_options:
        Exit = window.blit(image_Exit, (457, 638))
        if Exit.collidepoint(pos):
            window.blit(image_posExit, (457, 638))
        for button in memory_of_button:
            if button.key == pygame.K_ESCAPE or button.key == pygame.K_TAB:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 638))
                with open('option.txt', 'w') as set_in_op:
                    set_in_op.write(f'death_wall = {gaming_keyboard}\n')
                    set_in_op.write(f'death_wall = {death_wall}\n')
                    set_in_op.write(f'music = {music}\n')
                    set_in_op.write(f'sound = {sound}\n')
                    set_in_op.write(f'fast_speed = {fast_speed}')
                menu_options = False
                memory_of_button = []
        if memory_of_mouse:
            if Exit.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 638))
                with open('option.txt', 'w') as set_in_op:
                    set_in_op.write(f'death_wall = {gaming_keyboard}\n')
                    set_in_op.write(f'death_wall = {death_wall}\n')
                    set_in_op.write(f'music = {music}\n')
                    set_in_op.write(f'sound = {sound}\n')
                    set_in_op.write(f'fast_speed = {fast_speed}')
                menu_options = False
                memory_of_mouse = []

        # Gaming keyboard
        pygame.draw.rect(window, LIME, (580, move_green_rect_on.gaming_keyboard + gaming_keyboard_on_off[0], 28, 28))
        pygame.draw.rect(window, LIME, (772, move_green_rect_off.gaming_keyboard + gaming_keyboard_on_off[1], 28, 28))
        pygame.draw.rect(window, BLACK, (580, 63, 28, 28))
        pygame.draw.rect(window, BLACK, (772, 63, 28, 28))

        # Death wall
        pygame.draw.rect(window, LIME, (580, move_green_rect_on.death_wall + death_wall_on_off[0], 28, 28))
        pygame.draw.rect(window, LIME, (772, move_green_rect_off.death_wall + death_wall_on_off[1], 28, 28))
        pygame.draw.rect(window, BLACK, (580, 179, 28, 28))
        pygame.draw.rect(window, BLACK, (772, 179, 28, 28))

        # Music
        pygame.draw.rect(window, LIME, (580, move_green_rect_on.music + music_on_off[0], 28, 28))
        pygame.draw.rect(window, LIME, (772, move_green_rect_off.music + music_on_off[1], 28, 28))
        pygame.draw.rect(window, BLACK, (580, 308, 28, 28))
        pygame.draw.rect(window, BLACK, (772, 308, 28, 28))

        # Sound
        pygame.draw.rect(window, LIME, (580, move_green_rect_on.sound + sound_on_off[0], 28, 28))
        pygame.draw.rect(window, LIME, (772, move_green_rect_off.sound + sound_on_off[1], 28, 28))
        pygame.draw.rect(window, BLACK, (580, 435, 28, 28))
        pygame.draw.rect(window, BLACK, (772, 435, 28, 28))

        # Fast speed
        pygame.draw.rect(window, LIME, (580, move_green_rect_on.fast_speed + fast_speed_on_off[0], 28, 28))
        pygame.draw.rect(window, LIME, (772, move_green_rect_off.fast_speed + fast_speed_on_off[1], 28, 28))
        pygame.draw.rect(window, BLACK, (580, 559, 28, 28))
        pygame.draw.rect(window, BLACK, (772, 559, 28, 28))

        # Names
        window.blit(image_gaming_keyboard, (176, 14))
        window.blit(image_Death_wall, (196, 147))
        window.blit(image_Music, (237, 276))
        window.blit(image_Sound, (232, 403))
        window.blit(image_Fast_speed, (199, 528))
        Gaming_keyboard_on = window.blit(image_on, (504, 16))
        Death_wall_on = window.blit(image_on, (504, 132))
        Music_on = window.blit(image_on, (504, 261))
        Sound_on = window.blit(image_on, (504, 388))
        Fast_speed_on = window.blit(image_on, (504, 512))
        window.blit(image_slash, (638, 7))
        Gaming_keyboard_off = window.blit(image_on, (696, 16))
        Death_wall_off = window.blit(image_off, (693, 132))
        Music_off = window.blit(image_off, (693, 261))
        Sound_off = window.blit(image_off, (693, 388))
        Fast_speed_off = window.blit(image_off, (693, 512))

        # Gaming keyboard animation
        for button in memory_of_button:
            if button.key == pygame.K_g or button.key == pygame.K_k or button.key == pygame.K_b:
                if not gaming_keyboard:
                    if sound:
                        sound_posClick.play()
                    gaming_keyboard = True
                    memory_of_button = []
        if memory_of_mouse:
            if Gaming_keyboard_on.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if not gaming_keyboard:
                    if sound:
                        sound_posClick.play()
                    gaming_keyboard = True
                    memory_of_button = []
        for button in memory_of_button:
            if button.key == pygame.K_g or button.key == pygame.K_k or button.key == pygame.K_b:
                if gaming_keyboard:
                    if sound:
                        sound_posClick.play()
                    gaming_keyboard = False
                    memory_of_button = []
        if memory_of_mouse:
            if Gaming_keyboard_off.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if gaming_keyboard:
                    if sound:
                        sound_posClick.play()
                    gaming_keyboard = False
                    memory_of_button = []
        if not gaming_keyboard:
            if move_green_rect_off.gaming_keyboard > 7 + gaming_keyboard_on_off[0]:
                move_green_rect_on.gaming_keyboard += 2
                move_green_rect_off.gaming_keyboard -= 2
        else:
            if move_green_rect_on.gaming_keyboard > 7 + gaming_keyboard_on_off[1]:
                move_green_rect_on.gaming_keyboard -= 2
                move_green_rect_off.gaming_keyboard += 2

        # Death wall animation
        for button in memory_of_button:
            if button.key == pygame.K_d:
                if not death_wall:
                    if sound:
                        sound_posClick.play()
                    death_wall = True
                    memory_of_button = []
        if memory_of_mouse:
            if Death_wall_on.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if not death_wall:
                    if sound:
                        sound_posClick.play()
                    death_wall = True
                    memory_of_mouse = []
        for button in memory_of_button:
            if button.key == pygame.K_d:
                if death_wall:
                    if sound:
                        sound_posClick.play()
                    death_wall = False
                    memory_of_button = []
        if memory_of_mouse:
            if Death_wall_off.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if death_wall:
                    if sound:
                        sound_posClick.play()
                    death_wall = False
                    memory_of_mouse = []
        if not death_wall:
            if move_green_rect_off.death_wall > 123 + death_wall_on_off[0]:
                move_green_rect_on.death_wall += 2
                move_green_rect_off.death_wall -= 2
        else:
            if move_green_rect_on.death_wall > 123 + death_wall_on_off[1]:
                move_green_rect_on.death_wall -= 2
                move_green_rect_off.death_wall += 2

        # Music animation
        for button in memory_of_button:
            if button.key == pygame.K_m or button.key == pygame.K_a:
                if music:
                    if sound:
                        sound_posClick.play()
                    pygame.mixer.music.stop()
                    music = False
                    memory_of_button = []
        if memory_of_mouse:
            if Music_on.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if not music:
                    if sound:
                        sound_posClick.play()
                    change_music = True
                    music = True
                    memory_of_mouse = []
        for button in memory_of_button:
            if button.key == pygame.K_m or button.key == pygame.K_a:
                if not music:
                    if sound:
                        sound_posClick.play()
                    change_music = True
                    music = True
                    memory_of_button = []
        if memory_of_mouse:
            if Music_off.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if music:
                    if sound:
                        sound_posClick.play()
                    pygame.mixer.music.stop()
                    music = False
                    memory_of_mouse = []
        if not music:
            if move_green_rect_off.music > 252 + music_on_off[0]:
                move_green_rect_on.music += 2
                move_green_rect_off.music -= 2
        else:
            if move_green_rect_on.music > 252 + music_on_off[1]:
                move_green_rect_on.music -= 2
                move_green_rect_off.music += 2

        # Sound animation
        for button in memory_of_button:
            if button.key == pygame.K_s:
                if not sound:
                    sound_posClick.play()
                    sound = True
                    memory_of_button = []
        if memory_of_mouse:
            if Sound_on.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if not sound:
                    sound_posClick.play()
                    sound = True
                    memory_of_mouse = []
        for button in memory_of_button:
            if button.key == pygame.K_s:
                sound = False
                memory_of_button = []
        if memory_of_mouse:
            if Sound_off.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                sound = False
                memory_of_mouse = []
        if not sound:
            if move_green_rect_off.sound > 379 + sound_on_off[0]:
                move_green_rect_on.sound += 2
                move_green_rect_off.sound -= 2
        else:
            if move_green_rect_on.sound > 379 + sound_on_off[1]:
                move_green_rect_on.sound -= 2
                move_green_rect_off.sound += 2

        # Fast speed animation
        for button in memory_of_button:
            if button.key == pygame.K_f:
                if not fast_speed:
                    if sound:
                        sound_posClick.play()
                    fast_speed = True
                    memory_of_button = []
        if memory_of_mouse:
            if Fast_speed_on.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if not fast_speed:
                    if sound:
                        sound_posClick.play()
                    fast_speed = True
                    memory_of_mouse = []
        for button in memory_of_button:
            if button.key == pygame.K_f:
                if fast_speed:
                    if sound:
                        sound_posClick.play()
                    fast_speed = False
                    memory_of_button = []
        if memory_of_mouse:
            if Fast_speed_off.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if fast_speed:
                    if sound:
                        sound_posClick.play()
                    fast_speed = False
                    memory_of_mouse = []
        if not fast_speed:
            if move_green_rect_off.fast_speed > 503 + fast_speed_on_off[0]:
                move_green_rect_on.fast_speed += 2
                move_green_rect_off.fast_speed -= 2
        else:
            if move_green_rect_on.fast_speed > 503 + fast_speed_on_off[1]:
                move_green_rect_on.fast_speed -= 2
                move_green_rect_off.fast_speed += 2

    # Game start
    if game_start:
        if start_music_in_game:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("musics/Bowers & Wilkins _ www.wowa.me.mp3")
            change_music = True
            start_music_in_game = False

        # Continue
        if game_pause:
            Continue = window.blit(image_Continue, (800, 47))
            if Continue.collidepoint(pos):
                window.blit(image_posContinue, (800, 47))
            for button in memory_of_button:
                if button.key == pygame.K_ESCAPE:
                    if sound:
                        sound_posClick.play()
                    game_start = False
                    memory_of_button = []
                if button.key == pygame.K_RETURN or button.key == pygame.K_p:
                    if sound:
                        sound_posClick.play()
                    window.fill((0, 0, 0))
                    window.blit(image_presContinue, (800, 47))
                    game_pause = False
                    with open('save.txt') as r:
                        r.readline()
                        memory = eval(r.readline().rstrip())
                        size_snake = eval(r.readline().rstrip())
                        x = eval(r.readline().rstrip())
                        y = eval(r.readline().rstrip())
                        points = eval(r.readline().rstrip())
                        right_clicked = eval(r.readline().rstrip())
                        left_clicked = eval(r.readline().rstrip())
                        down_clicked = eval(r.readline().rstrip())
                        up_clicked = eval(r.readline())
                memory_of_button = []
            if memory_of_mouse:
                if Continue.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                    if sound:
                        sound_posClick.play()
                    window.fill((0, 0, 0))
                    window.blit(image_presContinue, (800, 47))
                    game_pause = False
                    with open('save.txt') as r:
                        r.readline()
                        memory = eval(r.readline().rstrip())
                        size_snake = eval(r.readline().rstrip())
                        x = eval(r.readline().rstrip())
                        y = eval(r.readline().rstrip())
                        points = eval(r.readline().rstrip())
                        right_clicked = eval(r.readline().rstrip())
                        left_clicked = eval(r.readline().rstrip())
                        down_clicked = eval(r.readline().rstrip())
                        up_clicked = eval(r.readline())
                    memory_of_mouse = []

        # Pause
        if not game_pause and skip == 1:
            Pause = window.blit(image_Pause, (816, 47))
            if Pause.collidepoint(pos):
                window.blit(image_posPause, (816, 47))
            for button in memory_of_button:
                if button.key == pygame.K_RETURN or button.key == pygame.K_p:
                    if sound:
                        sound_posClick.play()
                    window.fill((0, 0, 0))
                    window.blit(image_presPause, (816, 47))
                    game_pause = True
                    with open('save.txt', 'w') as write:
                        module_xp = 0
                        module_yp = 0
                        if right_clicked:
                            module_xp = 32
                        if left_clicked:
                            module_xp = -32
                        if down_clicked:
                            module_yp = 32
                        if up_clicked:
                            module_yp = -32
                        write.write(f'{record}\n')
                        write.write(f'{memory}\n')
                        write.write(f'{size_snake}\n')
                        write.write(f'{memory[-1:][0][0] + module_xp}\n')
                        write.write(f'{memory[-1:][0][1] + module_yp}\n')
                        write.write(f'{points}\n')
                        write.write(f'{right_clicked}\n')
                        write.write(f'{left_clicked}\n')
                        write.write(f'{down_clicked}\n')
                        write.write(f'{up_clicked}')
                    skip = 0
                    memory_of_button = []
            if memory_of_mouse:
                if Pause.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                    if sound:
                        sound_posClick.play()
                    window.fill((0, 0, 0))
                    window.blit(image_presPause, (816, 47))
                    game_pause = True
                    with open('save.txt', 'w') as write:
                        module_xp = 0
                        module_yp = 0
                        if right_clicked:
                            module_xp = 32
                        if left_clicked:
                            module_xp = -32
                        if down_clicked:
                            module_yp = 32
                        if up_clicked:
                            module_yp = -32
                        write.write(f'{record}\n')
                        write.write(f'{memory}\n')
                        write.write(f'{size_snake}\n')
                        write.write(f'{memory[-1:][0][0] + module_xp}\n')
                        write.write(f'{memory[-1:][0][1] + module_yp}\n')
                        write.write(f'{points}\n')
                        write.write(f'{right_clicked}\n')
                        write.write(f'{left_clicked}\n')
                        write.write(f'{down_clicked}\n')
                        write.write(f'{up_clicked}')
                    memory_of_mouse = []
                skip = 0
        if not game_pause:
            skip = 1

        # Exit
        Exit = window.blit(image_Exit, (836, 689))
        if Exit.collidepoint(pos):
            window.blit(image_posExit, (836, 689))
        for button in memory_of_button:
            if button.key == pygame.K_ESCAPE:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (836, 689))
                game_start = False
                start_music_in_game = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musics/Kring _ www.wowa.me.mp3")
                change_music = True
                with open('save.txt', 'w') as write:
                    module_xe = 0
                    module_ye = 0
                    if right_clicked:
                        module_xe = 32
                    if left_clicked:
                        module_xe = -32
                    if down_clicked:
                        module_ye = 32
                    if up_clicked:
                        module_ye = -32
                    write.write(f'{record}\n')
                    write.write(f'{memory}\n')
                    write.write(f'{size_snake}\n')
                    write.write(f'{memory[-1:][0][0] + module_xe}\n')
                    write.write(f'{memory[-1:][0][1] + module_ye}\n')
                    write.write(f'{points}\n')
                    write.write(f'{right_clicked}\n')
                    write.write(f'{left_clicked}\n')
                    write.write(f'{down_clicked}\n')
                    write.write(f'{up_clicked}')
            memory_of_button = []
        if memory_of_mouse:
            if Exit.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presExit, (836, 689))
                game_start = False
                start_music_in_game = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musics/Kring _ www.wowa.me.mp3")
                change_music = True
                with open('save.txt', 'w') as write:
                    module_xe = 0
                    module_ye = 0
                    if right_clicked:
                        module_xe = 32
                    if left_clicked:
                        module_xe = -32
                    if down_clicked:
                        module_ye = 32
                    if up_clicked:
                        module_ye = -32
                    write.write(f'{record}\n')
                    write.write(f'{memory}\n')
                    write.write(f'{size_snake}\n')
                    write.write(f'{memory[-1:][0][0] + module_xe}\n')
                    write.write(f'{memory[-1:][0][1] + module_ye}\n')
                    write.write(f'{points}\n')
                    write.write(f'{right_clicked}\n')
                    write.write(f'{left_clicked}\n')
                    write.write(f'{down_clicked}\n')
                    write.write(f'{up_clicked}')
            memory_of_mouse = []
        # Info
        pygame.draw.rect(window, GREEN, (784, 450, 32, 32))
        pygame.draw.rect(window, WHITE, (846, 464, 10, 3))
        pygame.draw.rect(window, BLUE, (784, 504, 32, 32))
        pygame.draw.rect(window, WHITE, (846, 518, 10, 3))
        pygame.draw.rect(window, ORANGE, (784, 556, 32, 32))
        pygame.draw.rect(window, WHITE, (846, 570, 10, 3))
        pygame.draw.rect(window, PINK, (784, 608, 32, 32))
        pygame.draw.rect(window, WHITE, (846, 622, 10, 3))
        step_x = 0
        for number in str(green):
            window.blit(numbers[int(number)], (888 + step_x, 450))
            step_x += 28
        step_x = 0
        for number in str(blue):
            window.blit(numbers[int(number)], (888 + step_x, 504))
            step_x += 28
        step_x = 0
        for number in str(orange):
            window.blit(numbers[int(number)], (888 + step_x, 556))
            step_x += 28
        step_x = 0
        for number in str(pink):
            window.blit(numbers[int(number)], (888 + step_x, 608))
            step_x += 28

        # Record
        window.blit(image_RECORD, (795, 262))
        step_x = 0
        for _ in range(len(str(record)) - 1):
            step_x -= 28
        if len(str(record)) >= 8:
            for number in str(record):
                window.blit(numbers[int(number)], (972 + step_x, 352))
                step_x += 28
        else:
            for number in str(record):
                window.blit(numbers[int(number)], (944 + step_x, 352))
                step_x += 28

        # Points
        if points >= 99999999:
            points = 99999999
        if points <= 99999999:
            step_x = 0
            for _ in range(len(str(points)) - 1):
                step_x -= 28
            for number in str(points):
                window.blit(numbers[int(number)], (972 + step_x, 180))
                step_x += 28

        # Menu of game
        pygame.draw.polygon(window, WHITE, ((14, 14), (14, 752), (752, 752), (752, 14)), 2)  # game
        pygame.draw.polygon(window, WHITE, ((762, 14), (1010, 14), (1010, 148), (762, 148)), 2)  # continue/start
        pygame.draw.polygon(window, WHITE, ((762, 164), (1010, 164), (1010, 674), (762, 674)), 2)  # frame
        pygame.draw.polygon(window, WHITE, ((770, 172), (1002, 172), (1002, 228), (770, 228)), 3)  # points
        pygame.draw.polygon(window, WHITE, ((770, 240), (1002, 240), (1002, 428), (770, 428)), 1)  # skill active time
        pygame.draw.polygon(window, WHITE, ((770, 434), (1002, 434), (1002, 666), (770, 666)), 1)  # result of skill

        # Spawn eat
        pygame.draw.rect(window, color_eat[ce1], eat_zone[li[0]])
        pygame.draw.rect(window, color_eat[ce2], eat_zone[li[1]])
        pygame.draw.rect(window, color_eat[ce3], eat_zone[li[2]])
        if paschal:
            pygame.draw.rect(window, RED, (784, 688, 32, 32))

        # Draw Snake
        if not game_pause:
            memory.append((x, y))
        for x, y in memory:
            pygame.draw.rect(window, SKIN_OF_SNAKE, (x, y, width, height))

        # Clear/Add machine
        if memory[-1] == (eat_zone[li[0]][0], eat_zone[li[0]][1]):
            if sound:
                sound_Eating.play()
            not_delete = False
            re = 1
            li.remove(li[0])
            li.insert(0, get_eat2())
            if ce1 == 0:
                points += green
            elif ce1 == 1:
                points += blue
            elif ce1 == 2:
                points += orange
            elif ce1 == 3:
                points += pink
            ce1 = random_color_eat()
        if memory[-1] == (eat_zone[li[1]][0], eat_zone[li[1]][1]):
            if sound:
                sound_Eating.play()
            not_delete = False
            re = 1
            li.remove(li[1])
            li.insert(1, get_eat2())
            if ce2 == 0:
                points += green
            elif ce2 == 1:
                points += blue
            elif ce2 == 2:
                points += orange
            elif ce2 == 3:
                points += pink
            ce2 = random_color_eat()
        if memory[-1] == (eat_zone[li[2]][0], eat_zone[li[2]][1]):
            if sound:
                sound_Eating.play()
            not_delete = False
            re = 1
            li.remove(li[2])
            li.insert(2, get_eat2())
            if ce3 == 0:
                points += green
            elif ce3 == 1:
                points += blue
            elif ce3 == 2:
                points += orange
            elif ce3 == 3:
                points += pink
            ce3 = random_color_eat()
        if paschal and memory[-1] == (784, 688):
            if sound:
                sound_Eating.play()
                sound_Alien.play()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("musics/Piratos _ www.wowa.me.mp3")
            change_music = True
            points = 99999999
            paschal = False

    # Game over
    if game_over:
        with open('save.txt', 'w') as re:
            if points > int(record):
                record = points
                re.write(f'{points}\n')
            else:
                re.write(f'{record}\n')
            re.write(f'[]\n')
            re.write(f'3\n')
            re.write(f'16\n')
            re.write(f'16\n')
            re.write(f'0\n')
            re.write(f'True\n')
            re.write(f'False\n')
            re.write(f'False\n')
            re.write(f'False')
        game_start = False

        # Game Over: background
        window.blit(image_GameOver, (0, 0))

        # Game Over: New game
        NewGame = window.blit(image_NewGame, (413, 575))
        if NewGame.collidepoint(pos):
            window.blit(image_posNewGame, (413, 575))
        for button in memory_of_button:
            if button.key == pygame.K_SPACE:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presNewGame, (413, 575))
                game_over = False
                game_again = True
                memory_of_button = []
        if memory_of_mouse:
            if NewGame.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                window.fill((0, 0, 0))
                window.blit(image_presNewGame, (413, 575))
                game_over = False
                game_again = True
                memory_of_mouse = []

        # Game Over: Exit
        Exit = window.blit(image_Exit, (457, 650))
        if Exit.collidepoint(pos):
            window.blit(image_posExit, (457, 650))
        for button in memory_of_button:
            if button.key == pygame.K_ESCAPE:
                if sound:
                    sound_posClick.play()
                start_music_in_game = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musics/Kring _ www.wowa.me.mp3")
                change_music = True
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 650))
                game_over = False
                memory_of_button = []
        if memory_of_mouse:
            if Exit.collidepoint(memory_of_mouse[0].pos) and memory_of_mouse[0].button:
                if sound:
                    sound_posClick.play()
                start_music_in_game = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musics/Kring _ www.wowa.me.mp3")
                change_music = True
                window.fill((0, 0, 0))
                window.blit(image_presExit, (457, 650))
                game_over = False
                memory_of_mouse = []

    memory_of_button = []
    memory_of_mouse = []
    pygame.display.update()


# FPS by clock
clock = pygame.time.Clock()

# Main Loop
while running:

    # Restart music
    if music:
        while change_music:
            pygame.mixer.music.play(-1)
            change_music = False

    # Mouse position and button clicking.
    pos = pygame.mouse.get_pos()
    click_mouse_left, click_mouse_middle, click_mouse_right = pygame.mouse.get_pressed()

    while game_start:

        # Restart music
        if music:
            while change_music:
                pygame.mixer.music.play(-1)
                change_music = False

        # Mouse position and button clicking.
        pos = pygame.mouse.get_pos()
        click_mouse_left, click_mouse_middle, click_mouse_right = pygame.mouse.get_pressed()

        # Key buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('save.txt', 'w') as wr:
                    module_x = 0
                    module_y = 0
                    if right_clicked:
                        module_x = 32
                    if left_clicked:
                        module_x = -32
                    if down_clicked:
                        module_y = 32
                    if up_clicked:
                        module_y = -32
                    wr.write(f'{record}\n')
                    wr.write(f'{memory[1:]}\n')
                    wr.write(f'{size_snake}\n')
                    wr.write(f'{memory[-1:][0][0] + module_x}\n')
                    wr.write(f'{memory[-1:][0][1] + module_y}\n')
                    wr.write(f'{points}\n')
                    wr.write(f'{right_clicked}\n')
                    wr.write(f'{left_clicked}\n')
                    wr.write(f'{down_clicked}\n')
                    wr.write(f'{up_clicked}')
                game_start = False
                running = False
            if event.type == pygame.KEYDOWN:
                memory_of_move.append(event)
                memory_of_button.append(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                memory_of_mouse.append(event)
        if gaming_keyboard:
            for _ in memory_of_move:
                if memory_of_move[0].key == pygame.K_RIGHT and not left_clicked \
                        or memory_of_move[0].key == pygame.K_d and not left_clicked:
                    right_clicked = True
                    left_clicked = False
                    down_clicked = False
                    up_clicked = False
                    del memory_of_move[0]
                    break
                elif memory_of_move[0].key == pygame.K_LEFT and not right_clicked \
                        or memory_of_move[0].key == pygame.K_a and not right_clicked:
                    left_clicked = True
                    right_clicked = False
                    down_clicked = False
                    up_clicked = False
                    del memory_of_move[0]
                    break
                elif memory_of_move[0].key == pygame.K_DOWN and not up_clicked \
                        or memory_of_move[0].key == pygame.K_s and not up_clicked:
                    down_clicked = True
                    right_clicked = False
                    left_clicked = False
                    up_clicked = False
                    del memory_of_move[0]
                    break
                elif memory_of_move[0].key == pygame.K_UP and not down_clicked \
                        or memory_of_move[0].key == pygame.K_w and not down_clicked:
                    up_clicked = True
                    right_clicked = False
                    left_clicked = False
                    down_clicked = False
                    del memory_of_move[0]
                    break
                else:
                    memory_of_move = []
                    break
        if not gaming_keyboard:
            for _ in memory_of_move:
                if memory_of_move[0].key == pygame.K_RIGHT \
                        or memory_of_move[0].key == pygame.K_d:
                    if right_clicked:
                        down_clicked = True
                        right_clicked = False
                        left_clicked = False
                        up_clicked = False
                    elif down_clicked:
                        left_clicked = True
                        right_clicked = False
                        down_clicked = False
                        up_clicked = False
                    elif left_clicked:
                        up_clicked = True
                        right_clicked = False
                        left_clicked = False
                        down_clicked = False
                    elif up_clicked:
                        right_clicked = True
                        left_clicked = False
                        down_clicked = False
                        up_clicked = False
                    del memory_of_move[0]
                    break
                elif memory_of_move[0].key == pygame.K_LEFT \
                        or memory_of_move[0].key == pygame.K_a:
                    if right_clicked:
                        up_clicked = True
                        right_clicked = False
                        left_clicked = False
                        down_clicked = False
                    elif up_clicked:
                        left_clicked = True
                        right_clicked = False
                        down_clicked = False
                        up_clicked = False
                    elif left_clicked:
                        down_clicked = True
                        right_clicked = False
                        left_clicked = False
                        up_clicked = False
                    elif down_clicked:
                        right_clicked = True
                        left_clicked = False
                        down_clicked = False
                        up_clicked = False
                    del memory_of_move[0]
                    break
                else:
                    memory_of_move = []
                    break
        if not game_pause:
            if right_clicked:
                x += speed
            elif left_clicked:
                x -= speed
            elif down_clicked:
                y += speed
            elif up_clicked:
                y -= speed

        # Set options: death wall
        if death_wall:
            if x == -16 or x == 752 or y == -16 or y == 752:
                game_over = True
        else:
            if x <= -16:
                x = 720
            if x >= 752:
                x = 16
            if y <= -16:
                y = 720
            if y >= 752:
                y = 16

        if memory[-1] in memory[:-1]:
            game_over = True

        # Memory size of Snake
        if not game_pause:
            if size_snake < 100:
                size_snake -= 1
            if size_snake == 1:
                size_snake = 100
            elif size_snake == 100 and not_delete:
                del memory[0]
            if re == 1:
                not_delete = True
                re = 0

        # Draw on window.
        draw_window()

        # FPS game
        if not fast_speed:
            clock.tick(6)
        else:
            clock.tick(18)

    # Draw on window.
    draw_window()

    # Quit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('option.txt', 'w') as set_op:
                set_op.write(f'death_wall = {gaming_keyboard}\n')
                set_op.write(f'death_wall = {death_wall}\n')
                set_op.write(f'music = {music}\n')
                set_op.write(f'sound = {sound}\n')
                set_op.write(f'fast_speed = {fast_speed}')
            running = False
        if event.type == pygame.KEYDOWN:
            memory_of_button.append(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            memory_of_mouse.append(event)

    # FPS menu and emergency exit.
    clock.tick(32)

# Emergency exit
pygame.quit()
