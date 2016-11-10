import pygame,sys
from pygame.locals import *
import simplejson

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Twitter')

background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((250,250,250))

font = pygame.font.Font(None,16)
text=font.render("Test window",1,(10,10,10))  #text color
textpos=text.get_rect()
textpos.centerx=background.get_rect().centerx
background.blit(text, textpos)

screen.blit(background,(0,0))
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background,(0,0))
	pygame.display.flip()
	