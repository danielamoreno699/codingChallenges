# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = []
        if root:
            response = self.inorderTraversal(root.left)
            response.append(root.val)
            response = response + self.inorderTraversal(root.right)
        return response