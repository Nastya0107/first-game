from random import randint
import pygame

from time import sleep
pygame.init()    #включаем модуль

width =  1200  #1369     #ширина
height = 600  #768     #высота
fps = 30      #кадров в секунду
game_name = "ОНО"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (width, height))
begin = pygame.image.load('begin.webp')
begin = pygame.transform.scale(begin, (width, height))
bg_1 = pygame.image.load('bg_1.webp')
bg_1 = pygame.transform.scale(bg_1, (width, height))
bg_2 = pygame.image.load('bg_2.jpg')
bg_2 = pygame.transform.scale(bg_2, (width, height))
bg_3 = pygame.image.load('bg_4-1.jpg')
bg_3 = pygame.transform.scale(bg_3, (width, height))
bg_4 = pygame.image.load('bg_3.jpg')
bg_4 = pygame.transform.scale(bg_4, (width, height))
uft = pygame.image.load('end.webp')
uft = pygame.transform.scale(uft, (width, height))
team = pygame.image.load('team.jpeg')
team = pygame.transform.scale(team, (width, height))

end_1 = pygame.image.load('end_1.webp')
end_1 = pygame.transform.scale(end_1, (width, height))
end_2 = pygame.image.load('end_2.webp')
end_2 = pygame.transform.scale(end_2, (width, height))
end_3 = pygame.image.load('end_3.jpg')
end_3 = pygame.transform.scale(end_3, (width, height))
end_4 = pygame.image.load('end_4.webp')
end_4 = pygame.transform.scale(end_4, (width, height))

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

rez = pygame.mixer.Sound('rez.mp3')


image_1 = 'door_1.png'
image_2 = 'door_2.png'
image_3 = 'door_3.png'
open_door_1 = 'open_door.png'

door_1 = pygame.image.load(image_1)
door_1_rect = door_1.get_rect()
door_2 = pygame.image.load(image_1)
door_2_rect = door_2.get_rect()
door_3 = pygame.image.load(image_3)
door_3_rect = door_3.get_rect()

open_door = pygame.image.load(open_door_1)
open_door_2 = pygame.image.load(open_door_1)
open_door_2_rect = open_door_2.get_rect()
open_door_3 = pygame.image.load(open_door_1)
open_door_3_rect = open_door_3.get_rect()
open_door_rect = open_door.get_rect()
open_door = pygame.transform.scale(open_door,(500,650))
open_door_2 = pygame.transform.scale(open_door_2,(500,650))
open_door_3 = pygame.transform.scale(open_door_3,(500,650))

screamer = pygame.image.load('screamer.webp')
screamer = pygame.transform.scale(screamer, (width, height))
screamer_1 = pygame.image.load('screamer_2.webp')
screamer_1 = pygame.transform.scale(screamer_1, (width, height))
screamer_2 = pygame.image.load('screamer_3.webp')
screamer_2 = pygame.transform.scale(screamer_2, (width, height))
screamer_3 = pygame.image.load('screamer_4.webp')
screamer_3 = pygame.transform.scale(screamer_3, (width, height))

player = pygame.image.load('georgia.png')
player_rect = player.get_rect()
open_door_rect.x -= 40
open_door_2_rect.x = open_door_rect.right + 20
open_door_3_rect.x = open_door_2_rect.right

door_1_rect.y = 100
door_1_rect.x = 100
door_2_rect.y = 100
door_2_rect.x = door_1_rect.right + 50
door_3_rect.y = 100
door_3_rect.x = door_2_rect.right + 50
player_rect.y = 300
player_rect.x = door_3_rect.right + 100
run = True
timer = pygame.time.Clock()
t_begin = 1
count = 0
can = True
door_open = False
dor = True
dor_2 = True
dor_3 = True
chance = 0
def which_door():
    global key
    if key[pygame.K_1]:
        screen.blit(open_door, open_door_rect)
    elif key[pygame.K_2]:
        screen.blit(open_door_2, open_door_2_rect)
    elif key[pygame.K_3]:
        screen.blit(open_door_3, open_door_3_rect)
def win(click):
    global dor, count, can, door_open
    if click:
        door_open = True
        if door_open == True:
            if count >= 5 and count < 10:
                screen.blit(bg_1, (0, 0))
            elif count > 0 and count < 5:
                screen.blit(bg, (0, 0))
            elif count >= 10 and count < 15:
                screen.blit(bg_2, (0, 0))
            elif count >= 15 and count < 20:
                screen.blit(bg_3, (0, 0))
            elif count >= 20 and count < 25:
                screen.blit(bg_4, (0, 0))
            which_door()
            pygame.display.update()
            sleep(1)
        if can == True:
            count += 1
        dor = False
        can = False

def loose(click):
    if click:
        rez.play()
        screen.blit(screamer_1, (0, 0))
        pygame.display.update()
        sleep(1)
def loose_1(click):
    if click :
        rez.play()
        screen.blit(screamer, (0, 0))
        pygame.display.update()
        sleep(1)
def loose_2(click):
    if click :
        rez.play()
        screen.blit(screamer_2, (0, 0))
        pygame.display.update()
        sleep(1)
def loose_3(click):
    if click :
        rez.play()
        screen.blit(screamer_3, (0, 0))
        pygame.display.update()
        sleep(1)
def ran(click1):
    global choose
    choose = randint(1, 6)
    if choose == 1 or choose == 3 :
        win(click1)
    if choose == 5:
        loose(click1)
    if choose == 4:
        loose_1(click1)
    if choose == 6:
        loose_2(click1)
    if choose == 2:
        loose_3(click1)
def do():
    one = key[pygame.K_1]
    two = key[pygame.K_2]
    three = key[pygame.K_3]
    ran(one)
    ran(two)
    ran(three)
def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')    # Выбираем тип шрифта для текста
    font = pygame.font.Font(font_name, size)       # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)    # Превращаем текст в картинку
    text_rect = text_image.get_rect()              # Задаем рамку картинки с текстом
    text_rect.center = (x,y)                       # Переносим текст в координаты
    screen.blit(text_image, text_rect)             # Рисуем текст на экране
while run:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if count == 25:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('uft.mp3')
        pygame.mixer.music.set_volume(5)
        pygame.mixer.music.play(-1)
        screen.blit(uft,(0, 0))
        pygame.display.update()
        sleep(38)
        pygame.mixer.music.stop()
        pygame.mixer.music.load('stans_letter.mp3')
        pygame.mixer.music.set_volume(8)
        pygame.mixer.music.play(-1)
        screen.blit(team, (0, 0))
        pygame.display.update()
        sleep(10)
        screen.blit(end_1, (0, 0))
        pygame.display.update()
        sleep(5)
        screen.blit(end_2, (0, 0))
        pygame.display.update()
        sleep(5)
        screen.blit(end_3, (0, 0))
        pygame.display.update()
        sleep(5)
        screen.blit(end_4, (0, 0))
        pygame.display.update()
        sleep(5)
        exit()
    key = pygame.key.get_pressed()
    do()
    door_open = False
    dor = True
    dor_2 = True
    dor_3 = True
    can = True
    if t_begin == 1:
        screen.blit(begin,(0, 0))
        pygame.display.update()
        sleep(0.5)
        t_begin = 0
    screen.blit(bg, (0, 0))
    if count >= 5 and count < 10:
        screen.blit(bg_1,(0, 0))
    elif count >= 10 and count < 15:
        screen.blit(bg_2,(0, 0))
    elif count >= 15 and count < 20:
        screen.blit(bg_3,(0, 0))
    elif count >= 20 and count < 25:
        screen.blit(bg_4, (0, 0))
    draw_text(screen, "Количество успешно пройденных дверей: "+str(count), 50, height, 50, 'white')
    if dor == True:
        screen.blit(door_1, door_1_rect)
    if dor_2 == True:
        screen.blit(door_2, door_2_rect)
    if dor_3 == True:
        screen.blit(door_3, door_3_rect)
    screen.blit(player, player_rect)
    pygame.display.update()