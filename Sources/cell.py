from edge import Edge

class Cell:
	def __init__(self, top_edge, bottom_edge, right_edge, left_edge):
		self.top_edge = top_edge
		self.bottom_edge = bottom_edge
		self.left_edge = left_edge
		self.right_edge = right_edge