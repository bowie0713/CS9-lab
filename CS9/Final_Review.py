# Add item into Ordered Linked List
def add(self, item):
	current = item
	previous = None
	stop = False

	
	while current != None and not stop:
		if current.getData() > item:
			stop = True
		else:
			previous = current
			current = current.getNext()


	temp = Node(item)

	
	if previous == None:
		temp.setNext(self.head)
		self.head = temp
	else: # Case 2: insert not at front of list
		temp.setNext(current)
		previous.setNext(temp)
		
d
