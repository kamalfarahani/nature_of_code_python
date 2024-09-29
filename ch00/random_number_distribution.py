import random
import pygame


def main() -> None:
    pygame.init()
    display_width = 640
    display_height = 480
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    total_numbers = 20
    random_counts = [0] * total_numbers

    rect_width = display_width // total_numbers
    rect_height = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        new_number = random.randint(0, total_numbers - 1)
        random_counts[new_number] += 1

        for idx, count in enumerate(random_counts):
            rect = pygame.Rect(
                idx * rect_width,
                display_height - count * rect_height,
                rect_width,
                count * rect_height,
            )

            pygame.draw.rect(
                surface=screen,
                color=(255, 255, 255),
                rect=rect,
                width=2,
            )

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
