import random
import pygame


class Mover:
    position: pygame.Vector2
    velocity: pygame.Vector2
    width: int
    height: int

    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        self.width = width
        self.height = height

        self.position = pygame.Vector2(
            random.randint(0, width),
            random.randint(0, height),
        )
        self.velocity = pygame.Vector2(
            random.uniform(-2, 2),
            random.uniform(-2, 2),
        )

    def update(self) -> None:
        self.position += self.velocity

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
    display_width = 640
    display_height = 480
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
