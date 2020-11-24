import pygame
pygame.init()
global black, white
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
display_width = 1200
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

def draw_line(surface,color,start_pos,end_pos,width):
    pygame.draw.line(surface,color,start_pos,end_pos,width)

def game_loop():
    maze = "\
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+n\
|        |     |        |           |     |     |n\
+  +--+  +  +  +--+  +  +  +  +--+--+  +  +--+  +n\
|  |     |  |        |  |  |           |  |     |n\
+  +--+  +  +  +--+--+  +  +--+--+--+--+  +  +  +n\
|     |     |  |     |  |  |        |     |  |  |n\
+--+  +--+--+--+  +  +--+  +  +--+--+--+--+  +  +n\
|     |           |        |                 |  |n\
+  +  +  +--+--+--+--+--+--+--+--+--+--+--+  +--+n\
|  |  |  |        |                       |     |n\
+  +--+  +  +--+  +  +--+--+--+--+--+--+  +  +  +n\
|        |  |        |        |        |  |  |  |n\
+  +--+--+  +--+--+--+  +--+  +  +  +--+  +  +  +n\
|        |           |  |     |  |        |  |  |n\
+--+--+  +--+--+--+  +  +  +--+  +--+--+--+--+  +n\
|                    |  |                       |n\
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+"

    gameExit = False

    WALL_LENGTH = 20
    x=y=x2=y2=START=5

    gameDisplay.fill(white)
    linecount = 0
    for i in maze:
        if i == "-":
            x2+=WALL_LENGTH
            draw_line(gameDisplay,black,(x,y),(x2,y2),5)
            x+=WALL_LENGTH
        elif i == "+":
            x2+=WALL_LENGTH
            draw_line(gameDisplay,red,(x,y),(x2,y2),5)
            x+=WALL_LENGTH
        elif i == "n":
            linecount+=1
            if(linecount % 2 == 0):
                y+=WALL_LENGTH*2
                y2=y
            x=START
            x2=START
        elif i == "|":
            y2-=WALL_LENGTH*2
            draw_line(gameDisplay,black,(x,y),(x2,y2),5)
            x+=WALL_LENGTH
            x2=x
            y2=y
        elif i == " ":
            x+=WALL_LENGTH
            x2=x

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameExit = True

        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()
