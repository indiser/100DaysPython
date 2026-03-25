import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_walk_1.png").convert_alpha()
        player_walk2=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_walk_2.png").convert_alpha()
        self.player_jump=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/jump.png").convert_alpha()
        self.player_index=0
        self.player_walk=[player_walk1,player_walk2]

        self.image=self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom =(80,300))
        self.gravity=0
        self.jump_sound=pygame.mixer.Sound("Professional Portfolio Project/Day87/audio/jump.mp3")
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity=-20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom=300

    def animation(self):
        if self.rect.bottom < 300:
            self.image=self.player_jump
        else:
            self.player_index+=0.1
            if self.player_index >= len(self.player_walk): self.player_index=0
            self.image=self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type=='fly':
            fly_1=pygame.image.load("Professional Portfolio Project/Day87/graphics/Fly/Fly1.png").convert_alpha()
            fly_2=pygame.image.load("Professional Portfolio Project/Day87/graphics/Fly/Fly2.png").convert_alpha()
            self.frames=[fly_1,fly_2]
            y_pos=210
        else:
            snail_1=pygame.image.load("Professional Portfolio Project/Day87/graphics/snail/snail1.png").convert_alpha()
            snail_2=pygame.image.load("Professional Portfolio Project/Day87/graphics/snail/snail2.png").convert_alpha()
            self.frames=[snail_1,snail_2]
            y_pos=300

        self.animation_index=0
        self.image=self.frames[self.animation_index]
        self.rect=self.image.get_rect(midbottom=(random.randint(900,1100),y_pos))

    def animation(self):
        self.animation_index+=0.1
        if self.animation_index >= len(self.frames): self.animation_index=0
        self.image=self.frames[int(self.animation_index)]

    def update(self):
        self.animation()
        self.rect.x-=6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time=pygame.time.get_ticks() // 1000 - start_time
    score_surface=test_font.render(f"Score: {current_time}",False,(0,0,0))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    # print(current_time)
    return current_time

def obs_movement(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -=5 
            if obs_rect.bottom==300:
                screen.blit(snail_surface,obs_rect)
            else:
                screen.blit(fly_surface,obs_rect)

        obs_list=[obs for obs in obs_list if obs.x > -100]
        return obs_list
    return []

def collisions(player,obs):
    if obs:
        for obs_rect in obs:
            if player.colliderect(obs_rect):
                return False
            
    return True

def collion_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    return True

def player_animation():
    global player_surf,player_index

    if player_rectangle.bottom < 300:
        player_surf=player_jump
    else:
        player_index+=0.1
        if player_index >= len(player_walk): player_index=0
        player_surf=player_walk[int(player_index)]





pygame.init()

game_sound=pygame.mixer.Sound("Professional Portfolio Project/Day87/audio/music.wav")


game_active=True
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("First Game")
# red_rectangle=pygame.draw.rect(screen, (255,0,0), (30, 30,30,30))
clock=pygame.time.Clock()

# test_surface=pygame.Surface((300,200))
# test_surface.fill('Red')

player=pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group=pygame.sprite.Group()

sky_surface=pygame.image.load("Professional Portfolio Project/Day87/graphics/Sky.png").convert()
ground_surface=pygame.image.load("Professional Portfolio Project/Day87/graphics/ground.png").convert()

test_font=pygame.font.Font("Professional Portfolio Project/Day87/font/Pixeltype.ttf",50)
text_color=(64,64,64)
text_surface=test_font.render("Game",False,text_color)

snail_frame_1=pygame.image.load("Professional Portfolio Project/Day87/graphics/snail/snail1.png").convert_alpha()
snail_frame_2=pygame.image.load("Professional Portfolio Project/Day87/graphics/snail/snail2.png").convert_alpha()
snail_index=0
snail_frames=[snail_frame_1,snail_frame_2]
snail_surface=snail_frames[snail_index]
snail_x_pos=600
# snail_rectangle=snail_surface.get_rect(midbottom=(600,300))

fly_frame_1=pygame.image.load("Professional Portfolio Project/Day87/graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2=pygame.image.load("Professional Portfolio Project/Day87/graphics/Fly/Fly2.png").convert_alpha()
fly_index=0
fly_frames=[fly_frame_1,fly_frame_2]
fly_surface=fly_frames[fly_index]

obs_rect_list=[]

# player_surface=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_walk_1.png").convert_alpha()
# player_rectangle=player_surface.get_rect(midbottom=(100,300))

score_text=test_font.render("Score",False,text_color)
score_rectangle=score_text.get_rect(center=(400,50))

player_gravity=0
running=True
x=0
start_time=0
score=0

player_stand=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_stand.png").convert_alpha()
# player_stand=pygame.transform.scale(player_stand,(200,400))
# player_stand=pygame.transform.scale2x(player_stand)
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rectangle=player_stand.get_rect(center=(400,200))

player_walk1=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_walk_1.png").convert_alpha()
player_walk2=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/player_walk_2.png").convert_alpha()
player_jump=pygame.image.load("Professional Portfolio Project/Day87/graphics/Player/jump.png").convert_alpha()
player_index=0
player_walk=[player_walk1,player_walk2]

player_surf=player_walk[player_index]
player_rectangle=player_surf.get_rect(midbottom=(100,300))


game_title=test_font.render("Pixel Game",False,(111,196,196))
game_title_rectangle=game_title.get_rect(center=(400,50))

restart_instuction=test_font.render("Press Space To Play",False,(111,196,196))
restart_instuction_rectangle=restart_instuction.get_rect(center=(400,350))

#Timer
obs_timer=pygame.USEREVENT+1
pygame.time.set_timer(obs_timer,1600)

snail_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_timer,500)

fly_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_timer,200)


game_sound.play(loops=-1)

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if game_active:
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)
            if event.type==pygame.MOUSEMOTION and player_rectangle.collidepoint(event.pos) and player_rectangle.bottom>=300:
                print("Mouse player Collsion")
                player_gravity=-20
            # if event.type==pygame.MOUSEBUTTONDOWN and player_rectangle.collidepoint(event.pos):
            #     print("Mouse player Collsion")
            #     player_gravity=-20

            # if event.type == pygame.KEYDOWN:
            #     print("Keydown")
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    if player_rectangle.bottom>=300:
                        player_gravity=-20
                        # print("jump")
            # if event.type == pygame.KEYUP:
            #     print("Keyup")
        else:
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    game_active=True
                    # snail_rectangle.left=600
                    start_time=pygame.time.get_ticks() // 1000
        
        
        
        # if game_active:
        #     if event.type==obs_timer:
        #         if random.randint(0,2):
        #             obs_rect_list.append(snail_surface.get_rect(bottomright=(random.randint(900,1100),300)))
        #         else:
        #             obs_rect_list.append(fly_surface.get_rect(bottomright=(random.randint(900,1100),210)))
        #     if event.type==snail_timer:
        #         if snail_index==0: snail_index=1
        #         else: snail_index=0
        #         snail_surface=snail_frames[snail_index]
        #     if event.type==fly_timer:
        #         if fly_index==0: fly_index=1
        #         else: fly_index=0
        #         fly_surface=fly_frames[fly_index]

        if game_active:
            if event.type==obs_timer:
                obstacle_group.add(Obstacle(random.choice(['fly','snail','snail'])))
                # if random.randint(0,2):
                #     obs_rect_list.append(snail_surface.get_rect(bottomright=(random.randint(900,1100),300)))
                # else:
                #     obs_rect_list.append(fly_surface.get_rect(bottomright=(random.randint(900,1100),210)))
            if event.type==snail_timer:
                if snail_index==0: snail_index=1
                else: snail_index=0
                snail_surface=snail_frames[snail_index]
            if event.type==fly_timer:
                if fly_index==0: fly_index=1
                else: fly_index=0
                fly_surface=fly_frames[fly_index]

                

    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # screen.blit(text_surface,(300,50))
        # snail_x_pos-=5
        # if snail_x_pos < -50:
        #     snail_x_pos=600
        # screen.blit(snail_surface,(snail_x_pos,280))
        # snail_rectangle.x-=5
        # if snail_rectangle.right <= 0: snail_rectangle.left = 800
        # screen.blit(snail_surface,snail_rectangle)
        # player_rectangle.left+=5

        # player_gravity+=1
        # player_rectangle.y+=player_gravity
        # if player_rectangle.bottom >= 300: player_rectangle.bottom=300
        # player_animation()
        # screen.blit(player_surf,player_rectangle)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # obbs_rect_list=obs_movement(obs_rect_list)

        # if(player_rectangle.colliderect(snail_rectangle)):
        #     print("collision")

        # mouse_pos=pygame.mouse.get_pos()
        # if(player_rectangle.collidepoint(mouse_pos)):
        #     # print("col")
        #     print(pygame.mouse.get_pressed())

        # pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
        # pygame.draw.rect(screen,'#c0e8ec',score_rectangle,10)
        # screen.blit(score_text,score_rectangle)

        # keys=pygame.key.get_pressed()
        # if(keys[pygame.K_SPACE]):
        #     print("jump")

        # pygame.draw.line(screen,'Gold',start_pos=(0,0),end_pos=(800,400),width=10)
        # pygame.draw.line(screen,'Gold',start_pos=(0,0),end_pos=pygame.mouse.get_pos(),width=10)
        # pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
        score=display_score()

        # if snail_rectangle.colliderect(player_rectangle):
        #     game_active=False

        # game_active=collisions(player_rectangle,obbs_rect_list)
        game_active=collion_sprite()
    else:
        screen.fill((94,129,162))
        screen.blit(game_title,game_title_rectangle)
        obs_rect_list.clear()
        player_rectangle.midbottom=(80,300)
        player_gravity=0
        final_score=test_font.render(f"Final Score: {score}",False,(111,196,196))
        final_score_rectangle=final_score.get_rect(center=(400,95))
        screen.blit(final_score,final_score_rectangle)
        screen.blit(player_stand,player_stand_rectangle)
        screen.blit(restart_instuction,restart_instuction_rectangle)

    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()