import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    pygame.display.set_caption("Asteroids")
    _window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(_window_size)

    background = pygame.Surface(_window_size)
    background.fill(pygame.Color("#000000"))

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill("black")
        screen.blit(background, (0,0))  
        player.update(dt)      
        player.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()