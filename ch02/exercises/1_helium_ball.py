import pygame

from noise import snoise2


class Ball:
    position: pygame.Vector2
    velocity: pygame.Vector2
    acceleration: pygame.Vector2
    radius: int
    width: int
    height: int

    def __init__(
        self,
        position: pygame.Vector2,
        radius: int,
        width: int,
        height: int,
    ) -> None:
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.radius = radius
        self.width = width
        self.height = height

    def apply_force(self, force: pygame.Vector2) -> None:
        self.acceleration += force

    def check_edges(self) -> None:
        if self.position.x > self.width - self.radius:
            self.position.x = self.width - self.radius
            self.velocity.x *= -1

        if self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -1

        if self.position.y > self.height - self.radius:
            self.position.y = self.height - self.radius
            self.velocity.y *= -1

        if self.position.y < self.radius:
            self.position.y = self.radius
            self.velocity.y *= -1

    def update(self) -> None:
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=surface,
            color=(0, 0, 0),
            center=(self.position.x, self.position.y),
            radius=self.radius,
            width=2,
        )


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    ball = Ball(
        position=pygame.Vector2(display_width // 2, display_height // 2),
        radius=20,
        width=display_width,
        height=display_height,
    )

    fly_force = pygame.Vector2(0, -0.5)

    t = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        # Generate wind based on Perlin noise
        wind = pygame.Vector2(snoise2(t, 0), 0) * 0.1

        ball.apply_force(fly_force)
        ball.apply_force(wind)
        ball.update()
        ball.check_edges()
        ball.show(screen)

        pygame.display.update()

        clock.tick(60)
        t += 0.01


if __name__ == "__main__":
    main()
