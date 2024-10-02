import random
import pygame


class Walker:
    position: pygame.Vector2

    def __init__(self, position: pygame.Vector2) -> None:
        self.position = position

    def step(self) -> None:
        self.position.x += random.randint(-1, 1)
        self.position.y += random.randint(-1, 1)


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    walker = Walker(
        pygame.Vector2(
            display_width // 2,
            display_height // 2,
        )
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Move the walker
        walker.step()

        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=(walker.position.x, walker.position.y),
            radius=2,
        )
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
