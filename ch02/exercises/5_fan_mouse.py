import pygame

from math import e


class Mover:
    position: pygame.Vector2
    velocity: pygame.Vector2
    acceleration: pygame.Vector2
    mass: float
    radius: int
    width: int
    height: int

    def __init__(
        self,
        position: pygame.Vector2,
        mass: float,
        radius: int,
        width: int,
        height: int,
    ) -> None:
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = mass
        self.radius = radius
        self.width = width
        self.height = height

    def apply_force(self, force: pygame.Vector2) -> None:
        acceleration = force / self.mass
        self.acceleration += acceleration

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

    mover = Mover(
        position=pygame.Vector2(100, 100),
        mass=1,
        radius=20,
        width=display_width,
        height=display_height,
    )

    gravity_force = pygame.Vector2(0, 0.5)

    t = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_position = pygame.Vector2(mouse_x, mouse_y)
            distance_from_mouse = mouse_position - mover.position
            wind_force_direction = distance_from_mouse.normalize()
            wind_force = (
                wind_force_direction
                * -(e ** (-distance_from_mouse.magnitude() / 100))
                * 0.5
            )
        else:
            wind_force = pygame.Vector2(0, 0)

        mover.apply_force(gravity_force)
        mover.apply_force(wind_force)
        mover.check_edges()
        mover.update()
        mover.show(screen)

        pygame.display.update()
        clock.tick(60)
        t += 0.01


if __name__ == "__main__":
    main()
