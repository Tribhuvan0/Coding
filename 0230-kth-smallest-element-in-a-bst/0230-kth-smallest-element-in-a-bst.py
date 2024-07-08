# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        lst = []
        def inOrder(root):
            if not root:
                return []
            
            inOrder(root.left)
            lst.append(root.val)
            inOrder(root.right)
            
            return lst
        
        lst = inOrder(root)
        return lst[k-1]
            
        