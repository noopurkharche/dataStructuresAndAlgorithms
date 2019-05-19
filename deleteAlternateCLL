# Python program to demonstrate 
# circular linked list traversal 
# Delete Alternate from Circular Linked List

# Structure for a Node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class CircularLinkedList: 
	
	# Constructor to create a empty circular linked list 
	def __init__(self): 
		self.head = None

	# Function to insert a node at the beginning of a 
	# circular linked list 
	def push(self, data): 
		ptr1 = Node(data) 
		temp = self.head 
		
		ptr1.next = self.head 

		# If linked list is not None then set the next of 
		# last node 
		if self.head is not None: 
			while(temp.next != self.head): 
				temp = temp.next
			temp.next = ptr1 

		else: 
			ptr1.next = ptr1 # For the first node 

		self.head = ptr1 

	# Function to print nodes in a given circular linked list 
	def printList(self): 
		temp = self.head 
		if self.head is not None: 
			while(True): 
				print("%d" %(temp.data)) 
				temp = temp.next
				if (temp == self.head): 
					break
	
	# Function to delete alternate nodes in a given circular linked list
	def removeAlternate(self):
	    temp = self.head
	    
	    if self.head is not None:
	        while (True):
	            #print("Current - " + str(temp.data))
	            #print("To be Delete - " + str(temp.next.data))
	            #print("New Next - " + str(temp.next.next.data))
	            temp.next = temp.next.next
	            
	            temp = temp.next
	            print("New Current - " + str(temp.data))
	            if temp.next == self.head or temp == self.head:
	                break


# Driver program to test above function 

# Initialize list as empty 
cllist = CircularLinkedList() 

# Created linked list will be 11->2->56->12 
cllist.push(12) 
cllist.push(56) 
cllist.push(2) 
cllist.push(11) 
cllist.push(10) 
print("Contents of circular Linked List")
cllist.printList() 
cllist.removeAlternate()
print("Contents of After alternate delete circular Linked List")
cllist.printList()
