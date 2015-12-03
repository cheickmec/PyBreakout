import pygame

#screen size ocnstant
SCREEN_SIZE = 640 , 480
#game object
class Game(object):
    def main(self,screen):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
if __name__ == '__main__':
    #initialize pygame
    pygame.init()
    #display screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    Game().main(screen)
