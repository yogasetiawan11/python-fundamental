import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# Tambahkan warna gradasi
BG_TOP = (64, 156, 255)    # Biru muda
BG_BOTTOM = (120, 86, 255) # Ungu muda

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT or
            head in self.body[1:]
        )

def spawn_food(snake_body):
    while True:
        food_pos = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
        if food_pos not in snake_body:
            return food_pos

def draw_text(surface, text, position, size=36, color=WHITE):
    font = pygame.font.Font(None, size)
    rendered = font.render(text, True, color)
    surface.blit(rendered, position)

def draw_background(surface):
    # Gradasi vertikal dari BG_TOP ke BG_BOTTOM
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = spawn_food(snake.body)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        snake.move()

        if snake.check_collision():
            draw_background(screen)
            draw_text(screen, "Game Over!", (WIDTH // 2 - 100, HEIGHT // 2 - 20), 48, RED)
            draw_text(screen, f"Score: {score}", (WIDTH // 2 - 60, HEIGHT // 2 + 30), 36)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        if snake.body[0] == food:
            snake.grow = True
            score += 1
            food = spawn_food(snake.body)

        # Draw everything
        draw_background(screen)

        # Draw food
        pygame.draw.rect(
            screen, RED,
            (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(
                screen, GREEN,
                (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

        # Draw score
        draw_text(screen, f"Score: {score}", (10, 10), 28)

        pygame.display.flip()
        clock.tick(15)  # Slightly faster gameplay

if __name__ == "__main__":
    main()