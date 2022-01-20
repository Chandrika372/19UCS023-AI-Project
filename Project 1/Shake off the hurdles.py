# AI Project 1
# 19UCS023 Chandrika Acharjee
#Topic: Shake Off the Hurdles

import pygame
import time
import random
pygame.init()


width = 750
height = 700
obj_width = 80
Displaywindow = pygame.display.set_mode((width, height))

pygame.display.set_caption("Shake off the Hurdles!")  
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)
red = (255,127,127)
green = (144,238,144)

pause = False

dark_red = (255,0,0)
dark_green = (0,255,0)
hurdle_color = (92,64,51)
# Input Image
objImg = pygame.image.load(r"C:\Users\Chandrika PC\Downloads\racecar.png")


def things_escaped(count):
    font = pygame.font.SysFont(None,50)
    text = font.render("Hurdles Escaped: " +str(count), True, black)
    Displaywindow.blit(text,(0,0))


def hurdle_1(hurdlex, hurdley, hurdlew, hurdleh, color):
    pygame.draw.rect(Displaywindow, color, [hurdlex, hurdley, hurdlew, hurdleh])


def hurdle_2(hurdlex, hurdley, hurdlew, hurdleh, color):
    pygame.draw.rect(Displaywindow, color, [hurdlex, hurdley, hurdlew, hurdleh])


def obj(x, y):
    Displaywindow.blit(objImg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()


def display_msg(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    Displaywindow.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    loop()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(Displaywindow, ac, (x, y, w, h))
        if click[0]==1 and action is not None:
            action()

    else:
        pygame.draw.rect(Displaywindow,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    Displaywindow.blit(textSurf,textRect)


def collide():
    collide = True
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects("Game Over!",largeText)
    TextRect.center = ((width/2),(height/2))
    Displaywindow.blit(TextSurf,TextRect)

    while collide:
        for event in pygame.event.get():
            # print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

     

        button("AGAIN",150,450,100,50,green,dark_green,loop)
        button("LEAVE",550,450,100,50,red,dark_red,leave_game)

        pygame.display.update()
        clock.tick(15)


def leave_game():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def paused():
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("Pause!",largeText)
    TextRect.center = ((width/2),(height/2))
    Displaywindow.blit(TextSurf,TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,green,dark_green,unpause)
        button("LEAVE",550,450,100,50,red,dark_red,leave_game)
        pygame.display.update()
        clock.tick(15)


def game_commence():
    commence = True

    while commence:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Displaywindow.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',55)
        TextSurf, TextRect = text_objects("Shake off the Hurdles!",largeText)
        TextRect.center = ((width/2),(height/2))
        Displaywindow.blit(TextSurf, TextRect)

        button("START!",150,450,100,50,green,dark_green,loop)
        button("LEAVE",550,450,100,50,red,dark_red,leave_game)

        pygame.display.update()
        clock.tick(15)


def loop():
    global pause

    x =(width * 0.45)
    y =(height * 0.8)
    x_alter = 0
    # for thing 1
    hurdle_startx = random.randrange(0, width)
    hurdle_starty = -600
    hurdle_speed = 4
    hurdle_width = 100
    hurdle_height = 100

    # for thing 2
    hurdle_startx2 = random.randrange(0, width)
    hurdle_starty2 = -600
    hurdle_speed2 = 5
    hurdle_width2 = 100
    hurdle_height2 = 100

    escaped = 0
    leave_game = False

    while not leave_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_alter = -5
                if event.key == pygame.K_RIGHT:
                    x_alter = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_alter = 0

        x +=x_alter

        Displaywindow.fill(white)  

        # hurdle 1
        hurdle_1(hurdle_startx,hurdle_starty,hurdle_width,hurdle_height,hurdle_color)
        hurdle_starty+= hurdle_speed

        # hurdle 2
        hurdle_2(hurdle_startx2,hurdle_starty2,hurdle_width2,hurdle_height2,hurdle_color)
        hurdle_starty2+= hurdle_speed2
        obj(x, y)  
        things_escaped(escaped)
        
        if x >width - obj_width or x< 0: 
            collide()
        if hurdle_starty > height:
            hurdle_starty = 0 - hurdle_height
            hurdle_startx = random.randrange(0, width)
            escaped += 1
            hurdle_speed += 0.4
            hurdle_width += (escaped * 1.04)
        if hurdle_starty2 > height:
            hurdle_starty2 = 0 - hurdle_height2
            hurdle_startx2 = random.randrange(0, width)
            escaped += 1
            hurdle_speed2 += 0.4
            hurdle_width2 += (escaped * 1.02) 
        if y <hurdle_starty + hurdle_height:
            print ("y traverse")
            if hurdle_startx < x < hurdle_startx + hurdle_width or hurdle_startx < x + obj_width < hurdle_startx \
                    + hurdle_width:
                print( "x traverse")
                collide()
        if y <hurdle_starty2 + hurdle_height2:
            print ("y traverse")
            if hurdle_startx2 < x < hurdle_startx2 + hurdle_width2 or hurdle_startx2 < x + obj_width < hurdle_startx2 \
                    + hurdle_width2:
                print ("x traverse")
                collide()

        pygame.display.update()  
        clock.tick(90)  # fps

game_commence()
loop()
pygame.quit()
quit()
