import pygame
import math
import time

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mickey Mickey")

done = False

clock = pygame.time.Clock()
backim = pygame.image.load("mainclock.png")
backim = pygame.transform.scale(backim, (1000, 800))
minim = pygame.image.load("rightarm.png")
secim = pygame.image.load("leftarm.png")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        t = time.localtime()

        minang = -(360 * (t.tm_min / 60)) + 270
        secang = -(360 * (t.tm_sec / 60)) + 270

        rotated_minim = pygame.transform.rotate(minim, minang)
        rotated_secim = pygame.transform.rotate(secim, secang)
        
        clock.tick(30)
        screen.blit(backim, (0, 0))
        screen.blit(rotated_minim, (screen.get_width() // 2 - rotated_minim.get_width() // 2, 
                                    screen.get_height() // 2 - rotated_minim.get_height() // 2))
        screen.blit(rotated_secim, (screen.get_width() // 2 - rotated_secim.get_width() // 2, 
                                    screen.get_height() // 2 - rotated_secim.get_height() // 2))
        pygame.display.flip()

pygame.quit()