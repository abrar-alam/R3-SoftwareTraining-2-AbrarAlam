from grid import Grid
from maze_generator import MazeGenerator
import pygame

screen = pygame.display.set_mode((640, 480))
running = 1
white = [255, 255, 255]
black = [0, 0, 0]

myGrid = Grid((8, 8))
myGrid.create_grid((8, 8))
myMaze = MazeGenerator(myGrid)
myMaze.processGrid()  # Our maze is now fully initialized

num_of_rows = len(myGrid.list_of_rows)
num_of_cols = len(myGrid.list_of_rows[0])

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill(white)

    for i in range(0, num_of_rows):
        for j in range(0, num_of_cols):
            if(myMaze.mazedGrid.list_of_rows[i][j].top_edge is not None):
                # Draw top edges of this cell
                pygame.draw.line(
                    screen, black, myGrid.list_of_rows[i][j].top_edge.point_1, myGrid.list_of_rows[i][j].top_edge.point_2)
            if(myMaze.mazedGrid.list_of_rows[i][j].bottom_edge is not None):
                # draw bottom edge of this cell
                pygame.draw.line(
                    screen, black, myGrid.list_of_rows[i][j].bottom_edge.point_1, myGrid.list_of_rows[i][j].bottom_edge.point_2)
            if(myMaze.mazedGrid.list_of_rows[i][j].right_edge is not None):
                # Draw right edge
                pygame.draw.line(
                    screen, black, myGrid.list_of_rows[i][j].right_edge.point_1, myGrid.list_of_rows[i][j].right_edge.point_2)
            if(myMaze.mazedGrid.list_of_rows[i][j].left_edge is not None):
                pygame.draw.line(
                    screen, black, myGrid.list_of_rows[i][j].left_edge.point_1, myGrid.list_of_rows[i][j].left_edge.point_2)

    pygame.display.flip()
