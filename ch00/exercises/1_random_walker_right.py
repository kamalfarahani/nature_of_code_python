import random
import pygame


class Walker:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def step(self) -> None:
        probability = random.random()
        if probability < 0.4:
            self.x += 1
        elif probability < 0.6:
            self.x -= 1
        elif probability < 0.8:
            self.y += 1
        else:
            self.y -= 1


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    walker = Walker(
        x=display_width // 2,
        y=display_height // 2,
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
            center=(walker.x, walker.y),
            radius=2,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
