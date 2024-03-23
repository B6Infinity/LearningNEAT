import pygame
from pong.Game import Game

TICK = 60

width, height = 800, 600
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)


class PongGame():
    def __init__(self):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self):
                
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(TICK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                game.move_paddle(left=True, up=False)

            game.loop()
            game.draw()

            pygame.display.update()

        pygame.quit()

    # def move_paddle(self, left, up):

