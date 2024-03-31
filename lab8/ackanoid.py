import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
initial_paddle_width = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - initial_paddle_width // 2, H - paddleH - 30, initial_paddle_width, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = []
for i in range(10):
    for j in range(4):
        # Randomly choose whether the block is breakable or unbreakable
        is_breakable = random.choice([True, False])
        is_bonus = random.choice([True, False]) if is_breakable else False
        if is_breakable:
            if is_bonus:
                block_list.append((pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), (0, 255, 0), is_breakable, is_bonus))  # Green for bonus blocks
            else:
                block_list.append((pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), is_breakable, is_bonus))
        else:
            block_list.append((pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), (255, 0, 0), is_breakable, is_bonus))  # Red for unbreakable blocks

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Initial paddle width
initial_paddle_width = paddle.width

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # Draw blocks
    for block, color, is_breakable, _ in block_list:
        pygame.draw.rect(screen, color, block)
    
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Increase ball speed over time
    ballSpeed += 0.001  # Adjust the value to control the rate of increase
    
    # Shrink paddle over time
    shrink_rate = 0.05  # Adjust the rate of shrinking
    initial_paddle_width -= shrink_rate
    paddle.width = max(initial_paddle_width, 10)  # Ensure paddle width doesn't go below a certain value
    
    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision with breakable blocks
    for index, (block, _, is_breakable, _) in enumerate(block_list):
        if is_breakable:
            if ball.colliderect(block):
                block_list.pop(index)
                dx, dy = detect_collision(dx, dy, ball, block)
                game_score += 5 if is_bonus else 1  # Increase score by 5 for bonus blocks
                collision_sound.play()
                break  # Exit loop after first collision
    
    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not block_list:
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
    
    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)













