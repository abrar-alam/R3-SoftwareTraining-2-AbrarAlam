from edge import Edge
from cell import Cell
from grid import Grid
import pygame

screen = pygame.display.set_mode((640, 480))
running = 1
white = [ 255 , 255 , 255 ]
black = [ 0 , 0 , 0 ]

myGrid = Grid((8,8))
myGrid.create_grid((8,8))

num_of_rows = len(myGrid.list_of_rows)
num_of_cols = len(myGrid.list_of_rows[0])

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill(white)
	#pygame.draw.line(screen, black , (25, 0), (25, 25))
	#pygame.draw.line(screen, black , (25, 25), (50, 25))
	# pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
	for i in range(0, num_of_rows):
		for j in range(0, num_of_cols):
			pygame.draw.line(screen, black , myGrid.list_of_rows[i][j].top_edge.point_1, myGrid.list_of_rows[i][j].top_edge.point_2)
			pygame.draw.line(screen, black , myGrid.list_of_rows[i][j].bottom_edge.point_1, myGrid.list_of_rows[i][j].bottom_edge.point_2)
			pygame.draw.line(screen, black , myGrid.list_of_rows[i][j].right_edge.point_1, myGrid.list_of_rows[i][j].right_edge.point_2)
			pygame.draw.line(screen, black , myGrid.list_of_rows[i][j].left_edge.point_1, myGrid.list_of_rows[i][j].left_edge.point_2)
	pygame.display.flip()


