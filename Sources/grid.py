from edge import Edge
from cell import Cell
class Grid:
	def __init__(self, size_of_grid):##size of grid is given as tuple
		self.num_of_rows = size_of_grid[0]
		self.num_of_cols = size_of_grid[1]
		self.list_of_rows = None

	def create_grid (self, size_of_grid):
		x1 = 0
		y1 = 0
		x2 = 0
		y2 = 0

		start = 5 ## Our offset
		wall_length = 20 ## Wal length
		my_list = []

		for i in range(0,size_of_grid[0]): # rpw generation
			row_of_cells = []
			for j in range (0,size_of_grid[1]):# col generation

				top_edge_x1 = start + (j * wall_length)
				top_edge_y1 = start + ((i+1) * wall_length)
				top_edge_x2	= start + ((j+1) * wall_length)
				top_edge_y2	= top_edge_y1

				#Now we instantiate the edges for this cell to be created
				if (i == (size_of_grid[0] -1)):
					top_edge = Edge((top_edge_x1, top_edge_y1), (top_edge_x2, top_edge_y2), 0)  #At top row, out topedge type is 0
				else:
					top_edge = Edge((top_edge_x1, top_edge_y1), (top_edge_x2, top_edge_y2), 1) 
				if (i == 0):
					bottom_edge = Edge((top_edge_x1, top_edge_y1 - wall_length),(top_edge_x2, top_edge_y2 - wall_length), 0) # at first row, bottom edge type is 0
				else:
					bottom_edge = Edge((top_edge_x1, top_edge_y1 - wall_length),(top_edge_x2, top_edge_y2 - wall_length), 1)
				if (j == (size_of_grid[1] -1)):
					right_edge = Edge((top_edge_x2, top_edge_y2 - wall_length), (top_edge_x2, top_edge_y2), 0) #in the last col, rightedge is type 0
				else:
					right_edge = Edge((top_edge_x2, top_edge_y2 - wall_length), (top_edge_x2, top_edge_y2), 1)
				if (j == 0):
					left_edge = Edge((top_edge_x1, top_edge_y1 - wall_length), (top_edge_x1, top_edge_y1), 0)# in first col, left edge is type 0
				else:
					left_edge = Edge((top_edge_x1, top_edge_y1 - wall_length), (top_edge_x1, top_edge_y1), 1)
				# now we add this cell to the list
				row_of_cells.append(Cell(top_edge, bottom_edge, right_edge, left_edge))
			#now we append the entire row of cell
			my_list.append(row_of_cells)
		# now we reverse the order to standardize
		my_list.reverse()
		self.list_of_rows = my_list
			

