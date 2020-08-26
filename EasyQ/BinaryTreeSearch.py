def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)


def findClosest(tree, target, closest):

    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value > target:
        return findClosest(tree.left, target, closest)
    elif tree.value < target:
        return findClosest(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
