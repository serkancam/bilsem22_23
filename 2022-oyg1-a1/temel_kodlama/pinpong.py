import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ilk oyun!")
clock = pygame.time.Clock()


player_img = pygame.image.load("temel_kodlama/playerShip1.png").convert()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
       
        self.rect.centerx =x
        self.rect.bottom = y     
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8        
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
# Game loop
game_over = True
running = True
while running:
    if game_over:
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player1 = Player(10,50)
        player2 = Player(10,430)
        all_sprites.add(player1)
        all_sprites.add(player2)
        
      

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    screen.fill(BLACK)
  
    all_sprites.draw(screen)

   
    # Draw / render
    # screen.fill(BLACK)    
    pygame.display.flip()

pygame.quit()