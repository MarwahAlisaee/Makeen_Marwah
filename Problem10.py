class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(tree1, tree2):
    if tree1 is None:
        return True
    if tree2 is None:
        return False

    if is_identical(tree1, tree2):
        return True

    return is_subtree(tree1, tree2.left) or is_subtree(tree1, tree2.right)

def is_identical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False

    return (
        node1.val == node2.val and
        is_identical(node1.left, node2.left) and
        is_identical(node1.right, node2.right)
    )

tree1 = TreeNode(10)
tree1.left = TreeNode(4)
tree1.right = TreeNode(6)
tree1.left.right = TreeNode(30)

tree2 = TreeNode(26)
tree2.left = TreeNode(10)
tree2.right = TreeNode(3)
tree2.left.left = TreeNode(4)
tree2.left.right = TreeNode(6)
tree2.left.left.right = TreeNode(30)
tree2.right.right = TreeNode(3)

if is_subtree(tree1, tree2):
    print("Tree one is a subtree of tree two")
else:
    print("Tree one is not a subtree of tree two")

