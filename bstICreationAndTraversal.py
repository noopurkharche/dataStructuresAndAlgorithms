class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def insertIntoBST(root, node):
    # if root is None create 
    if root is None:
        root = node
        return
    else:
        if root.val < node.val:
            # check if right is None then insert to the right
            if root.right is None:
                root.right = node
            else:
                insertIntoBST(root.right, node)
        else:
            # check if right is None then insert to the right
            if root.left is None:
                root.left = node
            else:
                insertIntoBST(root.left, node)
    return
    
# postorder traversal of he tree iterative
def postorderIterative(root):
        
    stack1 = [root]
    stack2 = []
        
    while len(stack1) != 0:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        
    while len(stack2) != 0:
        print(stack2.pop().val)

def preorderIterative( root):
    traversalList = []
    stack = []
    stack.append(root)
    while (len(stack) > 0):
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def inorderIterative(root):
    stack = []
    while True:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            if len(stack) == 0:
                break
            else:
                root = stack.pop()
                print(root.val)
                root = root.right

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50) 
insertIntoBST(r,Node(30)) 
insertIntoBST(r,Node(20)) 
insertIntoBST(r,Node(40)) 
insertIntoBST(r,Node(70)) 
insertIntoBST(r,Node(60)) 
insertIntoBST(r,Node(80))

print("----------Inorder Recursive-----------")
inorder(r)
print("----------Postorder Iterative-----------")
postorderIterative(r)
print("----------Preorder Iterative-----------")
preorderIterative(r)
print("----------Inorder Iterative-----------")
inorderIterative(r)


