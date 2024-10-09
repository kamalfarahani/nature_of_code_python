from __future__ import annotations

import random
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
    ) -> None:
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = mass
        self.radius = int(sqrt(mass) * 2)

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

    center = pygame.Vector2(
        display_width // 2,
        display_height // 2,
    )

    sun = Body(
        position=pygame.Vector2(
            display_width // 2,
            display_height // 2,
        ),
        mass=500,
    )

    bodies: list[Body] = []
    for _ in range(10):
        distance_from_center = pygame.Vector2(
            random.uniform(-100, 100),
            random.uniform(-100, 100),
        ).normalize() * random.randint(100, 150)

        body = Body(
            position=distance_from_center + center,
            mass=random.randint(10, 15),
        )
        body.velocity = distance_from_center.normalize().rotate(90) * random.uniform(
            10, 15
        )
        bodies.append(body)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        surface.fill((255, 255, 255))

        for body_1 in bodies:
            for body_2 in bodies:
                if body_2 is not body_1:
                    body_2.attract(body_1)

            sun.attract(body_1)
            body_1.update()
            body_1.show(surface)

        sun.show(surface)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
