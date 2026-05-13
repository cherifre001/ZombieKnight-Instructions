import pygame

from settings import FPS, WINDOW_HEIGHT, WINDOW_WIDTH, display_surface
from zombie import Zombie
from ruby import Ruby

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (25, 200, 25)

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group):
        """Initialize the game"""
        #Set constant variables
        self.STARTING_ROUND_TIME = 30
        self.STARTING_ZOMBIE_CREATION_TIME = 5

        #Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

        #Set fonts
        self.title_font = pygame.font.Font("fonts/Poultrygeist.ttf", 48)
        self.HUD_font = pygame.font.Font("fonts/Pixel.ttf", 24)

        #Set sounds
        self.lost_ruby_sound = pygame.mixer.Sound("sounds/lost_ruby.wav")
        self.ruby_pickup_sound = pygame.mixer.Sound("sounds/ruby_pickup.wav")
        pygame.mixer.music.load("sounds/level_music.wav")

        #Attach groups and sprites
        self.player = player
        self.zombie_group = zombie_group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        self.ruby_group = ruby_group


    def update(self):
        """Update the game"""
        #Update the round time every second
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

        self.check_collisions()
        self.add_zombie()
        self.check_round_completion()
        self.check_game_over()


    def draw(self):
        """Draw the game HUD"""

        #Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render("Health: " + str(self.player.health), True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        #Draw the HUD
        display_surface.blit(score_text, score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)


    def add_zombie(self):
        """Add a zombie to the game"""
        #Check to add a zombie every second
        if self.frame_count % FPS == 0:
            #Only add a zombie if zombie creation time has passed
            if self.round_time % self.zombie_creation_time == 0:
                zombie = Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                self.zombie_group.add(zombie)


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        #See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.zombie_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True

        #See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.player, self.zombie_group, False)
        if collision_list:
            for zombie in collision_list:
                #The zombie is dead; stomp it
                if zombie.is_dead:
                    zombie.kick_sound.play()
                    zombie.kill()
                    self.score += 25

                    ruby = Ruby(self.platform_group, self.portal_group)
                    self.ruby_group.add(ruby)
                #The zombie isn't dead, so take damage
                else:
                    self.player.health -= 20
                    self.player.hit_sound.play()
                    #Move the player to not continually take damage
                    self.player.position.x -= 256*zombie.direction
                    self.player.rect.bottomleft = self.player.position

        #See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.player, self.ruby_group, True):
            self.ruby_pickup_sound.play()
            self.score += 100
            self.player.health += 10
            if self.player.health > self.player.STARTING_HEALTH:
                self.player.health = self.player.STARTING_HEALTH

        #See if a living zombie collided with a ruby
        for zombie in self.zombie_group:
            if not zombie.is_dead:
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    self.lost_ruby_sound.play()
                    zombie = Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                    self.zombie_group.add(zombie)


    def check_round_completion(self):
        """Check if the player survived a single night"""
        if self.round_time == 0:
            self.start_new_round()


    def check_game_over(self):
        """Check to see if the player lost the game"""
        if self.player.health <= 0:
            pygame.mixer.music.stop()
            self.pause_game("Game Over! Final Score: " + str(self.score), "Press 'Enter' to play again...")
            self.reset_game()


    def start_new_round(self):
        """Start a new night"""
        self.round_number += 1

        #Decrease zombie creation time...more zombies
        if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            self.zombie_creation_time -= 1

        #Reset round values
        self.round_time = self.STARTING_ROUND_TIME

        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()

        self.player.reset()

        self.pause_game("You survived the night!", "Press 'Enter' to continue...")


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        pygame.mixer.music.pause()

        #Create main pause text
        main_text = self.title_font.render(main_text, True, GREEN)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        #Create sub pause text
        sub_text = self.title_font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        #Pause the game until user hits enter or quits
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #User wants to continue
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                        pygame.mixer.music.unpause()
                #User wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    pygame.mixer.music.stop()


    def reset_game(self):
        """Reset the game"""
        #Reset game values
        self.score = 0
        self.round_number = 1
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

        #Reset the player
        self.player.health = self.player.STARTING_HEALTH
        self.player.reset()

        #Empty sprite groups
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()

        pygame.mixer.music.play(-1, 0.0)
