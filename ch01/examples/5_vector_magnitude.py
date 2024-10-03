import pygame


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    vector_center = pygame.Vector2(
        display_width // 2,
        display_height // 2,
    )

    gray = pygame.Color(180, 180, 180)
    black = pygame.Color(0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        origin = pygame.Vector2(
            display_width // 2,
            display_height // 2,
        )
        end = pygame.Vector2(*pygame.mouse.get_pos())
        vector = end - origin

        magnitude = vector.magnitude()

        pygame.draw.line(
            surface=screen,
            color=gray,
            start_pos=(display_width // 2, display_height // 2),
            end_pos=origin + vector,
            width=3,
        )

        pygame.draw.line(
            surface=screen,
            color=black,
            start_pos=(0, 20),
            end_pos=(magnitude, 20),
            width=15,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
