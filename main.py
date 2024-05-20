import pygame
import random
import sys
import asyncio

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
GAMESPEED = 17
pygame.display.set_caption("For Vera")
pygame.display.set_icon(pygame.image.load("images/icon.png"))
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



RUN = [pygame.image.load("images/Run (1).png"),
       pygame.image.load("images/Run (2).png"),
       pygame.image.load("images/Run (3).png"),
       pygame.image.load("images/Run (4).png"),
       pygame.image.load("images/Run (5).png"),
       pygame.image.load("images/Run (6).png"),
       pygame.image.load("images/Run (7).png"),
       pygame.image.load("images/Run (8).png"),
       pygame.image.load("images/Run (9).png"),
       pygame.image.load("images/Run (10).png"),
       pygame.image.load("images/Run (11).png"),
       pygame.image.load("images/Run (12).png"),
       pygame.image.load("images/Run (13).png"),
       pygame.image.load("images/Run (14).png"),
       pygame.image.load("images/Run (15).png"),
       pygame.image.load("images/Run (16).png"),
       pygame.image.load("images/Run (17).png"),
       pygame.image.load("images/Run (18).png"),
       pygame.image.load("images/Run (19).png"),
       pygame.image.load("images/Run (20).png")
       ]
JUMP = [pygame.image.load("images/Jump (1).png"),
        pygame.image.load("images/Jump (2).png"),
        pygame.image.load("images/Jump (3).png"),
        pygame.image.load("images/Jump (4).png"),
        pygame.image.load("images/Jump (5).png"),
        pygame.image.load("images/Jump (6).png"),
        pygame.image.load("images/Jump (7).png"),
        pygame.image.load("images/Jump (8).png"),
        pygame.image.load("images/Jump (9).png"),
        pygame.image.load("images/Jump (10).png"),
        pygame.image.load("images/Jump (11).png"),
        pygame.image.load("images/Jump (12).png"),
        pygame.image.load("images/Jump (13).png"),
        pygame.image.load("images/Jump (14).png"),
        pygame.image.load("images/Jump (15).png"),
        pygame.image.load("images/Jump (16).png"),
        pygame.image.load("images/Jump (17).png"),
        pygame.image.load("images/Jump (18).png"),
        pygame.image.load("images/Jump (19).png"),
        pygame.image.load("images/Jump (20).png"),
        pygame.image.load("images/Jump (21).png"),
        pygame.image.load("images/Jump (22).png"),
        pygame.image.load("images/Jump (23).png"),
        pygame.image.load("images/Jump (24).png"),
        pygame.image.load("images/Jump (25).png"),
        pygame.image.load("images/Jump (26).png"),
        pygame.image.load("images/Jump (27).png"),
        pygame.image.load("images/Jump (28).png"),
        pygame.image.load("images/Jump (29).png"),
        pygame.image.load("images/Jump (30).png")
        ]

BACKGROUND = pygame.image.load("images/BG.png")
BG = pygame.transform.scale(BACKGROUND, (1200,700))

SCENE_RAW = [pygame.image.load("images/start.png"),
         pygame.image.load("images/lose.png"),
         pygame.image.load("images/end.png"),
         pygame.image.load("images/awww.png")
         ]
SCENE = [pygame.transform.scale(SCENE_RAW[0], (1200,700)),
         pygame.transform.scale(SCENE_RAW[1], (1200,700)),
         pygame.transform.scale(SCENE_RAW[2], (1200,700)),
         pygame.transform.scale(SCENE_RAW[3], (1200,700))
         ]


OBSTACLES = [pygame.image.load("images/H.png"),
             pygame.image.load("images/A1.png"),
             pygame.image.load("images/P1.png"),
             pygame.image.load("images/P2.png"),
             pygame.image.load("images/Y1.png"),
             pygame.image.load("images/V.png"),
             pygame.image.load("images/E.png"),
             pygame.image.load("images/R.png"),
             pygame.image.load("images/A2.png"),
             pygame.image.load("images/D.png"),
             pygame.image.load("images/A3.png"),
             pygame.image.load("images/Y2.png"),
             pygame.image.load("images/cake.png")
             
             ]

OBSTACLES_AD = [pygame.transform.scale(OBSTACLES[0], (160,220)),
                pygame.transform.scale(OBSTACLES[1], (180,220)),
                pygame.transform.scale(OBSTACLES[2], (180,220)),
                pygame.transform.scale(OBSTACLES[3], (180,220)),
                pygame.transform.scale(OBSTACLES[4], (180,220)),
                pygame.transform.scale(OBSTACLES[5], (180,220)),
                pygame.transform.scale(OBSTACLES[6], (180,220)),
                pygame.transform.scale(OBSTACLES[7], (180,220)),
                pygame.transform.scale(OBSTACLES[8], (180,220)),
                pygame.transform.scale(OBSTACLES[9], (180,220)),
                pygame.transform.scale(OBSTACLES[10], (180,200)),
                pygame.transform.scale(OBSTACLES[11], (180,200)),
                pygame.image.load("images/cake.png")
                ]
BUTTON = [pygame.image.load("images/easy.png"),
              pygame.image.load("images/again.png")]


class girl:
    X_POS = 80
    Y_POS = 400
    JUMP_V = 25
    IMAGE_X = 192.5
    IMAGE_Y = 224.5
    
    def __init__(self):
        self.run_img = RUN
        self.jump_img = JUMP
        
        self.girl_run = True
        self.girl_jump = False
        
        self.step_index_RUN = 0
        self.step_index_JUMP = 0
        self.image_size = (self.IMAGE_X, self.IMAGE_Y)
        self.image = pygame.transform.scale(self.run_img[0], self.image_size) 
        self.girl_rect = self.image.get_rect()
        self.jump_v = self.JUMP_V
        self.girl_rect.x = self.X_POS
        self.girl_rect.y = self.Y_POS
            
    def running(self):
        self.image = pygame.transform.scale(self.run_img[self.step_index_RUN], self.image_size) 
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_POS
        self.girl_rect.y = self.Y_POS 
        
        if self.step_index_RUN >= 19:
            self.step_index_RUN = 0
        
        self.step_index_RUN += 1 
        
    def jumping(self):  
        self.image = pygame.transform.scale(self.jump_img[self.step_index_JUMP], self.image_size) 
        
        self.girl_rect.y -= self.jump_v
        self.jump_v -= 1
        self.step_index_JUMP +=1
        
        if self.step_index_JUMP >=29:
            self.step_index_JUMP = 29
        
        if self.girl_rect.y >= self.Y_POS:
            self.step_index_JUMP = 0
            self.girl_jump = False
            self.girl_run = True
            self.jump_v = self.JUMP_V


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.girl_rect.x, self.girl_rect.y))
        
    def update(self, userinput):
        if self.girl_run:
            self.running()
            
        if self.girl_jump:
            self.jumping()
            
        if userinput[pygame.K_SPACE] and not self.girl_jump:
            self.girl_jump = True
            self.girl_run = False
    

class obstacles:
    
    def __init__(self, index, y_pos):
        self.obstacle_image = OBSTACLES_AD[index]
        self.obstacle_rect = self.obstacle_image.get_rect()
        self.obstacle_rect.x = SCREEN_WIDTH*(index + 1) + random.randint(SCREEN_WIDTH*0.65, SCREEN_WIDTH)
        self.obstacle_rect.y = y_pos
        self.POS_X0 = self.obstacle_rect.x
        
    def update(self):
        self.obstacle_rect.x -= game_speed
        
        
    def draw(self, SCREEN):
        SCREEN.blit(self.obstacle_image, (self.obstacle_rect.x, self.obstacle_rect.y))

class button:
    
    def __init__(self, index, button_pos, button_size):
        self.button_image = pygame.transform.scale(BUTTON[index], button_size) 
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = button_pos[0]
        self.button_rect.y = button_pos[1]
    
    def draw(self, SCREEN):
        SCREEN.blit(self.button_image, (self.button_rect.x, self.button_rect.y))
           
def game():
    global game_speed, BG_X_POS, BG_Y_POS, OBS, run, clock, player, current_state, current_mode, STATE

    run = True
    clock = pygame.time.Clock()
    player = girl()
    OBS = [obstacles(0,400), obstacles(1,400), obstacles(2,400), obstacles(3, 400), obstacles(4, 420), obstacles(5, 400), obstacles(6, 400), obstacles(7, 400), obstacles(8, 400), obstacles(9, 400),obstacles(10, 420), obstacles(11, 420), obstacles(12, 200)]
    game_speed = GAMESPEED
    BG_X_POS = 0
    BG_Y_POS = 0
    button_again_pos = (900, 600)
    button_easy_size = (650, 100)
    button_again_size = (250, 48)
    button_easy_pos = (275, 400)
    button_easy = button(0, button_easy_pos, button_easy_size)
    button_again = button(1, button_again_pos, button_again_size)
    current_state = "START"
    current_mode = "NORMAL"
    STATE = ["START", "RUNNING", "LOSE", "END"]
    MODE = ["NORMAL", "EASY"]
    colide = False
    
    
    def background():
        global game_speed, BG_X_POS, BG_Y_POS, OBS, run
        BG_WIDTH = BG.get_width()
        SCREEN.blit(BG, (BG_X_POS, BG_Y_POS))
        SCREEN.blit(BG, (BG_WIDTH + BG_X_POS, BG_Y_POS))
        
        if BG_X_POS <= -BG_WIDTH:
            BG_X_POS = 0
        BG_X_POS -=game_speed
    
    def obs_refresh():  
        for obs in OBS:
            obs.obstacle_rect.x = obs.POS_X0
        
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and current_state == STATE[0]:
                current_state = STATE[1]
        
        SCREEN.fill((0, 0, 0))
        userinput = pygame.key.get_pressed()

#state check

        #START
        if current_state == STATE[0]:
            SCREEN.blit(SCENE[0], (0,0))
            pygame.display.update()
            
        #RUNNING          
        if current_state == STATE[1]:
            background()
            player.draw(SCREEN)
            
            if colide == False:
                player.update(userinput)
            
            for obs in OBS:
                
                if colide == False:
                    obs.draw(SCREEN)
                    
                obs.update()
                
                #END
                if player.girl_rect.colliderect(OBS[12].obstacle_rect):
                    current_state = STATE[3] 
                        
                elif player.girl_rect.colliderect(obs.obstacle_rect):
                    
                    
                    #NORMAL-->LOSE
                    if current_mode == MODE[0]: 
                        colide = True
                        game_speed = 0
                        SCREEN.blit(SCENE[1], (0,0))
                        button_easy.draw(SCREEN)
                        button_again.draw(SCREEN)
                        
                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if button_again.button_rect.collidepoint(pygame.mouse.get_pos()):
                                    obs_refresh()
                                    game_speed = GAMESPEED
                                    colide = False
                            elif button_easy.button_rect.collidepoint(pygame.mouse.get_pos()):
                                    obs_refresh()
                                    game_speed = GAMESPEED
                                    colide = False
                                    current_mode = MODE[1]
                                    
                    elif current_mode == MODE[1]:
                        obs.obstacle_rect.x -= 400
                        SCREEN.blit(SCENE[3], (0,0))
                        pygame.display.update()
                        pygame.time.wait(900)
                                    
                                    
        if current_state == STATE[3]:
            game_speed = 0
            SCREEN.blit(SCENE[2], (0,0))
        
                
        clock.tick(35)
        pygame.display.update()

if __name__ == "__main__":
    game()