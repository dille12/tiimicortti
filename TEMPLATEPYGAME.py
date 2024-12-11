import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Base Template")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.running = True  # This will control the game loop
        self.pressed = []
        self.mousepos = [0,0]
        
    def handle_mouse_events(self, event):
        # Handle mouse button events here
        self.pressed.clear()
        self.mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                self.pressed.append("m1")
            elif event.button == 3:  # Right mouse button
                self.pressed.append("m2")

        if self.pressed:
            print(self.pressed)
        
    def update(self):
        # Game logic updates go here
        pass
    
    def draw(self):
        # Fill the screen with black (or any other background color)
        screen.fill(BLACK)
        
        # You can draw game objects here
        pygame.display.update()  # Update the display

    def run(self):
        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_mouse_events(event)

            self.update()  # Update game logic
            self.draw()    # Render game objects
            
            # Cap the frame rate at 60 FPS
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
