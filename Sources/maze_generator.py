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
			if (self.checkValidTopEdge(currentCell.top_edge) == 1):
				validEdgeList.append(0)

			if (self.checkValidBottomEdge(currentCell.bottom_edge) == 1):
				validEdgeList.append(1)

			if (self.checkValidRightEdge(currentCell.right_edge) == 1):
				validEdgeList.append(2)

			if (self.checkValidLeftEdge(currentCell.left_edge) == 1):
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
					# now we update our visited cell list
					self.visitedCells.append(currentCell)

				if(edgeToCarveID == 1): #if we have a bottom edge to break
					currentCell.bottom_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow + 1
					currentCol = currentCol
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					# now we update our visited cell list
					self.visitedCells.append(currentCell)

				if(edgeToCarveID == 2): #if we have a right edge to break
					currentCell.right_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow 
					currentCol = currentCol + 1
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					# now we update our visited cell list
					self.visitedCells.append(currentCell)

				if(edgeToCarveID == 3): #if we have a left edge to break
					currentCell.left_edge = None #here we mark our edge to be broken
					#Now we ipdate our current location
					currentRow = currentRow 
					currentCol = currentCol - 1
					currentCell = self.mazedGrid.list_of_rows[currentRow][currentCol] #its our newly reached cell
					# now we update our visited cell list
					self.visitedCells.append(currentCell)






	# Helper methods
	def checkValidTopEdge (self,topside):
		if(topside is None):
			return 0
		elif(topside.edge_type == 0):
			return 0
		else:
			for i in range(0, len(self.visitedCells)):
				if (topside.point_1 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].bottom_edge.point_1\
					and topside.point_2 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].bottom_edge.point_2):
					return 0
			return 1 


	def checkValidBottomEdge(self,downside):
		if(downside is None):
			return 0
		elif(downside.edge_type == 0):
			return 0
		else:
			for i in range(0, len(self.visitedCells)):
				if (downside.point_1 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].top_edge.point_1\
					and downside.point_2 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].top_edge.point_2):
					return 0
			return 1 
		
	def checkValidRightEdge(self,rightside):
		if(rightside is None):
			return 0
		elif(rightside.edge_type == 0):
			return 0
		else:
			for i in range(0, len(self.visitedCells)):
				if (rightside.point_1 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].left_edge.point_1\
					and rightside.point_2 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].left_edge.point_2):
					return 0
			return 1 
	def checkValidLeftEdge(self, leftside):
		if(leftside is None):
			return 0
		elif(leftside.edge_type == 0):
			return 0
		else:
			for i in range(0, len(self.visitedCells)):
				if (leftside.point_1 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].right_edge.point_1\
					and leftside.point_2 == self.mazedGrid.list_of_rows[visitedCells[i][0]][visitedCells[i][1]].right_edge.point_2):
					return 0
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
				if (((i,j) is not in self.visitedCells) and (self.giveVisitedNeighbour((i,j)) is not None)):
					return self.mazedGrid.list_of_rows[i][j], i, j # we are returning the cell, and its row and col #
		return None,None,None

	def giveVisitedNeighbour(self, loc_of_unv_cell):
		


