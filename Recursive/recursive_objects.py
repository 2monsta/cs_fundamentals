class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
	def search(self, value):
		if self.value == value:
			return self
		if self.right is None:
			return None
		return self.right.search(value)

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, value):
        new_node = LinkedListNode(value)

        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.right = new_node
            new_node.left = self.end
            self.end = new_node

    def search(self, value):
		if self.start is None:
			return None
		self.start.search(value)

		# THIS IS THE ORIGINAL
        # current_node = self.start

        # while current_node is not None:
        #     if current_node.value == value:
        #         return current_node

        #     current_node = current_node.right

	def isEmpty(self):
		if self.start is None:
			return True
		else:
			return False

	def remove_last_node(self):
		if self.isEmpty():
			return
		else:
			second_to_last = self.end.left
			second_to_last.right = None
			self.end.left = None

			self.end = second_to_last
			
	def print_all_node_values(self):
		current_node = self.start
		while current_node is not None:
			print current_node.value
			current_node = current_node.right

	def delete_at_index(self, index):
		current_node = self.start
		counter = 0;
		while(current_node is not None):
			counter +=1
			current_node = current_node.right
			if(counter == index):
				left_node = current_node.left
				right_node = current_node.right
				current_node.left = None
				current_node.right = None
				left_node.right = right_node
				right_node.left = left_node
				# current_node is None

			




# def foo(start_count):
# 	print start_count
# 	if start_count == 0:
# 		return
# 	foo(start_count-1)
# foo(10)

ll = LinkedList()
ll.append(10)
ll.start.search(10);


