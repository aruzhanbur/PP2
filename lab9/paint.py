import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
w = 800
h = 600
active_size = 0
active_color = (255, 255, 255)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint")
painting = []

def draw_menu():
    pygame.draw.rect(screen, (128, 128, 128), [0, 0, w, 80])
    pygame.draw.line(screen, (100, 100, 100), (0, 80), (w, 80), 3)
    xl_brush = pygame.draw.rect(screen, (0, 0, 0), [10, 10, 50, 50])
    pygame.draw.circle(screen, (255, 255, 255), (35, 35), 21)
    l_brush = pygame.draw.rect(screen, (0, 0, 0), [70, 10, 50, 50])
    pygame.draw.circle(screen, (255, 255, 255), (95, 35), 15)
    m_brush = pygame.draw.rect(screen, (0, 0, 0), [130, 10, 50, 50])
    pygame.draw.circle(screen, (255, 255, 255), (155, 35), 10)
    s_brush = pygame.draw.rect(screen, (0, 0, 0), [190, 10, 50, 50])
    pygame.draw.circle(screen, (255, 255, 255), (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    blue = pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [w- 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [w - 60, 35, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [w - 85, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [w - 85, 35, 25, 25])
    color_list = [blue, red, green, black, yellow, white]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0), (255, 255, 0), (255, 255, 255)]

    return brush_list, color_list, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
run = True
while run:
    timer.tick(fps)
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    leftclick = pygame.mouse.get_pressed()[0]
    if mouse[1] > 80:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    if leftclick and mouse[1] > 80:
        painting.append((active_color, mouse, active_size))
    draw_painting(painting)
    brushes, colors, rgbs = draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    pygame.display.flip()
pygame.quit()
