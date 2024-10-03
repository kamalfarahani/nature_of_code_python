import random
import pygame


class Mover:
    position: pygame.Vector2
    velocity: pygame.Vector2
    width: int
    height: int
    max_velocity: float

    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        self.width = width
        self.height = height
        self.max_velocity = 10.0

        self.position = pygame.Vector2(width // 2, height // 2)
        self.velocity = pygame.Vector2(0, 0)

    def update(self) -> None:
        mouse_position = pygame.Vector2(*pygame.mouse.get_pos())
        acceleration_dir = (mouse_position - self.position).normalize()
        self.velocity += acceleration_dir * 0.5
        self.velocity = self.velocity.clamp_magnitude(0, self.max_velocity)
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
