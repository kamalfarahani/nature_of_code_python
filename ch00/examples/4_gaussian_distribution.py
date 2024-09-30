import pygame
import numpy as np


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    std = 60
    mean = display_width // 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        x_random = std * np.random.randn() + mean

        circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
        circle_surface.fill((0, 0, 0, 0))  # Fully transparent

        pygame.draw.circle(
            surface=circle_surface,
            color=(255, 255, 255, 10),
            center=(10, 10),
            radius=10,
        )

        rect = circle_surface.get_rect()
        rect.centerx = round(x_random)
        rect.centery = display_height // 2
        screen.blit(
            source=circle_surface,
            dest=rect,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
