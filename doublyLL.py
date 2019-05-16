
# node class for doubly linked list
class Node:
    def __init__(self,data):
       self.data = data
       self.next = None
       self.prev = None
       
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # insert the new node at the front of the list
    def push(self, data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        # check if head is not None 
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return 
    
    # insert neew node after the given node
    def insertAfter(self, prev_node, data):
        new_node = Node(data)
        new_node.prev = prev_node
        temp = prev_node.next 
        new_node.next = temp
        prev_node.next = new_node
        if temp is not None:
            temp.prev = new_node
        return
    
    # append node at the end 
    def append(self, data): 
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = None
            new_node.prev = None
            return
        
        # Travers to the last node of the doubly LL
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        
        lastNode.next = new_node
        new_node.prev = lastNode
        new_node.next = None
        return
    
    def printDll(self):
        print("--------------------------------")
        current = self.head
        str1 = ""
        while current is not None:
            str1 = str1 + "<- " + str(current.data) + " ->"
            current = current.next
        print(str1)
        
    # insert node after node with given data 
    def insertAfterData(self,data, new_data):
        new_node = Node(new_data)
        #print(new_node.data)
        current = self.head
        
        while current is not None and current.data != data:
            current = current.next
        #print(current.data)
        
        if current is not None:
            temp = current.next
        
        current.next = new_node
        new_node.next = temp
        
        if temp is not None:
            temp.prev = new_node
        
        new_node.next = temp
        new_node.prev = current
        
        return    
                
        
        

l1 = DoublyLinkedList()
l1.append(6)
l1.append(2)
l1.append(1)

# at the start
l1.push(7)

# insert afetr the given node
l1.insertAfter(l1.head, 8)
l1.insertAfterData(6,10)
print(l1.printDll())
    
    
        
    
        
        
        
        
    
