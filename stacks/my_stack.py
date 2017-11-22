class myStack:
	def __init__():
		self.stack  = []
	def push(new_element):
		# add new element to the top of the stack
		self.stack.append(new_element);
	def pop():
		# removes the top element and also return it
		element = self.stack[len(self.stack)-1]
		del self.stack[len(self.stack)-1]
		return element
	def peek():
		# return top most element
		return self.stack[-1]

class myQueue:
	def __init__():
		self.queue  = []
	def enqueue(self, new_element):
		self.queue.append(new_element);
	def dequeue(self):
		element = self.queue[0]
		del self.queue[0]
		return element