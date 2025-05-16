import pygame
from constants import *
from player import Player


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock= pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip() 
       
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()