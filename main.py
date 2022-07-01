import time
import sys
import pygame

class TrafficLight:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (252, 252, 252)
        self.RED = (255, 0, 0)
        self.RED_DARK = (249, 169, 183)
        self.YELLOW = (255, 255, 0)
        self.YELLOW_DARK = (244, 244, 128)
        self.GREEN = (0, 255, 0)
        self.GREEN_DARK = (161, 232, 175)

    def switch_color(self, color1, color2, x, y, radius):
        #pygame.draw.circle(self.screen, self.RED_DARK, (320, 140), 40)

        pygame.draw.circle(self.screen, color1, (x, y), radius)
        time.sleep(2)
        pygame.draw.circle(self.screen, color2, (x, y), radius)
        # time.sleep(1)

    def on(self):
        timing = 3
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.WHITE)
            pygame.draw.rect(self.screen, self.BLACK, (270, 90, 100, 280), 2)


            #self.switch_color(self.RED, self.RED_DARK, 320, 140, 40)
            pygame.draw.circle(self.screen, self.RED, (320, 140), 40)
            pygame.time.wait(1000)
            pygame.draw.circle(self.screen, self.RED_DARK, (320, 140), 40)


            # pygame.draw.circle(self.screen, self.RED_DARK, (320, 140), 40)
            # pygame.draw.circle(self.screen, self.YELLOW_DARK, (320, 230), 40)
            # pygame.draw.circle(self.screen, self.GREEN_DARK, (320, 320), 40)

            pygame.display.update()

        pygame.quit()



tl = TrafficLight()
tl.on()
