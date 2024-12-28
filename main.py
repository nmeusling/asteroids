import pygame
from constants import *


def main():
    pygame.init()

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

        screen.blit(background, (0,0))        
    
        pygame.display.update()

if __name__ == "__main__":
    main()