from binarytree import Node, show
import numpy.random as nprnd
from collections import deque

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
				if self.left is None:
					return False
				else:
					return self.left.exists(value_toSearchFor)
			elif self.value < value_toSearchFor:
				if self.right is None:
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
	
	def is_root(self):
		return self.parent is None

	def is_right_child(self):
		if self.is_root(): return False
		return self.value >= self.parent.value
	def is_left_child(self):
		if self.is_root(): return False
		return self.value < self.parent.value



	def left_rotate(self):
		print "Starting Left Rotation"

		#check to see if you can actually do the rotation
		# check for null parent
		if self.is_root() or self.is_right_child():
			return
		#assign all the variable you'll be using
		pivot = self
		parent_of_pivot = self.parent
		left_of_pivot = self.left
		# can only rotate a right child
		if self.is_left_child():
			parent_of_pivot =pivot
			pivot.left = parent_of_pivot
			parent_of_pivot.right = left_of_pivot
			left_of_pivot.parent = parent.right
			# The paren'ts left child because the right child of the pivot
			# Pivot becomes the parent's parent
		print "Done with Left Roatation"
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


	def test_rotate(self):
		if self.root is None or self.root.right is None:
			return
		
		self.root.right.left_rotate()

	def print_level_order(self):
		if self.root is None:
			return
		queue.deque()
		queue.append(self.root)
		while len(queue) !=0:
			current_node = queue.popleft()
			print current_node.value
			if current_node.left is not None:
				queue.append(current_node.left)
			if current_node.right is not None:
				queue.append(current_node.right)
def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
for i in random_numbers(10):
    tree.add(i)

# print tree.exists(199);
show(tree.root)
# print tree.height();
tree.test_rotate()
show(tree.root);