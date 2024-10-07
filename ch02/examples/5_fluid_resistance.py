import pygame


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

    def bounce_edges(self) -> None:
        bounce = -0.9
        if self.position.x > self.width - self.radius:
            self.position.x = self.width - self.radius
            self.velocity.x *= bounce

        if self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= bounce

        if self.position.y > self.height - self.radius:
            self.position.y = self.height - self.radius
            self.velocity.y *= bounce

        if self.position.y < self.radius:
            self.position.y = self.radius
            self.velocity.y *= bounce

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


class Fluid:
    x: int
    y: int
    width: int
    height: int
    coefficient: float

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        coefficient: float,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coefficient = coefficient

    def contains(self, mover: Mover) -> bool:
        position = mover.position

        return (
            self.x < position.x < self.x + self.width
            and self.y < position.y < self.y + self.height
        )

    def calculate_drag(self, mover: Mover) -> pygame.Vector2:
        speed = mover.velocity.magnitude()
        if speed == 0:
            return pygame.Vector2(0, 0)
        drag_magnitude = self.coefficient * speed * speed
        drag_force = mover.velocity.normalize() * -1 * drag_magnitude

        return drag_force

    def show(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(
            surface=surface,
            color=(128, 128, 128),
            rect=(self.x, self.y, self.width, self.height),
        )


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    gravity = pygame.Vector2(0, 0.1)
    movers = [
        Mover(
            position=pygame.Vector2(100, 100),
            mass=1,
            radius=20,
            width=display_width,
            height=display_height,
        ),
        Mover(
            position=pygame.Vector2(500, 100),
            mass=5,
            radius=50,
            width=display_width,
            height=display_height,
        ),
        Mover(
            position=pygame.Vector2(800, 100),
            mass=10,
            radius=80,
            width=display_width,
            height=display_height,
        ),
    ]

    fluid = Fluid(
        x=0,
        y=display_height // 2,
        width=display_width,
        height=display_width // 2,
        coefficient=0.1,
    )

    while True:
        surface.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                return

        fluid.show(surface)

        for mover in movers:
            if fluid.contains(mover):
                drag = fluid.calculate_drag(mover)
                mover.apply_force(drag)

            mover.apply_force(gravity * mover.mass)
            mover.update()
            mover.bounce_edges()

            mover.show(surface)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
