def tree_height(tree):
    if tree is None:
        return 0
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if left_height is -1 or right_height is -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1