import pygame;
from constants import *;
from player import *;

def main():
    print("Starting Asteroids!");
    print(f"Screen width: {SCREEN_WIDTH}");
    print(f"Screen height: {SCREEN_HEIGHT}");

    # System Stuff
    pygame.init();
    pyClock = pygame.time.Clock();
    deltaTime = 0;
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));

    # Game Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2);

    while (True):
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return;

        screen.fill((0,0,0));

        player.draw(screen);

        pygame.display.flip();
        deltaTime = pyClock.tick(60) / 1000;

if (__name__ == "__main__"):
    main();