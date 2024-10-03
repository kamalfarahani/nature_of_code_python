import random
import pygame

from noise import snoise2


class Mover:
    position: pygame.Vector2
    velocity: pygame.Vector2
    width: int
    height: int
    t: float

    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        self.width = width
        self.height = height
        self.t = 0

        self.position = pygame.Vector2(width // 2, height // 2)
        self.velocity = pygame.Vector2(0, 0)

    def update(self) -> None:
        acceleration = pygame.Vector2(
            snoise2(self.t, 0),
            snoise2(0, self.t + 1000),
        )

        self.velocity += acceleration * random.random()
        self.position += self.velocity
        self.t += 0.01

    def check_edge(self) -> None:
        if self.position.x < 0:
            self.position.x = self.width
        if self.position.x > self.width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = self.height
        if self.position.y > self.height:
            self.position.y = 0

    def show(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=surface,
            color=(0, 0, 0),
            center=(self.position.x, self.position.y),
            radius=20,
            width=0,
        )


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    mover = Mover(display_width, display_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        mover.update()
        mover.check_edge()
        mover.show(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
