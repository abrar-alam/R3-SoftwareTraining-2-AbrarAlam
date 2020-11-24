from edge import Edge
from cell import Cell
from grid import Grid

demo_grid = Grid((4,4))
demo_grid.create_grid((4,4))

for row in range(0, len(demo_grid.list_of_rows)):
  for col in range(0, len(demo_grid.list_of_rows[0])):
    print( demo_grid.list_of_rows[row][col].bottom_edge.point_1, demo_grid.list_of_rows[row][col].bottom_edge.point_2)
