import pygame
############################ BREAKOUT ##############################################
#####Screen size ocnstant
SCREEN_SIZE = 640 , 480
####################################################################################
#####Game object
class Game(object):
   
    def main(self,screen):
        image = pygame.image.load('bird.png')
        image_x = 320
        image_y = 240

        clock = pygame.time.Clock()
        while 1:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            image_x += 10
            screen.fill((200,200,200))
            screen.blit(image,(320,240))
            screen.blit(image,(image_x,image_y))
            pygame.display.flip()
##################################################################################
if __name__ == '__main__':
    #initialize pygame
    pygame.init()
    #display screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    Game().main(screen)
