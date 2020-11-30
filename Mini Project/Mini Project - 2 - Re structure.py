import pygame
import random
import math

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
# Initialise PyGame
pygame.init()   

# Blank Screen
size = (680,680)
screen = pygame.display.set_mode(size)
# Title of new window/screen
pygame.display.set_caption("Tile Game!")

# Create groups for each sprite
wall_list= pygame.sprite.Group()
player_list = pygame.sprite.Group()

# Create a group of all sprites together
all_sprites_group = pygame.sprite.Group()

# Manages how fast screen refreshes
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite): # Player Sprite
 
    # Constructor function
    def __init__(self, x, y, colour):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([x, y])
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
        # Allows the player to move Left/Right
        self.rect.x += self.change_x

        wall_hit_list = pygame.sprite.spritecollide(my_player, wall_list, False)
        for block in wall_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left

            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Allows the player to move Up/Down
        self.rect.y += self.change_y

        wall_hit_list = pygame.sprite.spritecollide(my_player, wall_list, False)
        for block in wall_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            else:
                self.rect.top = block.rect.bottom
# End Procedure

class Wall(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        # Location for where it will be + Colour of the wall
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Nothing yet
    #End update
# End class


my_player = Player(50, 50, WHITE)
player_list.add(my_player)
all_sprites_group.add(my_player)

# Go through lists and draw a 40x40 wall in the location when 1 is foundq

# Create a walls list, with all locations for walls in-game
walls = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

x = 0
y = 0

for block in range(0, 289):
    if block == 0:
        x = 0
    else:
        x = x + 40


    if block == 0:
        y = 0
    elif block % 17 == 0:
        x = 0
        y = y + 40

    # Use the walls class to create a wall in the position of a 1
    if walls[block] == 1:
        my_wall = Wall(x, y)
        wall_list.add(my_wall)
        all_sprites_group.add(my_wall)
        block = block + 1
    elif walls[block] ==  0:
        block = block + 1
#Next Operation
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

    all_sprites_group.update()
 
    screen.fill(BLACK)
 
    all_sprites_group.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()


