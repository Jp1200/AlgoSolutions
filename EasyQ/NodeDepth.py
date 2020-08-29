def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# simple if case if the tree is empty there is no depth to it
# Recursivly iterate through the function where we return the init depth of 0 + func(leftofroot)+func(rightofroot)
# when you run the func again with the root.right/left if it isnt none you dont return 0 instead you add 1 to depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
