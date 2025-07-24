# Example: Binary Tree Node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating a tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
print(root.left.value)  # Output: 5
