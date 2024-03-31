import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    eraser_mode = False
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_e:  # Toggle eraser mode
                    eraser_mode = not eraser_mode
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    mode = 'custom'  # Switch to custom color selection
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not eraser_mode: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3 and not eraser_mode: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list if not in eraser mode
                if not eraser_mode:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                else:
                    # If in eraser mode, remove points within the eraser radius
                    position = event.pos
                    for p in points:
                        if (p[0] - position[0])**2 + (p[1] - position[1])**2 <= radius**2:
                            points.remove(p)
        
        # Custom color selection
        if mode == 'custom':
            if pressed[pygame.K_1]:  # Select red
                mode = 'red'
            elif pressed[pygame.K_2]:  # Select green
                mode = 'green'
            elif pressed[pygame.K_3]:  # Select blue
                mode = 'blue'
        
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'custom':
        # You can add more custom colors here
        color = (255, 255, 0)  # Yellow
    
    if color_mode == 'eraser':
        color = (0, 0, 0)  # Set color to background color for erasing
        
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()



