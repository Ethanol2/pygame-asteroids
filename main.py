import pygame;
from constants import *;
from player import Player;
from player import Shot;
from asteroid import Asteroid;
from asteroidfield import AsteroidField;

def main():
    print("Starting Asteroids!");
    print(f"Screen width: {SCREEN_WIDTH}");
    print(f"Screen height: {SCREEN_HEIGHT}");

    # System Stuff
    pygame.init();
    pyClock = pygame.time.Clock();
    deltaTime = 0;
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    
    # Groups
    updatableGroup = pygame.sprite.Group();
    drawableGroup = pygame.sprite.Group();
    asteroidGroup = pygame.sprite.Group();
    bulletGroup = pygame.sprite.Group();

    # Player
    Player.containers = (updatableGroup, drawableGroup);
    Shot.containers = (updatableGroup, drawableGroup, bulletGroup);
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2);

    # Asteroids
    Asteroid.containers = (asteroidGroup, updatableGroup, drawableGroup);
    AsteroidField.containers = (updatableGroup);
    asteroidField = AsteroidField();

    while (True):
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return;

        screen.fill((0,0,0));
        
        updatableGroup.update(deltaTime);
        for drawable in drawableGroup:
            drawable.draw(screen);
        
        for asteroid in asteroidGroup:
            if (player.check_colision(asteroid)):
                print("Game Over!");
                return;

        pygame.display.flip();
        deltaTime = pyClock.tick(60) / 1000;

if (__name__ == "__main__"):
    main();