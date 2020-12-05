import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Dino run')
clock = pygame.time.Clock()
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)


import time
import random



display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (255,110,16)

car_width = 73
car_height = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dino run')
clock = pygame.time.Clock()

carImg = pygame.image.load('dino.png')
carImg = pygame.transform.scale(carImg, (car_width, car_height))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
        gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (15)
    y = (500 )

    x_change = 0
    y_change = 0
    thing_startx = 700
    thing_starty = 450
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0
 
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   y_change = -10
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_SPACE:
                   y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)


        
        thing_startx -= thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height or y <0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 
            thing_startx = 700
        
            dodged += 1
            thing_speed += 1
            thing_height -= (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()