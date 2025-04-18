import pygame
from constants import *
from player import *
from circleshape import *

Clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(player)






def game_loop(player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        
        



























if __name__ == "__main__":
    main()
  