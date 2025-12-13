#import statements

import os

import pygame
import csv

#set up for the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#sound effects
sound = pygame.mixer.Sound('glass-bottle-shatter-84593.mp3')
pygame.mixer.music.load('joyful-carnival-trumpet-232017.mp3')

#menu picker varubles
menu = True
game = False
#score
score = 0

#ball varubles
BALL_SPEED = 5
ball_dx = BALL_SPEED
ball_dy = -BALL_SPEED
ball_pos = pygame.Vector2(400, 500)

#checks if high score exists
high_exsist = os.path.isfile("high.csv")


#the images
ball_img = pygame.image.load('New Piskel (3).png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (32, 32))

paddle_img = pygame.image.load('New Piskel (2).png').convert_alpha()
paddle_img = pygame.transform.scale(paddle_img, (128, 32))

wall_img = pygame.image.load('New Piskel (4).png').convert_alpha()
wall_img = pygame.transform.scale(wall_img, (64, 32))

#fonts
font_help = pygame.font.SysFont('Times New Roman', 36)

font = pygame.font.SysFont('Times New Roman', 48)

#if high don't exsist it is created
with open('high.csv', "a", newline="") as score_A:
    writer = csv.writer(score_A)
    if not high_exsist:
        writer.writerow(["high score = ", "0"])

#makes the walls posable for later
walls = []

def create_walls():
    walls = []
    for row in range(3):
        for col in range(8):
            rect = wall_img.get_rect(topleft=(100 + col * 70, 80 + row * 40))
            walls.append(rect)
    return walls

walls = create_walls()

#resests the game and saves highscore
def reset_game():
    global score, ball_pos, ball_dx, ball_dy, game, menu, walls
    with open("high.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            high_score = int(row[1])
    if score > high_score:
        with open("high.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["high score =", score])
    pygame.mixer.music.stop()
    score = 0
    ball_pos = pygame.Vector2(400, 500)
    ball_dx = BALL_SPEED
    ball_dy = -BALL_SPEED
    game = False
    menu = True

#the loop that makes the game run
running = True

while running:

    #makes the screen black and gets mouse position
    screen.fill((0, 0, 0))

    mpos = pygame.mouse.get_pos()

    #the main menu section
    if menu:

        screen.fill((0, 0, 0))
        #title
        text = font.render('BreakOut', True, (255, 255, 255))
        screen.blit(text, (300, 50))

        #makes the play buton
        p_target = pygame.Rect(320, 150, 150, 50)
        p_collision = p_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), p_target)
        p_text = font.render('Play', True, (0, 0, 0))
        screen.blit(p_text, (350, 145))

        #makes the help buton
        h_target = pygame.Rect(320, 250, 150, 50)
        h_collision = h_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), h_target)
        h_text = font.render('Help', True, (0, 0, 0))
        screen.blit(h_text, (350, 245))

        #makes the exit buton
        e_target = pygame.Rect(320, 350, 150, 50)
        e_collision = e_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), e_target)
        e_text = font.render('Exit', True, (0, 0, 0))
        screen.blit(e_text, (350, 345))

        #back button stuff this is important and will break the game if removed
        b_target = pygame.Rect(50, 50, 150, 50)
        b_collision = b_target.collidepoint(mpos)

    #the game
    elif game:

        #plays music
        pygame.mixer.music.play(-1)
        #creates the paddle object
        paddle_rect = paddle_img.get_rect(midtop=(mpos[0], 550))
        screen.blit(paddle_img, paddle_rect)

        #sets the position
        ball_pos.x += ball_dx
        ball_pos.y += ball_dy
        ball_rect = ball_img.get_rect(center=ball_pos)

        #makes the walls colidable
        for wall in walls[:]:
            if ball_rect.colliderect(wall):
                walls.remove(wall)
                ball_dy *= -1
                score += 10
                sound.play()
                break

        #ball colides with paddle
        if ball_rect.colliderect(paddle_rect):
            ball_dy *= -1

        #ball's interactions with walls
        if ball_rect.left <= 0 or ball_rect.right >= 800:
            ball_dx *= -1
        if ball_rect.top <= 0:
            ball_dy *= -1
        if ball_rect.bottom >= 600:
            reset_game()

        #makes ball
        screen.blit(ball_img, ball_rect)

        #makes the walls
        for wall in walls:
            screen.blit(wall_img, wall)

        #resets walls
        if len(walls) == 0:
            walls = create_walls()
            ball_pos = pygame.Vector2(400, 500)
            ball_dx = BALL_SPEED
            ball_dy = -BALL_SPEED

        #show score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    #makes the help menu
    else:

        screen.fill((0, 0, 0))

        #title section
        text = font.render('help', True, (255, 255, 255))
        screen.blit(text, (350, 50))
        #tells you to move
        text_move = font_help.render('move mouse left and right to move left and right', True, (255, 255, 255))
        screen.blit(text_move, (100, 150))

        #tells you where the score is
        text_fire = font_help.render('score is at the top', True, (255, 255, 255))
        screen.blit(text_fire, (100, 200))

        #goal of the game
        text_st = font_help.render('get the most amount of points to win the game', True, (255, 255, 255))
        screen.blit(text_st, (100, 250))


        #back buton
        b_target = pygame.Rect(50, 50, 150, 50)
        b_collision = b_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), b_target)
        e_text = font.render('back', True, (0, 0, 0))
        screen.blit(e_text, (80, 45))
    #the actions for the game
    for event in pygame.event.get():
        #makes x in the corner work
        if event.type == pygame.QUIT:
            running = False

        # makes quit buton work
        if e_collision:
            if pygame.mouse.get_pressed()[0]:
                running = False
        #makes the help buton work
        if h_collision:
            if pygame.mouse.get_pressed()[0]:
               menu = False
               game = False

        #makes the back buton work
        if b_collision:
            if pygame.mouse.get_pressed()[0]:
                menu = True

        #makes the play buton work
        if p_collision:
            if pygame.mouse.get_pressed()[0]:
                menu = False
                game = True
    #renderer
    pygame.display.flip()
    clock.tick(60)
#exits the game
pygame.quit()