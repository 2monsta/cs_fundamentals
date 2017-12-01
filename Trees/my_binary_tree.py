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

	def height(self):
		if self.left is None and self.right is None:
			return 1
		left_subtree_height = 0
		right_subtree_height =0
		if self.left is not None:
			left_subtree_height = self.left.height()
		if self.right is not None:
			right_subtree_height = self.right.height()

		if left_subtree_height > right_subtree_height:
			return left_subtree_height +1
		else:
			return right_subtree_height +1
			

# three ways to process the tree
# in order : left self right
# post order: left right self
# pre order: self left right

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

	def height(self):
		if self.root is not None:
			return self.root.height()
		return 0
	def print_in_order(self):
		if self.left is not None:
			self.left.print_in_order()

		# print self and print right tree
		print self.value
		if self.right is not None:
			self.print_in_order()

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
for i in random_numbers(10):
	tree.add(i)

print tree.exists(199);
show(tree.root)
print tree.height();