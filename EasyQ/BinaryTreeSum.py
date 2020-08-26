class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):

    output = []
    addNode(root, 0, output)
    return output


def addNode(node, runningTotal, output):
    if node is None:
        return
    runningTotal = runningTotal + node.value
    if node.left is None and node.right is None:
        output.append(runningTotal)
        return

    addNode(node.left, runningTotal, output)
    addNode(node.right, runningTotal, output)
