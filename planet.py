import pygame as pg
pg.init()
score = 0
lives = 10
p_index = 0
info = pg.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
screen = pg.display.set_mode((WIDTH, HEIGHT))
bg = pg.image.load("bg1.png")
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))
planets = ["p2.png","p1.png"]
planet = pg.image.load(planets[p_index])
#crash = pg.image.load("crash.png")
bullet = pg.image.load("bullet.png")
spaceship = pg.image.load("spaceship.png")
font = pg.font.Font(None, 50)  # None = default font
planet_x = 450
bullet_y = 1700
move_dir = 'right'
keep_alive = True
fired = False
while keep_alive and (lives>0):
    screen.blit(bg,[0,0])
    screen.blit(planet,[planet_x,220])
    
    screen.blit(bullet,[450,bullet_y])
    screen.blit(spaceship,[450,1700])
    
    if(move_dir == 'right'):
        planet_x = planet_x + 10
        if (planet_x >= 1020):
            move_dir = 'left'
    else:
        planet_x = planet_x - 10
        if(planet_x<=0):
         
             move_dir = 'right'
    for event in pg.event.get():
        if(event.type == pg.MOUSEBUTTONDOWN):
            fired = True
    if(fired is True):
        bullet_y = bullet_y -10
        if(bullet_y ==220):
            fired = False
            #bullet_y = 1700
    if(fired is False):
        bullet_y = 1700    
    if((bullet_y>=220) and (bullet_y<=280) and (planet_x <= 510) and (planet_x>=390)):
        score = score + 1
        p_index += 1
        planet = pg.image.load(planets[p_index])
        fired = False
        
    elif((bullet_y>=220) and (bullet_y<=280) and ((planet_x > 510) or (planet_x<390))):
        lives = lives - 1
        fired = False
      
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text1 = font.render(f"lives: {lives}", True, (255,255,255))
    screen.blit(text1, (300,850))
    screen.blit(text, (300, 750))

    pg.display.update()