import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bird')

#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('FlappyBird_Game/bg.png')
ground_img= pygame.image.load('FlappyBird_Game/ground.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        

run= True
while run:
    
    clock.tick(fps)
    
    #draw background 
    screen.blit(bg,(0,0))
    
    #draw and scroll the ground 
    screen.blit(ground_img,(ground_scroll,786))
    ground_scroll -= scroll_speed
    if abs(ground_scroll)>35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
    pygame.display.update()
    
pygame.quit()        