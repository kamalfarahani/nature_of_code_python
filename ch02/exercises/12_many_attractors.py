import random
import pygame

from math import sqrt


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


class Attractor:
    position: pygame.Vector2
    mass: float
    radius: int
    gravitational_constant: float

    def __init__(
        self,
        position: pygame.Vector2,
        mass: float,
        radius: int,
        gravitational_constant: float,
    ) -> None:
        self.position = position
        self.mass = mass
        self.radius = radius
        self.gravitational_constant = gravitational_constant
        self.is_dragging = False
        self.rollover = False
        self.drag_offset = pygame.Vector2(0, 0)

    def attract(self, mover: Mover) -> pygame.Vector2:
        dist = self.position - mover.position
        dist_constrained = dist.clamp_magnitude(5, 25)
        direction = dist.normalize()
        force = (
            self.gravitational_constant
            * self.mass
            * mover.mass
            / (dist_constrained.magnitude_squared())
        )

        return direction * force

    def handle_drag(self, mouse_position: pygame.Vector2) -> None:
        if self.is_dragging:
            self.position = mouse_position - self.drag_offset

    def handle_press(self, mouse_position: pygame.Vector2) -> None:
        dist = mouse_position - self.position
        if dist.magnitude() < self.radius:
            self.is_dragging = True
            self.drag_offset = mouse_position - self.position

    def stop_dragging(self) -> None:
        self.is_dragging = False

    def handle_hover(self, mouse_position: pygame.Vector2) -> None:
        dist = mouse_position - self.position
        if dist.magnitude() < self.radius:
            self.rollover = True
        else:
            self.rollover = False

    def show(self, surface: pygame.Surface) -> None:
        circle_surface = pygame.Surface(
            size=(self.radius * 2, self.radius * 2),
            flags=pygame.SRCALPHA,
        )

        if self.is_dragging:
            color = (0, 0, 0, 255)
        elif self.rollover:
            color = (0, 0, 0, 180)
        else:
            color = (0, 0, 0, 128)

        pygame.draw.circle(
            surface=circle_surface,
            color=color,
            center=(self.radius, self.radius),
            radius=self.radius,
            width=5,
        )
        surface.blit(
            source=circle_surface,
            dest=(self.position.x - self.radius, self.position.y - self.radius),
        )


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    attractors = []
    for _ in range(10):
        mass = random.uniform(1, 50)
        radius = int(sqrt(mass) * 2)
        attractor = Attractor(
            position=pygame.Vector2(
                random.randrange(0, display_width),
                random.randrange(0, display_height),
            ),
            mass=mass,
            radius=radius,
            gravitational_constant=0.5,
        )
        attractors.append(attractor)

    movers = []
    for _ in range(10):
        mass = random.uniform(1, 50)
        radius = int(sqrt(mass) * 2)
        mover = Mover(
            position=pygame.Vector2(
                random.randrange(0, display_width),
                random.randrange(0, display_height),
            ),
            mass=mass,
            radius=radius,
            width=display_width,
            height=display_height,
        )
        movers.append(mover)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            for attractor in attractors:
                mouse_position = pygame.Vector2(*pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    attractor.handle_press(mouse_position)
                if event.type == pygame.MOUSEBUTTONUP:
                    attractor.stop_dragging()
                if event.type == pygame.MOUSEMOTION:
                    attractor.handle_drag(mouse_position)
                    attractor.handle_hover(mouse_position)

        surface.fill((255, 255, 255))

        for mover in movers:
            for attractor in attractors:
                attract_force = attractor.attract(mover)

                mover.apply_force(attract_force)
            mover.update()
            mover.show(surface)

        for attractor in attractors:
            attractor.show(surface)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
