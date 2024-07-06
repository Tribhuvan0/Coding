# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxiDepth(self, root: Optional[TreeNode]) -> int: # By DFS
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    
    def maxDepth(self, root): #By BFS
        queue = deque()
        level = 0
        
        if root:
            queue.append(root)
            
        while(len(queue)) > 0:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
            level += 1
        return level
            
        
        
        
        