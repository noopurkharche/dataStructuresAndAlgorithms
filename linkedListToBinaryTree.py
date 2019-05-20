# Python program to create a Complete Binary Tree from 
# its linked list representation 
  
# Linked List node 
class ListNode: 
  
        # Constructor to create a new node 
        def __init__(self, data): 
            self.data = data 
            self.next = None
  
# Binary Tree Node structure 
class BinaryTreeNode: 
    
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Class to convert the linked list to Binary Tree 
class Conversion: 
  
    # Constructor for storing head of linked list 
    # and root for the Binary Tree 
    def __init__(self, data = None): 
        self.head = None
        self.root = None
  
    def push(self, new_data): 
  
        # Creating a new linked list node and storing data 
        new_node = ListNode(new_data) 
  
        # Make next of new node as head 
        new_node.next = self.head 
  
        # Move the head to point to new node 
        self.head = new_node
        
        
    def convert2BinaryTree(self):
        
        # 10 - 12 - 15 - 25 - 30 - 36
        q = []
        
        if self.head is None:
            self.root = None
            return
        
        # create the root node of the tree
        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)
        p = self.head.next
        
        # while queue is not empty 
        while (p is not  None):
            
            # get the first node from
            parent = q.pop(0)
            
            leftChild = None
            rightChild = None
            
            # create the leftchild of the tree
            print(p.data)
            leftChild = BinaryTreeNode(p.data)
            
            # push it to the queue
            q.append(leftChild)
            p = p.next
            
            if p:
                print(p.data)
                # create the leftchild of the tree
                rightChild = BinaryTreeNode(p.data)
                # push it to the queue
                q.append(rightChild)
                p = p.next
                
            # link parent node to the left and right child
            parent.left = leftChild
            parent.right = rightChild
            
            
    def inorderTraversal(self, root): 
        if(root): 
            self.inorderTraversal(root.left) 
            print(root.data) 
            self.inorderTraversal(root.right) 
            
# Driver Program to test above function 
  
# Object of conversion class 
conv = Conversion() 
conv.push(36) 
conv.push(30) 
conv.push(25) 
conv.push(15) 
conv.push(12) 
conv.push(10) 
  
conv.convert2BinaryTree() 
#conv.convertList2Binary()  
print("Inorder Traversal of the contructed Binary Tree is:")
conv.inorderTraversal(conv.root) 
