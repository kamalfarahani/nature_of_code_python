import random
import pygame


gravity_constant = 5
eps = 0.01


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

        self.position = pygame.Vector2(width // 2, height // 2)
        self.velocity = pygame.Vector2(0, 0)

    def update(self) -> None:
        mouse_position = pygame.Vector2(*pygame.mouse.get_pos())
        distance = mouse_position - self.position
        acceleration_dir = distance.normalize()
        acceleration = acceleration_dir * (
            gravity_constant / (distance.magnitude_squared() + eps)
        )
        self.velocity += acceleration
        self.position += self.velocity

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
        mover.show(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
