# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def tra(nodep, nodeq):
            #print(nodep.val, nodeq.val)
            if nodep==None and nodeq==None:
                return True
            if nodep==None or nodeq==None:
                return False

            if nodep.val!=nodeq.val:
                return False
            
            left = tra(nodep.left, nodeq.left)

            right = tra(nodep.right, nodeq.right)

            return left and right

        
        
        return tra(p,q)
        