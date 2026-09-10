# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return 0, 0  # (sum, count)
            
            # Get data from subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate values for current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check condition (integer division)
            if current_sum // current_count == node.val:
                self.count += 1
                
            return current_sum, current_count

        dfs(root)
        return self.count
