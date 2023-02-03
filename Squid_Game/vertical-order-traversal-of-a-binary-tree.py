# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ordered = []
                    # node, row, col
        queue.append((root, 0, 0))
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                ordered.append(node)
                
                if node[0].left:
                    queue.append((node[0].left, node[1] + 1, node[2] - 1))
                    
                if node[0].right:
                    queue.append((node[0].right, node[1] + 1, node[2] + 1))
                    
        ordered.sort(key=lambda x: (x[2],x[1],x[0].val))
        
        ans = []
        if len(ordered):
            ans.append([ordered[0][0].val])
        else:
            return ans
            
        for i in range(1, len(ordered)):
            if ordered[i-1][2] == ordered[i][2]:
                ans[-1].append(ordered[i][0].val)
            else:
                ans.append([ordered[i][0].val])
                
        return ans
