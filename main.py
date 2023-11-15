import pygame
import random
import math

# Initialize Pygame
pygame.init()
pygame.mixer.init()

sounds = {
    '1': pygame.mixer.Sound('collision1.wav'),
    '2': pygame.mixer.Sound('collision2.wav'),
    '3': pygame.mixer.Sound('collision3.wav'),
    '4': pygame.mixer.Sound('collision4.wav'),
    '5': pygame.mixer.Sound('collision5.wav'),
    '6': pygame.mixer.Sound('collision6.wav'),
    '7': pygame.mixer.Sound('collision7.wav')
}

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Square class
class Square:
    def __init__(self, size=100, x=WIDTH // 2, y=HEIGHT // 2):
        self.size = size
        self.color = random_color()
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = random.randint(0, 360)

    def move(self):
        radians = math.radians(self.direction)
        self.x += self.speed * math.cos(radians)
        self.y -= self.speed * math.sin(radians)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def check_collision(self):
        if self.x <= 0 or self.x + self.size >= WIDTH or self.y <= 0 or self.y + self.size >= HEIGHT:
            return True
        return False

# Create a list of squares
squares = [Square()]

# Loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move check collisions for square
    for square in squares[:]:  # Iterate over *COPY* of the list
        square.move()
        if square.check_collision():
            squares.remove(square)
            
            # Select sound based on speed
            
            if square.size > 50:
                sound = sounds['1']
            elif square.size <= 50:
                sound = sounds['2']
            elif square.size <= 35:
                sound = sounds['3']
            elif square.size <= 17:
                sound = sounds['4']
            elif square.size <= 9:
                sound = sounds['5']
            elif square.size <= 3 and square.size > 1:
                sound = sounds['6']
            else:
                sound = sounds['7']

            sound.play()
            
            print(square.size)
            
            if (square.size * 0.7 > 1):
                squares.append(Square(size=square.size * 0.7, x=WIDTH // 2, y=HEIGHT // 2))
                squares.append(Square(size=square.size * 0.7, x=WIDTH // 2, y=HEIGHT // 2))
            else:
                squares.append(Square(size= 1, x=WIDTH // 2, y=HEIGHT // 2))
                squares.append(Square(size= 1, x=WIDTH // 2, y=HEIGHT // 2))
        
        square.draw(screen)

    # Redraw
    screen.fill((0, 0, 0))
    for square in squares:
        square.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()