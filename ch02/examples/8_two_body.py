from __future__ import annotations

import pygame

from math import sqrt


G = 1


class Body:
    position: pygame.Vector2
    velocity: pygame.Vector2
    acceleration: pygame.Vector2
    mass: float
    radius: int

    def __init__(
        self,
        position: pygame.Vector2,
        mass: float,
        radius: int,
    ) -> None:
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = mass
        self.radius = radius

    def apply_force(self, force: pygame.Vector2) -> None:
        self.acceleration += force / self.mass

    def update(self) -> None:
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)

    def attract(self, other: Body) -> None:
        if self.position == other.position:
            return

        distance_direction = (self.position - other.position).normalize()
        distance = (self.position - other.position).clamp_magnitude(5, 25).magnitude()

        force = (G * other.mass * self.mass / (distance**2)) * distance_direction
        other.apply_force(force)

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
    surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    body_1 = Body(
        position=pygame.Vector2(
            display_width // 2,
            40,
        ),
        mass=8,
        radius=20,
    )

    body_2 = Body(
        position=pygame.Vector2(
            display_width // 2,
            200,
        ),
        mass=8,
        radius=20,
    )

    body_1.velocity = pygame.Vector2(1, 0)
    body_2.velocity = pygame.Vector2(-1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        surface.fill((255, 255, 255))

        body_1.attract(body_2)
        body_2.attract(body_1)

        body_1.update()
        body_2.update()

        body_1.show(surface)
        body_2.show(surface)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
