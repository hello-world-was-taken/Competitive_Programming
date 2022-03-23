#https://leetcode.com/problems/find-largest-value-in-each-tree-row/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ans = []
        if root:
            queue.append(root)
            while len(queue):
                size = len(queue)
                maxi = float("-inf")
                for i in range(size):
                    temp_1 = queue.popleft()
                    if temp_1.left:
                        queue.append(temp_1.left)
                    if temp_1.right:
                        queue.append(temp_1.right)
                    maxi = max(maxi, temp_1.val)
                    
                ans.append(maxi)
                
        return ans
