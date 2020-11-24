import pygame
WIDTH = 800
HEIGHT = 800
FPS = 30
# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption( "Grid" )
clock = pygame.time.Clock()
white = [ 255 , 255 , 255 ]
black = [ 0 , 0 , 0 ]
screen.fill(white)
pygame.display.update()
running = True
while running:
	# keep running at the at the right speed
	clock.tick(FPS)
	# process input (events)
	for event in pygame.event.get():
	# check for closing the window
		if event.type == pygame.QUIT:
			running = False
	
	pygame.draw.line(screen, (0, 0, 0), (25, -5), (25, -35), 18)
