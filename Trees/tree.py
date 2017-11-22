class myTreeNode:
	def __init__(self, value):
		self.value = value
		self.array = []
		self.parent = None
	def add_Child(self, child_node):
		self.array.append(child_node)
		child_node.parent = self
	def remove_child(self, child_node):
		del self.array[self.array.indexof(child_node)]


root = myTreeNode(5)
root.add_Child(myTreeNode(10));

for child in root.array:
	print child.value

# Binary Tree
# - one path to each node,
# - only two children