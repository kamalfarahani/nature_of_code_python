import pygame


def main() -> None:
    pygame.init()
    display_width = 640
    display_height = 240
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    position = pygame.Vector2(100, 100)
    velocity = pygame.Vector2(2.5, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))

        position += velocity
        if position.x < 0 or position.x > display_width:
            velocity.x = -velocity.x
        if position.y < 0 or position.y > display_height:
            velocity.y = -velocity.y

        pygame.draw.circle(
            surface=screen,
            color=(0, 0, 0),
            center=(position.x, position.y),
            radius=20,
            width=2,
        )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
