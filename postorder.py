
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = []
        if root:
            
            response = response + self.preorderTraversal(root.left)
            response = response + self.preorderTraversal(root.right)
            response.append(root.val)
        return response