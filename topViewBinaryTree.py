# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict = collections.defaultdict(list)
        queue = [(root,0,0)]
        while(queue):
            
            for i in range(len(queue)):
                node,hd,vd = queue.pop(0)
                dict[hd].append((vd,node.val))
                if node.left:
                    queue.append((node.left,hd-1,vd-1))
                if node.right:
                    queue.append((node.right,hd+1,vd-1))
        print(dict)
        result = []
        for i in sorted(dict.keys()):
            level=[x[1] for x in sorted(dict[i],key=lambda x:(-x[0],x[1]))] 
            result.append(level[0])
        return result
        
