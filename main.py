import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    pygame.init()
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(player)






def game_loop(player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        updatable.update(dt)
        screen.fill("black")
        for object in asteroids:
            if object.collision(player):
                sys.exit("Game Over!")
        
        for object in asteroids:
            for shot in shots:
                if object.collision(shot):
                    object.split()
                    shot.kill()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        
        



























if __name__ == "__main__":
    main()
  