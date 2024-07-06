# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        res = []
        if root:
            queue.append(root)
        
        while queue:
            lst = []
            for j in range(len(queue)):
                cur = queue.popleft()
                
                if cur:
                    lst.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if lst:
                res.append(lst)
        
        return res
            
                
            
            
        