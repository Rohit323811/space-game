import pygame as pg
pg.init()

# ---------------- VARIABLES ----------------
score = 0
planet_x = 450
bullet_y = 1700
move_dir = 'right'
fired = False
lives = 10
game_state = "menu"

info = pg.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

# ---------------- LOAD ----------------
planet = pg.image.load("static/p1.png")
bullet = pg.image.load("static/bullet.png")
spaceship = pg.image.load("static/spaceship.png")
bg = pg.image.load("static/bg1.png")
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))
bg1 = pg.image.load("static/start_bg.jpg")
bg1 = pg.transform.scale(bg1, (WIDTH, HEIGHT))
bg2 = pg.image.load("static/bg2.jpg")
bg2 = pg.transform.scale(bg2,(WIDTH, HEIGHT))
play_btn = pg.image.load("static/play_btn.png")
restart_btn = pg.image.load("static/restart.png")
exit_btn = pg.image.load("static/exit.png")
button_restart = restart_btn.get_rect(topleft=(260,800))
button_exit = exit_btn.get_rect(topleft=(260,1300))
button_rect = play_btn.get_rect(topleft=(260,1700))
font_big = pg.font.Font(None,200)
font_mid = pg.font.Font(None,100)
font_small = pg.font.Font(None,50)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

keep_alive = True

# ---------------- MAIN LOOP ----------------
while keep_alive:
    clock.tick(60)  # smooth FPS

    # -------- EVENTS --------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_alive = False

        if event.type == pg.MOUSEBUTTONDOWN:

            # MENU CLICK
            if game_state == "menu":
                if button_rect.collidepoint(event.pos):
                    game_state = "play"

            # FIRE BULLET
            elif game_state == "play":
                if not fired:
                    fired = True

    # -------- MENU --------
    if game_state == "menu":
        screen.blit(bg1,[0,0])
        screen.blit(play_btn,[200,1750])

        text1 = font_big.render("Space Game",True,(0,0,0))
        rect = text1.get_rect(center=(500, 500))

        text2 = font_mid.render("Press button to play",True,(0,0,0))
        rect1 = text2.get_rect(center=(500, 1700))

        screen.blit(text1, rect)
        screen.blit(text2, rect1)

    # -------- GAME --------
    elif game_state == "play":

        screen.blit(bg,[0,0])
        screen.blit(planet,[planet_x,220])
        screen.blit(bullet,[450,bullet_y])
        screen.blit(spaceship,[450,1700])

        # -------- PLANET MOVE --------
        if move_dir == 'right':
            planet_x += 10
            if planet_x >= 1020:
                move_dir = 'left'
        else:
            planet_x -= 10
            if planet_x <= 0:
                move_dir = 'right'

        # -------- BULLET MOVE --------
        if fired:
            bullet_y -= 10

        # -------- RESET BULLET --------
        if bullet_y <= 220:
            fired = False
            bullet_y = 1700

        # -------- COLLISION --------
        if (220 <= bullet_y <= 280) and (390 <= planet_x <= 510):
            score += 1
            fired = False
            bullet_y = 1700

        elif (220 <= bullet_y <= 280) and (planet_x > 510 or planet_x < 390):
            lives -= 1
            fired = False
            bullet_y = 1700

        # -------- TEXT --------
        text_score = font_small.render(f"Score: {score}", True, (255,255,255))
        text_lives = font_small.render(f"Lives: {lives}", True, (255,255,255))

        screen.blit(text_score, (300, 750))
        screen.blit(text_lives, (300, 850))

        # -------- GAME OVER --------
        if lives <= 0:
            game_state = "exit_screen"
            lives = 10
            score = 0
    elif (game_state == "exit_screen"):
        screen.blit(bg2,[0,0])
        screen.blit(restart_btn,[260,800])
        screen.blit(exit_btn,[260,1300])
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    game_state = "play"
                elif button_exit.collidepoint(event.pos):
                    keep_alive = False    
                
    # -------- UPDATE --------
    pg.display.update()

pg.quit()