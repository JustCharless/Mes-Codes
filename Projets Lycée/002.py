import pygame
from pygame.locals import *
import time
import random
import os

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
seconde = 10

#Chargement et collage du fond
fond = pygame.image.load("Rain.png").convert()
fenetre.blit(fond, (0,0))
perso_y = 490
perso_x = 100

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = (perso_x, perso_y)
bonus = pygame.image.load("H20.png").convert_alpha()
bonus2 = pygame.image.load("bonus2.png").convert_alpha()
over = pygame.image.load("over.jpg").convert_alpha()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()
vel = 1

fenetre_largeur = 1602
fenetre_altitude = 800
Ha = 1340
Hb = 500
H2a = 750
H2b = 500

x = fenetre_largeur/2
y = fenetre_altitude/2
changement_de_x = 0
changement_de_y = 0
bonusX = (Ha,500)
bonusY = (Hb,500)
bonus2X = (H2a,500)
bonus2Y = (H2b,500)

Q = 2000
B = 2000


for i in range(seconde):
          print(str(seconde - i) + " temps restant ")
          time.sleep(1)

c = 10*vel
continuer = 2
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    if event.type == KEYDOWN:
           if event.key == K_DOWN:
            perso_y += c
            perso_x += 0
            position_perso = (perso_x,perso_y)
           elif event.key == K_UP:
            perso_y -= c
            perso_x += 0
            position_perso = (perso_x,perso_y)
           elif event.key == K_RIGHT:
            perso_x += c
            perso_y += 0
            position_perso = (perso_x,perso_y)
           elif event.key == K_LEFT:
            perso_x -= c
            perso_y += 0
            position_perso = (perso_x,perso_y)

    if perso_x == Ha and perso_y == Hb:
        print("youpi")
        bonusX = round(random.randrange(0, fenetre_largeur-perso_x)/10.0)*10.0
        bonusY = round(random.randrange(0, fenetre_altitude-perso_y)/10.0)*10.0
    if perso_x == H2a and perso_y == H2b:
        bonus2X = 2000
        bonus2Y = 2000
        c = 10/2
    if perso_x >= 1602 or perso_x < 0 or perso_y >= 800 or perso_y < 0:
        Q = 300
        B = 200
    if perso_x >= 1602 or perso_x < 0 or perso_y >= 800 or perso_y < 0:
        print("GAME OVER")
        fenetre.blit(over, (Q,B))
    if perso_y < 200 and perso_x > 495:
        print("hors zone")
        perso_y += 10
    if perso_y > 735 and 467 < perso_x < 760:
        print("hors zone")
        perso_y -= 10
    if  perso_x > 745 and 680<perso_y <700:
        perso_x -= 10
    if perso_y > 500 and 0 < perso_x < 200:
        print("hors zone")
        perso_y -= 10
    if 270< perso_y< 300 and perso_x > 950:
        perso_x -= 10
    if 0<perso_x<495 and perso_y < 460:
        print("commence pas hors zone")
        perso_y += 10
    if perso_x > 1570 and perso_y > 650:
        print("VICTOIRE")


    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    fenetre.blit(bonus, [bonusX, bonusY])
    fenetre.blit(bonus2, [bonus2X, bonus2Y])
    fenetre.blit(over, (Q,B))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
