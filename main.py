import pygame
from constants import *
from player import Player


def main():
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
        player1.update(dt)
        screen.fill("black")
        player1.draw(screen)
      
        
        pygame.display.flip() 
       
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()