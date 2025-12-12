import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
menu = True
game = False
clock = pygame.time.Clock()

delta_time = 0.1

mpos = pygame.mouse.get_pos()

font_help = pygame.font.SysFont('Times New Roman', 24)

font = pygame.font.SysFont('Times New Roman', 48)


while running:



    mpos = pygame.mouse.get_pos()
    if menu:
        screen.fill((0, 0, 0))

        text = font.render('BreakOut', True, (255, 255, 255))
        screen.blit(text, (300, 50))

        p_target = pygame.Rect(320, 150, 150, 50)
        p_collision = p_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), p_target)
        p_text = font.render('Play', True, (0, 0, 0))
        screen.blit(p_text, (350, 145))

        h_target = pygame.Rect(320, 250, 150, 50)
        h_collision = h_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), h_target)
        h_text = font.render('Help', True, (0, 0, 0))
        screen.blit(h_text, (350, 245))

        e_target = pygame.Rect(320, 350, 150, 50)
        e_collision = e_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), e_target)
        e_text = font.render('Exit', True, (0, 0, 0))
        screen.blit(e_text, (350, 345))

        b_target = pygame.Rect(50, 50, 150, 50)
        b_collision = b_target.collidepoint(mpos)

    elif menu == False & game == True:
        pass
    else:

        screen.fill((0, 0, 0))

        text = font.render('help', True, (255, 255, 255))
        screen.blit(text, (350, 50))

        text_move = font_help.render('A and D to move left and right', True, (255, 255, 255))
        screen.blit(text_move, (100, 150))

        text_fire = font_help.render('W to fire the ball', True, (255, 255, 255))
        screen.blit(text_fire, (100, 200))

        text_lives = font_help.render('lives will be shown in the bottom left hand side', True, (255, 255, 255))
        screen.blit(text_lives, (100, 250))

        text_st = font_help.render('score and high score are at the top', True, (255, 255, 255))
        screen.blit(text_st, (100, 300))

        b_target = pygame.Rect(50, 50, 150, 50)
        b_collision = b_target.collidepoint(mpos)
        pygame.draw.rect(screen, (255, 255, 255), b_target)
        e_text = font.render('back', True, (0, 0, 0))
        screen.blit(e_text, (80, 45))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if e_collision:
            if pygame.mouse.get_pressed()[0]:
                running = False
        if h_collision:
            if pygame.mouse.get_pressed()[0]:
               menu = False
               game = False

        if b_collision:
            if pygame.mouse.get_pressed()[0]:
                menu = True

        if p_collision:
            if pygame.mouse.get_pressed()[0]:
                menu = False
                game = True


    pygame.display.flip()

    delta_time = clock.tick(60)

    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()