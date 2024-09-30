import pygame

from noise import snoise3


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

    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in range(display_width):
            for j in range(display_height):
                x = i / 100
                y = j / 100
                n = int(
                    map_values(
                        value=snoise3(x, y, t),
                        left_min=-1,
                        left_max=1,
                        right_min=0,
                        right_max=255,
                    )
                )
                screen.set_at((i, j), (n, n, n, 255))

        t += 0.01
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
