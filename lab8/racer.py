import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Other Variables 
w = 400
h = 600
speed = 5
score = 0
scorecoin = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
coin_got = font_small.render("Coin got", 1, (0, 0, 0))
game_over = font.render("Game Over", True, (0,0,0))
 
 
#Create a screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption("Game")
background = pygame.image.load("AnimatedStreet.png")

#classes for characters 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40), 0)  
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global scorecoin
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)

 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < w:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
incspeed = pygame.USEREVENT + 1
pygame.time.set_timer(incspeed, 1000)
 
#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == incspeed:
              incspeed += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(score), True, (0, 0, 0))
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Redraws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill((255, 0, 0))
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  

    #To be run collision between Player and Coin
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_collisions:
        scorecoin += 1
        pygame.display.update()

    if len(coins) < 1:  # Ensure there are always at least 1 coin on the screen
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)


    # Remove coins that have gone off-screen
    for coin in coins:
        if coin.rect.top > h:
            coin.kill()
    

    coin_text = font_small.render(f"{scorecoin}", True, (0, 0, 0))
    DISPLAYSURF.blit(coin_text, (300, 10))
         
    pygame.display.update()
    FramePerSec.tick(FPS)

