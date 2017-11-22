from binarytree import Node, show
import numpy.random as nprnd
class myTreeNode(Node):
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
	def add(self, new_node):
		if new_node.value >= self.value:
			if self.right is None:
				self.right = new_node
				new_node.parent = self
			else:
				self.right.add(new_node)
		else:
			if self.left is None:
				self.left = new_node
				new_node.parent = self
			else:
				self.left.add(new_node)
	def exists(self, value_toSearchFor):
		if self.value == value_toSearchFor:
			return True
		else:
			if self.value > value_toSearchFor:
				if(self.left is None):
					return False
				else:
					return self.left.exists(value_toSearchFor)
			elif self.value < value_toSearchFor:
				if(self.right is None):
					return False
				else:
					return self.right.exists(value_toSearchFor)
			
class BST:
	def __init__(self):
		self.root = None
	def add(self, value):
		new_node = myTreeNode(value)
		if self.root is None:
			self.root=new_node
		else:
			self.root.add(new_node)
	def exists(self, value):
		# return true if the value exists in the tree
		# return false if it doesnt exist in the tree
		if self.root is None:
			return False
		else:
			return self.root.exists(value)



def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
for i in random_numbers(10):
	tree.add(i)

print tree.exists(199);
show(tree.root)