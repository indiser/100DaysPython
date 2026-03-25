import pygame
import random

# constants
display_size=(600,800)
paddle_place=(300,760)
ball_place=(300,736)
purpul_edge_color=(255, 0, 255)
ball_gravity=0

BOUNDARY_MIN_X = 50
BOUNDARY_MIN_Y = 50
BOUNDARY_MAX_X = 250
BOUNDARY_MAX_Y = 300

pygame.init()

# Music
bg_music=pygame.mixer.Sound("Professional Portfolio Project/Day87/breakout_audio/Pixel_Pounce.mp3")
ball_hitting_bricks_sound=pygame.mixer.Sound("Professional Portfolio Project/Day87/breakout_audio/15-xylophone-chord-c-01-snd.mp3")
ball_hitting_paddle=pygame.mixer.Sound("Professional Portfolio Project/Day87/breakout_audio/18-xylophone-chord-c-04-snd.mp3")

game_active=True
game_over=win=False
clock=pygame.time.Clock()

screen=pygame.display.set_mode(display_size)
pygame.display.set_caption("Breakout")

# Paddle
paddle_surface=pygame.image.load("Professional Portfolio Project/Day87/Paddles/Style A/Paddle_A_Blue_128x28.png").convert_alpha()
paddle_rect=paddle_surface.get_rect(midbottom=paddle_place)
paddle_surface.set_colorkey(purpul_edge_color)

# ball
ball_surface=pygame.image.load("Professional Portfolio Project/Day87/Balls/Shiny/Ball_Blue_Shiny-16x16.png").convert_alpha()
ball_rect=ball_surface.get_rect(midbottom=ball_place)
ball_surface.set_colorkey(purpul_edge_color)

ball_speed_x = 4
ball_speed_y = -4


# Bricks
blue_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Blue-64x32.png").convert_alpha()

brick_width=blue_brick_surface.get_width()
brick_height=blue_brick_surface.get_height()

safe_max_x = BOUNDARY_MAX_X - brick_width
safe_max_y = BOUNDARY_MAX_Y - brick_height

red_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Red-64x32.png").convert_alpha()
green_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Green-64x32.png").convert_alpha()
purple_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Purple-64x32.png").convert_alpha()
orange_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Orange-64x32.png").convert_alpha()
yellow_brick_surface=pygame.image.load("Professional Portfolio Project/Day87/Bricks/Colored/Colored_Yellow-64x32.png").convert_alpha()

bricks = []
rows = 10
cols = 8
spacing = 0
brick_colors=[blue_brick_surface,red_brick_surface,green_brick_surface,orange_brick_surface,purple_brick_surface]
for row in range(rows):
    for col in range(cols):
        x = BOUNDARY_MIN_X + col * (brick_width + spacing)
        y = BOUNDARY_MIN_Y + row * (brick_height + spacing)

        brick_rect = pygame.Rect(x, y, brick_width, brick_height)
        brick_surface=random.choice(brick_colors)
        bricks.append((brick_surface,brick_rect))



# Text Font

text_font=pygame.font.SysFont("ubuntu mono",60)

text_color=((255,255,255))
game_over_text=text_font.render("Game Over",False,text_color)
game_over_rect=game_over_text.get_rect(center=(300,400))

winner_text=text_font.render("Victory",False,text_color)
winner_rect=winner_text.get_rect(center=(300,400))



running=True

bg_music.play(loops=-1)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active==False:
                ball_speed_x=4
                ball_speed_y=-4
                game_active=True

    
    if game_active:
        mouse_x = pygame.mouse.get_pos()[0]
        paddle_rect.centerx = mouse_x
        
        if paddle_rect.left < 0:
            paddle_rect.left = 0
        if paddle_rect.right > display_size[0]:
            paddle_rect.right = display_size[0]
        

        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y


        if ball_rect.left <= 0 or ball_rect.right >= display_size[0]:
            ball_speed_x *= -1
        
        if ball_rect.top <= 0:
            ball_speed_y *= -1
        
        for i, (brick_surface, brick_rect) in enumerate(bricks):
            if ball_rect.colliderect(brick_rect):
                ball_hitting_bricks_sound.play()
                ball_speed_y *= -1
                bricks.pop(i)
                break

        # Bounce off paddle
        if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
            ball_hitting_paddle.play()
            ball_speed_y *= -1

        if ball_rect.top > display_size[1]:
            game_over=True
            game_active=False

        if len(bricks)==0:
            win=True
            game_active=False


        screen.fill((0, 0, 0))
        screen.blit(paddle_surface,paddle_rect)
        screen.blit(ball_surface,ball_rect)

        for brick_surface,brick_rect in bricks:
            screen.blit(brick_surface,brick_rect)

        
    else:
        screen.fill((0,0,0))

        if game_over:
            screen.blit(game_over_text,game_over_rect)
        if win:
            screen.blit(winner_text,winner_rect)


    pygame.display.update()
    clock.tick(60)

pygame.quit()