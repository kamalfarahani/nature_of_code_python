import pygame

from noise import snoise2


class Walker:
    x: int
    y: int
    tx: float
    ty: float
    display_width: int
    display_height: int

    def __init__(
        self,
        x: int,
        y: int,
        display_width: int,
        display_height: int,
    ) -> None:
        self.x = x
        self.y = y
        self.display_width = display_width
        self.display_height = display_height
        self.tx = 0
        self.ty = 1000

    def step(self) -> None:
        self.x = round(
            map_values(
                snoise2(self.tx, 0),
                -1,
                1,
                0,
                self.display_width,
            )
        )

        self.y = round(
            map_values(
                snoise2(self.ty, 0),
                -1,
                1,
                0,
                self.display_height,
            )
        )

        self.tx += 0.01
        self.ty += 0.01


def map_values(
    value: float,
    left_min: float,
    left_max: float,
    right_min: float,
    right_max: float,
) -> float:
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    value_scaled = float(value - left_min) / float(left_span)

    # Convert the 0-1 range into a value in the right range.
    return right_min + (value_scaled * right_span)


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    walker = Walker(
        x=display_width // 2,
        y=display_height // 2,
        display_width=display_width,
        display_height=display_height,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Move the walker
        walker.step()

        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=(walker.x, walker.y),
            radius=5,
            width=2,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
