import pygame
import sys
from card import Card
from keypress import key_press_manager 
from pygame.math import Vector2 as v2
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
BLACK = (0, 0, 0)

# Screen setup

# Clock for controlling the frame rate
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.running = True  # This will control the game loop
        self.keypress = []
        self.keypress_held_down = []
        self.mouse_pos = [0,0]
        self.v2 = v2
        self.active = False
        self.activeNode = None
        self.font = pygame.font.Font("agencyb.ttf", 20)
        self.clicked = None
        self.turnsPassed = 10
        self.cardInstance = Card
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Pygame Base Template")

        
        self.card = Card(self)
        
        
        
    def update(self):
        key_press_manager(self)
    
    def draw(self):
        # Fill the screen with black (or any other background color)
        self.screen.fill(BLACK)

        if "space" in self.keypress:
            self.card.nodeListIndex = (self.card.nodeListIndex + 1) % len(self.card.nodeListKeys)

        t = self.font.render(f"Page: {self.card.nodeListKeys[self.card.nodeListIndex]}", True, [255,255,255])
        self.screen.blit(t, [10, 10])



        self.active = False
        for x in self.card.nodes[self.card.nodeListKeys[self.card.nodeListIndex]]:
            x.render()

        if self.activeNode:
            pygame.draw.line(self.screen, [255,0,0], self.activeNode.pos + self.activeNode.parent.pos, self.mouse_pos)
            if "mouse2" in self.keypress:
                self.activeNode = None

        if self.active and "mouse2" in self.keypress:
            self.DELTA = self.mouse_pos - self.active.pos
            self.clicked = self.active

        if self.clicked and "mouse2" not in self.keypress_held_down:
            self.clicked = None


        if self.clicked and "mouse2" in self.keypress_held_down:
            self.clicked.pos = self.mouse_pos.copy() - self.DELTA
        
        # You can draw game objects here
        pygame.display.update()  # Update the display

    def run(self):
        # Main game loop
        while self.running:

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
