from random import seed
from random import randint
from random import choice
from edge import Edge
from cell import Cell
from grid import Grid

class MazeGenerator:
	def __init__(self, full_grid): # constructor takes a Grid object with all cells initiazed
		self.mazedGrid = full_grid # This IV must be proceesed by a grid processor method to make it a maze
		self.visitedCells = [] # This stores the (row num, colnum) tuple location of the visited cells.

	def processGrid(self):
		randomCell = self.selectRandomCell(self) # first we select a random startting cell's coordinate
		# Extract the row and col no.
		currentRow = randomCell[0] # These must be updated during loop, cuz, we store these as tuple in the visited cell array
		currentCol = randomCell[1] # These must be updated during loop, cuz, we store these as tuple in the visited cell array
		
		# We extract our current cell object
		currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol]
		#Edge ids below:
		#Top edge ~ 0, bottom edge ~ 1, right edge ~ 2, left edge ~ 3

		#while the lenth of visted cell list is not n*n, we iterate
		while(len(self.visitedCells) != (self.mazedGrid.num_of_rows * self.mazedGrid.num_of_rows)):
			validEdgeList = [] # this will store our edge ids (legal edges) surrounding our current cell
			#top edge varification 
			if (self.checkValidTopEdge(currentRow, currentCol) == 1): # a source of bug. modify the method sd ot takes the co-ordinate
				validEdgeList.append(0)

			if (self.checkValidBottomEdge(currentRow, currentCol) == 1):
				validEdgeList.append(1)

			if (self.checkValidRightEdge(currentRow, currentCol) == 1):
				validEdgeList.append(2)

			if (self.checkValidLeftEdge(currentRow, currentCol) == 1):
				validEdgeList.append(3)

			if (len(validEdgeList) == 0): # We go hunting if we are at deadend
				#We update the our current cell as visited
				#self.visitedCells.append((currentRow, currentCol)) # We store our current cell's row and col # in the visited cell

				currentCell, currentRow, currentCol = self.huntTheCell(self) # a method we will define later, this will 
													#return a cell if found, otherwise return None	
				if (currentCell is None): # Means no more unvisited cell is found
					continue # This implicitly means we are terminating this method, and done
							# The condition in our while makes sure that we end here.
				else:

					self.visitedCells.append((currentRow, currentCol))
					continue	
			else:
				#Now we randomly select a valid edge to cross and update edge as None which was crossed
				# Then we update our currentCell variable
				seed()
				edgeToCarveID = choice(validEdgeList) # We now have the ID of edge such as top/bottom/left/right which we will break
													# and discover new unvisited cell
				if(edgeToCarveID == 0): #if we have a top edge to break
					currentCell.top_edge = None #here we mark our edge to be broken

					#Now we ipdate our current location
					currentRow = currentRow - 1
					currentCol = currentCol

					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					currentCell.bottom_edge = None # we do this because our actual edge objects were different, although they have the 
													# same co-ordinates. Not doing this will never mark the crossed cell as none
													# For example first we broke our current cell's top edge. But the cell we are about 
													#to move into has its bottom cell object not set to null. Thats what we are doping here
					# now we update our visited cell list
					self.visitedCells.append((currentRow, currentCol))

				if(edgeToCarveID == 1): #if we have a bottom edge to break
					currentCell.bottom_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow + 1
					currentCol = currentCol
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					currentCell.top_edge = None 
					# now we update our visited cell list
					self.visitedCells.append((currentRow, currentCol))

				if(edgeToCarveID == 2): #if we have a right edge to break
					currentCell.right_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow 
					currentCol = currentCol + 1
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					currentCell.left_edge = None 
					# now we update our visited cell list
					self.visitedCells.append((currentRow, currentCol))

				if(edgeToCarveID == 3): #if we have a left edge to break
					currentCell.left_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow 
					currentCol = currentCol - 1
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					currentCell.right_edge = None 
					# now we update our visited cell list
					self.visitedCells.append((currentRow, currentCol))






	# Helper methods
	def checkValidTopEdge (self,row_num, col_num):
		if(self.mazedGrid.list_of_rows[row_num][col_num].top_edge is None):
			return 0
		elif(self.mazedGrid.list_of_rows[row_num][col_num].top_edge.edge_type == 0):
			return 0
		elif((row_num-1,col_num) in self.visitedCells):
			return 0
		else:
			return 1
			
				
			


	def checkValidBottomEdge(self,row_num, col_num):
		if(self.mazedGrid.list_of_rows[row_num][col_num].bottom_edge is None):
			return 0
		elif(self.mazedGrid.list_of_rows[row_num][col_num].bottom_edge.edge_type == 0):
			return 0
		elif((row_num+1,col_num) in self.visitedCells):
			return 0
		else:
			return 1
		
	def checkValidRightEdge(self,row_num, col_num):
		if(self.mazedGrid.list_of_rows[row_num][col_num].right_edge is None):
			return 0
		elif(self.mazedGrid.list_of_rows[row_num][col_num].right_edge.edge_type == 0):
			return 0
		elif((row_num,col_num+1) in self.visitedCells):
			return 0
		else:
			return 1

	def checkValidLeftEdge(self,row_num, col_num):
		if(self.mazedGrid.list_of_rows[row_num][col_num].left_edge is None):
			return 0
		elif(self.mazedGrid.list_of_rows[row_num][col_num].left_edge.edge_type == 0):
			return 0
		elif((row_num,col_num-1) in self.visitedCells):
			return 0
		else:
			return 1
		

	def selectRandomCell(self):
		seed(1)

		#for _ in range(len(self.mazedGrid.list_of_rows)):
		value = randint(0, len(self.mazedGrid.list_of_rows) - 1)
		print(value)
		return((value, value))

	def huntTheCell(self):
		#resume
		for i in range(0, self.mazedGrid.num_of_rows):
			for j in range (0, self.mazedGrid.num_of_cols):
				if((i,j) not in self.visitedCells): # This guarantees we wont have null pointer exception
					# Now we carve the edge between our newly discovered cell and a neighbouring visited cell

					#check top 
					if ((self.mazedGrid.list_of_rows[i][j].top_edge is not None) and (self.mazedGrid.list_of_rows[i][j].top_edge.edge_type == 1)):
						if ((i-1, j) in self.visitedCells):
							self.mazedGrid.list_of_rows[i][j].top_edge = None 
							self.mazedGrid.list_of_rows[i-1][j].bottom_edge = None # We have now completed the carving
							return self.mazedGrid.list_of_rows[i][j], i, j
					#check bottom 
					if ((self.mazedGrid.list_of_rows[i][j].bottom_edge is not None) and (self.mazedGrid.list_of_rows[i][j].bottom_edge.edge_type == 1)):
						if ((i+1, j) in self.visitedCells):
							self.mazedGrid.list_of_rows[i][j].bottom_edge = None 
							self.mazedGrid.list_of_rows[i+1][j].top_edge = None # We have now completed the carving
							return self.mazedGrid.list_of_rows[i][j], i, j
					#check right
					if ((self.mazedGrid.list_of_rows[i][j].right_edge is not None) and (self.mazedGrid.list_of_rows[i][j].right_edge.edge_type == 1)):
						if ((i, j+1) in self.visitedCells):
							self.mazedGrid.list_of_rows[i][j].right_edge = None 
							self.mazedGrid.list_of_rows[i][j+1].left_edge = None # We have now completed the carving
							return self.mazedGrid.list_of_rows[i][j], i, j
					#check left
					if ((self.mazedGrid.list_of_rows[i][j].left_edge is not None) and (self.mazedGrid.list_of_rows[i][j].left_edge.edge_type == 1)):
						if ((i, j-1) in self.visitedCells):
							self.mazedGrid.list_of_rows[i][j].left_edge = None 
							self.mazedGrid.list_of_rows[i][j-1].right_edge = None # We have now completed the carving
							return self.mazedGrid.list_of_rows[i][j], i, j
				
		return None,None,None

	def giveVisitedNeighbour(self, loc_of_unv_cell):
		


