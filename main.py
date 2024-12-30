import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.set_caption("Asteroids")
    _window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(_window_size)

    background = pygame.Surface(_window_size)
    background.fill(pygame.Color("#000000"))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.blit(background, (0,0))  
        for u in updatable:
            u.update(dt)
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()