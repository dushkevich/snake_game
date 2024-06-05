import pygame
import random

pygame.init()

# Set the colors
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)

# Set parameters for black screen
black_screen = pygame.display
black_surface = black_screen.set_mode(size=(600, 450))
black_surface.fill(BLACK)
black_screen.set_caption("Red Moving Snake")

clock = pygame.time.Clock()

# Right and left, up and down (parameters for snake movement)
r_l = [285]
u_d = [225]

snake_tail = 0

vertical = 0
horizontal = 15

chunk_timer = 0

run = True

while run:

    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Rectangle of the snake
    red_rect = pygame.Rect(r_l[0], u_d[0], 15, 15)
    pygame.draw.rect(surface=black_surface, color=RED, rect=red_rect, width=0)

    if chunk_timer == 0:
        chunk_left = random.randint(0, 585)
        chunk_top = random.randint(0, 435)

    white_chunk = pygame.Rect(chunk_left, chunk_top, 15, 15)
    pygame.draw.rect(black_surface, WHITE, white_chunk, 0)
    chunk_timer += 1

    if chunk_timer == 70:
        chunk_timer = 0

    if red_rect.colliderect(white_chunk):
        chunk_timer = 0
        snake_tail += 1
        u_d.append(u_d[-1])
        r_l.append(r_l[-1])

    print('Before')
    print(u_d)
    print(r_l)

    print(len(u_d))
    for tail in range(snake_tail):
        if tail >= 1:
            if red_rect.colliderect(snake_itself):
                run = False
            elif red_rect.colliderect(snake_end):
                run = False

        snake_itself = pygame.Rect(r_l[tail+1], u_d[tail+1], 15, 15)
        pygame.draw.rect(surface=black_surface, color=RED, rect=snake_itself, width=0)
        snake_end = pygame.Rect(r_l[-1], u_d[-1], 15, 15)
        pygame.draw.rect(surface=black_surface, color=RED, rect=snake_end, width=0)

        u_d.reverse()
        r_l.reverse()
        u_d[tail] = u_d[tail+1]
        r_l[tail] = r_l[tail+1]
        u_d.reverse()
        r_l.reverse()

    u_d[0] = u_d[0] + vertical
    r_l[0] = r_l[0] + horizontal

    print('After')
    print(u_d)
    print(r_l)

    if keys[pygame.K_w]:
        vertical = - 15
        horizontal = 0
    elif keys[pygame.K_s]:
        vertical = + 15
        horizontal = 0
    elif keys[pygame.K_a]:
        vertical = 0
        horizontal = - 15
    elif keys[pygame.K_d]:
        vertical = 0
        horizontal = + 15

    if u_d[0] > 450:
        u_d[0] = 0
    elif u_d[0] < - 0:
        u_d[0] = 450
    elif r_l[0] > 600:
        r_l[0] = 0
    elif r_l[0] < 0:
        r_l[0] = 600

    black_screen.update()
    black_surface.fill(BLACK)

pygame.quit()
