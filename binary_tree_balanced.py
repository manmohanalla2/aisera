class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (abs(lh - rh) <= 1) and isBalanced(
    root.left) is True and isBalanced( root.right) is True:
        return True
    return False


# Balanced Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
root.right.right.right = Node(7)

#Unbalanced Tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(7)

print("Balanced Binary Tree:", end=' ')
if isBalanced(root):
    print(True)
else:
    print(False)