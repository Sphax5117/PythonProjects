import pygame
import time
import random

from pygame.constants import KEYDOWN

pygame.init() #l'init ( le démarrer )

dis_width = 400
dis_height  = 500

dis = pygame.display.set_mode((dis_width, dis_height)) #définir la définition de l'app

white = (255,255,255) 
blue=(0,0,255)
red=(255,0,0)
green = (0,255,0)



pygame.display.update() #Faire une update de l'app
pygame.display.set_caption("Snake game by Sphax") # Titre de l'app

clock = pygame.time.Clock()

game_over = False
x1 = dis_width / 2
y1 = dis_height / 2

x1_change = 0
y1_change = 0
snake_block=10

snake_List = []
Length_of_snake = 1



snake_speed=10

font_style = pygame.font.SysFont(None, 50) 

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
def message(msg,color):  #Défini ce qu'est la variable pour afficher un message 
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop(): #On créé une fonction 
    game_over = False
    game_close = False

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  #On créé la position de la pomme au hasard
foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  

while not game_over: # Tant que game_over n'est pas sur true, on print tout les events ( souris etc ..)
    
    game_close = False


    while game_close == True:
        dis.fill(blue)
        message("You lost ! Press C-Play again or Q-Quit !", red)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:          
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #condition pour fermer l'app ( le quit en majuscule est important )
            game_over = True
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0 
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  #Ferme le jeu si le joueur dépasse les limites
        game_close = True
        

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, green, [x1,y1,20,20]) #desssing un rectangle sur le display, bleu aux coordonées 200x 150y, de 10 px sur 10px
    pygame.draw.rect(dis, red, [foodx,foody, 20,20])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

message("You Lost", red)
pygame.display.update()
time.sleep(2)



pygame.quit()
quit()
