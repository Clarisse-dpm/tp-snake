from random import randint
import pygame as pg

def draw_board():
    screen.fill((0,0,0))
    x,y=0,0
    for i in range(30): 
        for j in range(15):
            rect = pg.Rect(x,y,20,20)
            pg.draw.rect(screen, (255,255,255),rect)
            y=y+40
        x=x+20
        if i%2 ==0 :
            y=20
        else : 
            y=0
snake = [(10, 15),(11, 15),(12, 15)]

def draw_snake(snake):
    for i in range(len(snake)) :
        x=snake[i][0]*20
        y=snake[i][1]*20
        rect = pg.Rect(x,y,20,20)
        pg.draw.rect(screen, (255,0,0),rect)


pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
continuer = True
while continuer :
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT : 
            continuer = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                continuer = False
    draw_board()
    draw_snake(snake)
    pg.display.update()
pg.quit()



#sur chaque image: 15*15 = 225 carrés