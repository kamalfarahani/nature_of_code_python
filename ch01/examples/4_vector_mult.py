import pygame


def main() -> None:
    pygame.init()
    display_width = 1000
    display_height = 800
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

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
            start_pos=origin,
            end_pos=origin + vector * 0.5,  # Multiply by 0.5
            width=5,
        )

        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
