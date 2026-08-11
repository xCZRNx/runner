from math import trunc
from warnings import catch_warnings
import pygame
from sys import exit, path_importer_cache
from pygame import key
from random import randint
from random import choice

from pygame.constants import K_SPACE, KSCAN_Y, K_s

def display_score():
    time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = text_font.render(f'{time}',False,"black")
    score_rect = score_surf.get_rect(topright = (750,10))
    pygame.draw.rect(screen,"Blue",score_rect,20)
    pygame.draw.rect(screen,"blue",score_rect)
    screen.blit(score_surf,score_rect)

def movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= GAMESPEED
            if obstacle_rect.bottom == 351:
                screen.blit(obstacle_1,obstacle_rect)
            elif obstacle_rect.bottom == 250:
                screen.blit(obstacle_2,obstacle_rect)
            else:
                screen.blit(obstacle_3,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rekt in obstacles:
            if player.colliderect(obstacle_rekt):
                return False
    return True


pygame.init()
screen = pygame.display.set_mode((800,400))
title = pygame.display.set_caption("Michal the Game")
clock = pygame.time.Clock()
icon = pygame.image.load('graphics/pixels.png')
pygame.display.set_icon(icon)


# texts
text_font = pygame.font.Font("font/Pixel.ttf",40)
over_font = pygame.font.Font("font/Pixel.ttf",60)
text = text_font.render("Michal the Game",False,'Black')
game_over = over_font.render("GAME OVER",False,"red")
game_over_rect = game_over.get_rect(center=(400,200))

# bg
sky = pygame.image.load("graphics/sky.png").convert()
ground = pygame.image.load("graphics/ground.png").convert()

#Player
player = pygame.image.load("graphics/wieczorek.png").convert_alpha()
player_rect = player.get_rect(bottomleft = (100,350))

#Main screen
charakter = pygame.image.load("graphics/wieczorek.png").convert_alpha()
charakter = pygame.transform.rotozoom(charakter,0,2)
charakter_rekt = charakter.get_rect(center = (400,200))


#obstacle nr 1
obstacle_1 = pygame.image.load("graphics/ue_fl.png").convert_alpha()
obs_3_rekt = obstacle_1.get_rect(bottomright = (randint(900,1200),350))
#obstacle nr 2
obstacle_2 = pygame.image.load("graphics/vat.png").convert_alpha()
obs_3_rekt = obstacle_2.get_rect(bottomright = (randint(900,1200),350))
#obstacle nr 3
obstacle_3 = pygame.image.load("graphics/green.png").convert_alpha()
obs_3_rekt = obstacle_3.get_rect(bottomright = (randint(900,1200),350))

lista = []
lista.append(obstacle_1)
lista.append(obstacle_2)
lista.append(obstacle_3)
obstacle_list = []

#obstacle timer
timer_obs = pygame.USEREVENT + 1
pygame.time.set_timer(timer_obs,1600)

# main values
gravity = 0
start_time = 0
GAMESPEED = 6
Game_active = True
Main_screen = True


#loop, zeby dzialalo
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        # if player_rect.bottom == 370: 
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Game_active == True and player_rect.bottom == 350:
                gravity = -19
            if event.key == pygame.K_SPACE and Game_active == False:
                Game_active = True
            if event.key == pygame.K_SPACE and Main_screen == True:
                Game_active = True
                Main_screen = False
        if event.type == timer_obs and Game_active == True:
            x = randint(0,3)
            if x == 0:
                obstacle_list.append(obstacle_1.get_rect(bottomright = (randint(900,1050),351)))
            elif x == 1:
                obstacle_list.append(obstacle_2.get_rect(bottomright = (randint(900,1050),250)))
            else:
                obstacle_list.append(obstacle_3.get_rect(bottomright = (randint(900,1050),350)))

    if Main_screen == True:
        screen.blit(charakter, charakter_rekt)


    else:
        if Game_active:
                # background
            screen.blit(sky,(0,0))
            screen.blit(ground,(0,350))
            screen.blit(text,(200,100))
            display_score()

            #player
            gravity +=1
            player_rect.y += gravity
            if player_rect.bottom > 350:
                player_rect.bottom =350
            screen.blit(player,player_rect)

            obstacle_list = movement(obstacle_list)
            Game_active = collisions(player_rect,obstacle_list)
            
        else:
            Game_active = False
            obstacle_list.clear()
            screen.fill((0,0,0))
            screen.blit(game_over,game_over_rect)
            start_time = int(pygame.time.get_ticks()/1000)


    pygame.display.update()
    clock.tick(60)
 
    
       