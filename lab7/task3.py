import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Moving circle")

x = 200
y = 200

v = 20
run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= v
    
    if keys[pygame.K_RIGHT] and x < 775:
        x += v

    if keys[pygame.K_UP] and y > 0:
        y -= v

    if keys[pygame.K_DOWN] and y < 475:
        y += v

    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)  
    pygame.display.update()

pygame.quit()