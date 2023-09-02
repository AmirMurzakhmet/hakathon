import pygame
import random

# Initialize pygame
pygame.init()


# Set up display
screen_width = 300
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Omnom Eating Game")

    

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player
player_width = 200
player_height = 200
player = pygame.image.load("omnom.png") 
player = pygame.transform.scale(player, (player_width, player_height))
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10

# Candy
candy_width = 60
candy_height = 60
candy_speed = 2
candys = []


def spawn_candy():
    x = random.randint(0, screen_width - candy_width)
    candys.append([x, 0])

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player position based on mouse
    player_x, _ = pygame.mouse.get_pos()

    # Move balloons
    new_candys = []
    for candy in candys:
        candy[1] += candy_speed
        if candy[1] < screen_height:
            new_candys.append(candy)
    candys = new_candys

    # Check for collisions
    for candy in candys:
        if (
            player_x < candy[0] + candy_width
            and player_x + player_width > candy[0]
            and player_y < candy[1] + candy_height
            and player_y + player_height > candy[1]
        ):
            candys.remove(candy)
            score += 1

    # Spawn new balloons
    if random.random() < 0.02:  # Adjust the probability to control balloon spawn rate
        spawn_candy()

    # Draw everything
    screen.fill(white)
    screen.blit(player, (player_x, player_y))
    for candy in candys:
        pygame.draw.ellipse(screen, red, (candy[0], candy[1], candy_width, candy_height))
    
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (15, 15))

    pygame.display.update()

    clock.tick(60)
