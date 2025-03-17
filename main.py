# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #establish groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)



    # create player instance   
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
 
    #create asteroidfield instance
    asteroidfield = AsteroidField()
    
    #initiate game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0,0,0)
        screen.fill(black)

        updatable.update(dt)

        for asteroid in asteroids.copy():
            if asteroid.collision(player):
                sys.exit("Game over!")
            for shot in shots.copy():
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()


        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()