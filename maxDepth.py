class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node (data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

root = Node(1)
root.insert(null)
root.insert(2)
root.insert(3)

root.PrintTree()

def tree_max_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root) - 1 if root else 0