class Edge:

	def __init__(self, point_1, point_2, edge_type):
		self.point_1 = point_1 ##Point 1 and point2 are touples or x,y coordinates
		self.point_2 = point_2
		self.edge_type = edge_type ## 0 represents boundary edge, 1 represents intrnal edge