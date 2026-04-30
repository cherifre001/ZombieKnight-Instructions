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
        # TODO: assign 30 to self.STARTING_ROUND_TIME
        # TODO: assign 5 to self.STARTING_ZOMBIE_CREATION_TIME

        #Set game values
        # TODO: assign 0 to self.score
        # TODO: assign 1 to self.round_number
        # TODO: assign 0 to self.frame_count
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_creation_time

        #Set fonts
        # TODO: assign pygame.font.Font() to self.title_font with these 2 arguments
        #  1: "fonts/Poultrygeist.ttf"
        #  2: 48
        # TODO: assign pygame.font.Font() to self.HUD_font with these 2 arguments
        #  1: "fonts/Pixel.ttf"
        #  2: 24

        #Set sounds
        # TODO: assign pygame.mixer.Sound() to self.lost_ruby_sound with this 1 argument
        #  1: "sounds/lost_ruby.wav"
        # TODO: assign pygame.mixer.Sound() to self.ruby_pickup_sound with this 1 argument
        #  1: "sounds/ruby_pickup.wav"
        # TODO: call pygame.mixer.music.load() with this 1 argument
        #  1: "sounds/level_music.wav"

        #Attach groups and sprites
        # TODO: assign player to self.player
        # TODO: assign zombie_group to self.zombie_group
        # TODO: assign platform_group to self.platform_group
        # TODO: assign portal_group to self.portal_group
        # TODO: assign bullet_group to self.bullet_group
        # TODO: assign ruby_group to self.ruby_group


    def update(self):
        """Update the game"""
        #Update the round time every second
        # TODO: add 1 to self.frame_count
        # TODO: if self.frame_count % FPS == 0:
            # TODO: subtract 1 from self.round_time
            # TODO: assign 0 to self.frame_count

        # TODO: call self.check_collisions()
        # TODO: call self.add_zombie()
        # TODO: call self.check_round_completion()
        # TODO: call self.check_game_over()


    def draw(self):
        """Draw the game HUD"""

        #Set text
        # TODO: assign self.HUD_font.render() to score_text with these 3 arguments
        #  1: "Score: " + str(self.score)
        #  2: True
        #  3: WHITE
        # TODO: assign score_text.get_rect() to score_rect
        # TODO: assign (10, WINDOW_HEIGHT - 50) to score_rect.topleft

        # TODO: assign self.HUD_font.render() to health_text with these 3 arguments
        #  1: "Health: " + str(self.player.health)
        #  2: True
        #  3: WHITE
        # TODO: assign health_text.get_rect() to health_rect
        # TODO: assign (10, WINDOW_HEIGHT - 25) to health_rect.topleft

        # TODO: assign self.title_font.render() to title_text with these 3 arguments
        #  1: "Zombie Knight"
        #  2: True
        #  3: GREEN
        # TODO: assign title_text.get_rect() to title_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25) to title_rect.center

        # TODO: assign self.HUD_font.render() to round_text with these 3 arguments
        #  1: "Night: " + str(self.round_number)
        #  2: True
        #  3: WHITE
        # TODO: assign round_text.get_rect() to round_rect
        # TODO: assign (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50) to round_rect.topright

        # TODO: assign self.HUD_font.render() to time_text with these 3 arguments
        #  1: "Sunrise In: " + str(self.round_time)
        #  2: True
        #  3: WHITE
        # TODO: assign time_text.get_rect() to time_rect
        # TODO: assign (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25) to time_rect.topright

        #Draw the HUD
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: score_text
        #  2: score_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: health_text
        #  2: health_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: title_text
        #  2: title_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: round_text
        #  2: round_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: time_text
        #  2: time_rect


    def add_zombie(self):
        """Add a zombie to the game"""
        #Check to add a zombie every second
        # TODO: if self.frame_count % FPS == 0:
            #Only add a zombie if zombie creation time has passed
            # TODO: if self.round_time % self.zombie_creation_time == 0:
                # TODO: assign Zombie() to zombie with these 4 arguments
                #  1: self.platform_group
                #  2: self.portal_group
                #  3: self.round_number
                #  4: 5 + self.round_number
                # TODO: call self.zombie_group.add() with this 1 argument
                #  1: zombie


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        #See if any bullet in the bullet group hit a zombie in the zombie group
        # TODO: assign pygame.sprite.groupcollide() to collision_dict with these 4 arguments
        #  1: self.bullet_group
        #  2: self.zombie_group
        #  3: True
        #  4: False
        # TODO: if collision_dict:
            # TODO: for zombies in collision_dict.values():
                # TODO: for zombie in zombies:
                    # TODO: call zombie.hit_sound.play()
                    # TODO: assign True to zombie.is_dead
                    # TODO: assign True to zombie.animate_death

        #See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        # TODO: assign pygame.sprite.spritecollide() to collision_list with these 3 arguments
        #  1: self.player
        #  2: self.zombie_group
        #  3: False
        # TODO: if collision_list:
            # TODO: for zombie in collision_list:
                #The zombie is dead; stomp it
                # TODO: if zombie.is_dead:
                    # TODO: call zombie.kick_sound.play()
                    # TODO: call zombie.kill()
                    # TODO: add 25 to self.score

                    # TODO: assign Ruby() to ruby with these 2 arguments
                    #  1: self.platform_group
                    #  2: self.portal_group
                    # TODO: call self.ruby_group.add() with this 1 argument
                    #  1: ruby
                #The zombie isn't dead, so take damage
                # TODO: else:
                    # TODO: subtract 20 from self.player.health
                    # TODO: call self.player.hit_sound.play()
                    #Move the player to not continually take damage
                    # TODO: subtract 256*zombie.direction from self.player.position.x
                    # TODO: assign self.player.position to self.player.rect.bottomleft

        #See if a player collided with a ruby
        # TODO: if pygame.sprite.spritecollide(self.player, self.ruby_group, True):
            # TODO: call self.ruby_pickup_sound.play()
            # TODO: add 100 to self.score
            # TODO: add 10 to self.player.health
            # TODO: if self.player.health > self.player.STARTING_HEALTH:
                # TODO: assign self.player.STARTING_HEALTH to self.player.health

        #See if a living zombie collided with a ruby
        # TODO: for zombie in self.zombie_group:
            # TODO: if not zombie.is_dead:
                # TODO: if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    # TODO: call self.lost_ruby_sound.play()
                    # TODO: assign Zombie() to zombie with these 4 arguments
                    #  1: self.platform_group
                    #  2: self.portal_group
                    #  3: self.round_number
                    #  4: 5 + self.round_number
                    # TODO: call self.zombie_group.add() with this 1 argument
                    #  1: zombie


    def check_round_completion(self):
        """Check if the player survived a single night"""
        # TODO: if self.round_time == 0:
            # TODO: call self.start_new_round()


    def check_game_over(self):
        """Check to see if the player lost the game"""
        # TODO: if self.player.health <= 0:
            # TODO: call pygame.mixer.music.stop()
            # TODO: call self.pause_game() with these 2 arguments
            #  1: "Game Over! Final Score: " + str(self.score)
            #  2: "Press 'Enter' to play again..."
            # TODO: call self.reset_game()


    def start_new_round(self):
        """Start a new night"""
        # TODO: add 1 to self.round_number

        #Decrease zombie creation time...more zombies
        # TODO: if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            # TODO: subtract 1 from self.zombie_creation_time

        #Reset round values
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time

        # TODO: call self.zombie_group.empty()
        # TODO: call self.ruby_group.empty()
        # TODO: call self.bullet_group.empty()

        # TODO: call self.player.reset()

        # TODO: call self.pause_game() with these 2 arguments
        #  1: "You survived the night!"
        #  2: "Press 'Enter' to continue..."


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        # TODO: call pygame.mixer.music.pause()

        #Create main pause text
        # TODO: assign self.title_font.render() to main_text with these 3 arguments
        #  1: main_text
        #  2: True
        #  3: GREEN
        # TODO: assign main_text.get_rect() to main_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) to main_rect.center

        #Create sub pause text
        # TODO: assign self.title_font.render() to sub_text with these 3 arguments
        #  1: sub_text
        #  2: True
        #  3: WHITE
        # TODO: assign sub_text.get_rect() to sub_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64) to sub_rect.center

        #Display the pause text
        # TODO: call display_surface.fill() with this 1 argument
        #  1: BLACK
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: main_text
        #  2: main_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: sub_text
        #  2: sub_rect
        # TODO: call pygame.display.update()

        #Pause the game until user hits enter or quits
        # TODO: assign True to is_paused
        # TODO: while is_paused:
            # TODO: for event in pygame.event.get():
                # TODO: if event.type == pygame.KEYDOWN:
                    #User wants to continue
                    # TODO: if event.key == pygame.K_RETURN:
                        # TODO: assign False to is_paused
                        # TODO: call pygame.mixer.music.unpause()
                #User wants to quit
                # TODO: if event.type == pygame.QUIT:
                    # TODO: assign False to is_paused
                    # TODO: call pygame.event.post() with this 1 argument
                    #  1: pygame.event.Event(pygame.QUIT)
                    # TODO: call pygame.mixer.music.stop()


    def reset_game(self):
        """Reset the game"""
        #Reset game values
        # TODO: assign 0 to self.score
        # TODO: assign 1 to self.round_number
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_creation_time

        #Reset the player
        # TODO: assign self.player.STARTING_HEALTH to self.player.health
        # TODO: call self.player.reset()

        #Empty sprite groups
        # TODO: call self.zombie_group.empty()
        # TODO: call self.ruby_group.empty()
        # TODO: call self.bullet_group.empty()

        # TODO: call pygame.mixer.music.play() with these 2 arguments
        #  1: -1
        #  2: 0.0