# method to find the lowest common ancestor for the two nodes    
# @para[in] : n1,n2 these are the nodes for which lca is to be found
# #para[in] : root is root node
def lowestCommonAncestor(n1,n2, root):
    
    if root == None:
        return None

    if root == n1 or root == n2:
        return root
        
    leftChild = lowestCommonAncestor(n1,n2, root.left)
    rightChild = lowestCommonAncestor(n1,n2,root.right)
    
    # if both are None return None
    if leftChild == None and rightChild == None:
        return None
    
    # if both are not None then this node (root i.e parent)  is the Lowest Common Ancestor
    if leftChild != None and rightChild != None:
        return root
        
    # if any one is None return value accordingly
    if leftChild is not None:
        return leftChild
    else:
        return rightChild

