import pygame
import random
import math

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# Variables
bullet_count = 100
slow_mo = 100
score = 0
missed = 0
lives = 5
game_level=1
# Initialise PyGame
pygame.init()   

# Blank Screen
size = (680,680)
screen = pygame.display.set_mode(size)
# Title of new window/screen
pygame.display.set_caption("Slo-Mo!")


# Create groups for each sprite
wall_list= pygame.sprite.Group()
player_list = pygame.sprite.Group()
portal_list = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
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
        self.image = pygame.Surface([30, 30])
        self.image.fill(colour)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.speed_multiplier = 1
    def changespeed(self, x, y): # Function to change speed of the Player
        if self.speed_multiplier <= 0:
            self.speed_multiplier = 0.5
        self.change_x += x/self.speed_multiplier
        self.change_y += y/self.speed_multiplier
    

    def update(self):
        self.rect.y = self.rect.y + self.change_y
        self.rect.x = self.rect.x + self.change_x

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

class Portal(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        # Location for where it will be + Colour of the wall
        self.image = pygame.Surface([40, 40])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Nothing yet
    #End update
# End class

class bullet(pygame.sprite.Sprite):
    # Define the constructor for bullet
    def __init__(self, colour, width, height, x, y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        #End Procedure
    def update(self):
        self.rect.y += self.change_y
        self.rect.x += self.change_x
    #End Procedure
#End Class

class Enemy(pygame.sprite.Sprite):
    # Define the constructor for the enemies
    def __init__(self,colour,width,height,x,y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        # End procedure
    def update(self):

        self.rect.y = self.rect.y + self.change_y
        self.rect.x = self.rect.x + self.change_x
    # End Procedure
# End Class


def gameLoop(lives, score, level):
    done = False
    lives = 5
    score = 0
    level = 1
    # Create the objects from the classes
    def level_loop(lives, score, game_level):
        my_player = Player(300, 300, WHITE)
        player_list.add(my_player)
        all_sprites_group.add(my_player)
        game_level = game_level + 1
        bullet_count = 10
        no_of_enemies = 1* game_level
        for x in range (no_of_enemies):
            my_enemy = Enemy(RED, 30, 30, random.randrange(0,680), random.randrange(0, 10))
            my_enemy.change_y = 3    
            enemy_group.add(my_enemy)
            all_sprites_group.add(my_enemy)

        no_of_enemies = 1*game_level
        for x in range (no_of_enemies):
            my_enemy = Enemy(BLUE, 30, 30, random.randrange(0,680), random.randrange(670, 680))
            my_enemy.change_y = -3
            enemy_group.add(my_enemy)
            all_sprites_group.add(my_enemy)

        no_of_enemies = 1*game_level
        for x in range (no_of_enemies):
            my_enemy = Enemy(WHITE, 30, 30, random.randrange(10,50), random.randrange(0, 680))
            my_enemy.change_x = 3
            enemy_group.add(my_enemy)
            all_sprites_group.add(my_enemy)

        no_of_enemies = 1*game_level
        for x in range (no_of_enemies):
            my_enemy = Enemy(WHITE, 30, 30, random.randrange(650,680), random.randrange(0, 680))
            my_enemy.change_x = -3
            enemy_group.add(my_enemy)
            all_sprites_group.add(my_enemy)




        # Go through lists and draw a 40x40 wall in the location when 1 is foundq

        # Create a walls list, with all locations for walls in-game
        walls = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

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
            elif walls[block] == 2:
                my_portal = Portal(x, y)
                portal_list.add(my_portal)
                all_sprites_group.add(my_portal)            
        #Next Operation
        done = False
        while not done:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        my_player.changespeed(-10, 0)
                    elif event.key == pygame.K_d:
                        my_player.changespeed(10, 0)
                    elif event.key == pygame.K_w:
                        my_player.changespeed(0, -10)
                    elif event.key == pygame.K_s:
                        my_player.changespeed(0, 10)
                    elif event.key == pygame.K_LSHIFT:
                        my_player.speed_multiplier = 2
        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        my_player.changespeed(10, 0)
                    elif event.key == pygame.K_d:
                        my_player.changespeed(-10, 0)
                    elif event.key == pygame.K_w:
                        my_player.changespeed(0, 10)
                    elif event.key == pygame.K_s:
                        my_player.changespeed(0, -10)
                    elif event.key == pygame.K_LSHIFT:
                        my_player.speed_multiplier = 1                   

                        # End if



                
                
                # create the bullet in the direction that they key is pressed
                    if bullet_count != 0:
                        if event.key == pygame.K_UP:
                            my_bullet = bullet(WHITE, 10, 10, (my_player.rect.x) + 4, my_player.rect.y)
                            bullet_group.add(my_bullet)
                            all_sprites_group.add(my_bullet)
                            my_bullet.change_y = -3
                            bullet_count = bullet_count - 1
                    if bullet_count != 0:
                        if event.key == pygame.K_DOWN:
                            my_bullet = bullet(WHITE, 10, 10, (my_player.rect.x) + 4, my_player.rect.y)
                            bullet_group.add(my_bullet)
                            all_sprites_group.add(my_bullet)
                            my_bullet.change_y = 3
                            bullet_count = bullet_count - 1
                    if bullet_count != 0:
                        if event.key == pygame.K_LEFT:
                            my_bullet = bullet(WHITE, 10, 10, (my_player.rect.x) + 4, my_player.rect.y)
                            bullet_group.add(my_bullet)
                            all_sprites_group.add(my_bullet)
                            my_bullet.change_x = -3                    
                            bullet_count = bullet_count - 1
                    if bullet_count != 0:
                        if event.key == pygame.K_RIGHT:
                            my_bullet = bullet(WHITE, 10, 10, (my_player.rect.x) + 4, my_player.rect.y)
                            bullet_group.add(my_bullet)
                            all_sprites_group.add(my_bullet)
                            my_bullet.change_x = 3                
                            bullet_count = bullet_count - 1
                    # Allows the player to move Left/Right
                
                my_player.rect.x += my_player.change_x

                wall_hit_list = pygame.sprite.spritecollide(my_player, wall_list, False)
                for block in wall_hit_list:
                    if my_player.change_x > 0:
                        my_player.rect.right = block.rect.left

                    else:
                        # Otherwise if we are moving left, do the opposite.
                        my_player.rect.left = block.rect.right
 
                    # Allows the player to move Up/Down
                my_player.rect.y += my_player.change_y

                wall_hit_list = pygame.sprite.spritecollide(my_player, wall_list, False)
                for block in wall_hit_list:
                    # Reset our position based on the top/bottom of the object.
                    if my_player.change_y > 0:
                        my_player.rect.bottom = block.rect.top

                    else:
                        my_player.rect.top = block.rect.bottom
            for my_bullet in bullet_group:
                if pygame.sprite.groupcollide(bullet_group, enemy_group, True, True):
                    score = score + 5
                    print("Score:" + str(score))
            for my_enemy in enemy_group:
                if pygame.sprite.groupcollide(enemy_group, wall_list, False, False):
                    score = score 
            for my_bullet in bullet_group:
                if pygame.sprite.groupcollide(bullet_group, wall_list, True, False):
                    pass

            if pygame.sprite.groupcollide(player_list, portal_list, True, True):
                my_player.change_y = 0
                my_player.change_x = 0
                my_player.rect.x = 300
                my_player.rect.y = 300
                level_loop(lives, score, game_level)

            if pygame.sprite.groupcollide(player_list, enemy_group, False, False):
                    print("GAME OVER")
                    gameOver()                
                    done = True                
            # End

                
            # End   
            keys = pygame.key.get_pressed()
            all_sprites_group.update()
        
            screen.fill(BLACK)
        
            all_sprites_group.draw(screen)
            #display lives
            font = pygame.font.Font('freesansbold.ttf', 10)
            text = font.render(("LIVES: " + str(lives)), 1, WHITE)
            screen.blit(text, (10, 15))

            #display bullet count
            font = pygame.font.Font('freesansbold.ttf', 10)
            text = font.render(("BULLETS: " + str(bullet_count)), 1, WHITE)
            screen.blit(text, (10, 25))

            #display score
            font = pygame.font.Font('freesansbold.ttf', 10)
            text = font.render(("SCORE: " + str(score)), 1, WHITE)
            screen.blit(text, (10, 35))  
            # --flip display to reveal changes made to objects  
            pygame.display.flip()
            # - The clock ticks over
            clock.tick(60)
            #End While - End of game loop
    level_loop(lives, score, game_level)
# End


def gameOver():
    done = False
    while not done:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: # when a key is down
                if event.key == pygame.K_ESCAPE: # if the escape key pressed done = True
                    done = True
                if event.key == pygame.K_RETURN:
                    gameLoop(5,0, 1)  
                #End If
        screen.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("GAME OVER", 1, WHITE)
        screen.blit(text, (160, 200))
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render("PRESS ENTER TO PLAY AGAIN!", 1, WHITE)
        screen.blit(text, (160, 270))        
        pygame.display.flip()
        clock.tick(60)
  
  
gameLoop(5,0, 1)  
# End game
pygame.quit()
