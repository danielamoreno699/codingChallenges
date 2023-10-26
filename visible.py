
def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val >= max_sofar:
            total += 1

        total += dfs(root.left, max(max_sofar, root.val)) # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.right, max(max_sofar, root.val))

        return total