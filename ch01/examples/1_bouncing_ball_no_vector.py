import pygame


def main() -> None:
    pygame.init()
    display_width = 640
    display_height = 240
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    ball_x = 100
    ball_y = 100
    x_speed = 2.5
    y_speed = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        ball_x += x_speed
        ball_y += y_speed

        if ball_x < 0 or ball_x > display_width:
            x_speed = -x_speed
        if ball_y < 0 or ball_y > display_height:
            y_speed = -y_speed

        pygame.draw.circle(
            surface=screen,
            color=(0, 0, 0),
            center=(ball_x, ball_y),
            radius=20,
            width=2,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
