import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
 
class Player(pygame.sprite.Sprite): # Player Sprite
 
    # Constructor function
    def __init__(self, x, y, colour):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([x, y ])
        self.image.fill(colour)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y): # Function to change speed of the Player
        self.change_x += x
        self.change_y += y
 
    def update(self):
        # Moving Left and Right mechanics
        self.rect.x += self.change_x
 
        # Moving Up and Down Mechanics
        self.rect.y += self.change_y
  
class Wall(pygame.sprite.Sprite):

    # Constructor function
    def __innit__(self, x, y, colour):
        # Call the parent's constructor
        super().__innit__()
        # Location for where it will be + Colour of the wall
        self.image = pygame.Surface([x, y ])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    # Set height, width
    
walls = [
    "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
    "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"]
    
    
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create a 1000 by 1000 sized screen
screen = pygame.display.set_mode([1000, 1000])
 
# Set the title of the window
pygame.display.set_caption('Role Playing Game')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 

 
# Create the player 
my_player = Player(50, 50, WHITE)


# Go through lists and draw a 40x40 wall in the location when 1 is found
for row in walls:
    for collums in row:
        if walls[row, collums] == '1':
            my_wall = Wall(x,y,BLUE)
        collums = collums + 1
    #next collum
    row = row + 1
#next row

 
all_sprite_list.add(my_player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_player.changespeed(-20, 0)
            elif event.key == pygame.K_RIGHT:
                my_player.changespeed(20, 0)
            elif event.key == pygame.K_UP:
                my_player.changespeed(0, -20)
            elif event.key == pygame.K_DOWN:
                my_player.changespeed(0, 20)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_player.changespeed(20, 0)
            elif event.key == pygame.K_RIGHT:
                my_player.changespeed(-20, 0)
            elif event.key == pygame.K_UP:
                my_player.changespeed(0, 20)
            elif event.key == pygame.K_DOWN:
                my_player.changespeed(0, -20)
 
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
