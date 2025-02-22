# Program to traverse given tree in pre-order, in-order and post-order fashion


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def inorder_traversal(self, node, path):
        if node:
            path = self.inorder_traversal(node.left, path)
            path += str(node.val) + ' '
            path = self.inorder_traversal(node.right, path)

        return path

    def preorder_traversal(self, node, path):
        if node:
            path += str(node.val) + ' '
            path = self.preorder_traversal(node.left, path)
            path = self.preorder_traversal(node.right, path)

        return path

    def postorder_traversal(self, node, path):
        if node:
            path = self.postorder_traversal(node.left, path)
            path = self.postorder_traversal(node.right, path)
            path += str(node.val) + ' '

        return path
    
    def inorder_traversal_iterative(self, node, path):
        if node:
            stack = []
            curr = node
            while (curr or len(stack) > 0):
                while curr != None:
                  stack.append(curr)
                  curr = curr.left
                curr = stack.pop()
                path += str(curr.val) + ' '
                curr = curr.right
        return path
    
    def preorder_traversal_iterative(self, node, path):
        if node:
          stack = []
          stack.append(node)
          while len(stack) > 0:
            curr = stack.pop()
            path += str(curr.val) + ' '
            if curr.right != None:
              stack.append(curr.right)
            if curr.left != None:
              stack.append(curr.left)
        return path
    
    def postorder_traversal_iterative(self, node, path):
      stack = []
      curr = node
      while (True):
        while (curr != None):
          stack.append(curr)
          stack.append(curr)
          curr = curr.left
        if (len(stack) == 0):
          return path
        curr = stack.pop()
        if (len(stack) > 0 and stack[-1] == curr):
          curr = curr.right
        else:
          path += str(curr.val) + ' '
          curr = None
      return path

# Creating a tree of the following structure:-

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

tree = Tree(1)

tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)

tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)

# In-Order Traversal :- left -> root -> right
print("In-Order Traversal :- left -> root -> right")
print("Recursive:")
print(tree.inorder_traversal(tree.root, ''))
print("Iterative:")
print(tree.inorder_traversal_iterative(tree.root, ''))
# Expected Output:- 4 2 5 1 6 3 7

print("\n")

# Pre-Order Traversal :- root -> left -> right
print("Pre-Order Traversal :- root -> left -> right")
print("Recursive:")
print(tree.preorder_traversal(tree.root, ''))
print("Iterative:")
print(tree.preorder_traversal_iterative(tree.root, ''))
# Expected Output:- 1 2 4 5 3 6 7

print("\n")

# Post-Order Traversal :- left -> right -> root
print("Post-Order Traversal :- left -> right -> root")
print("Recursive:")
print(tree.postorder_traversal(tree.root, ''))
print("Iterative:")
print(tree.postorder_traversal_iterative(tree.root, ''))
# Expected Output:- 4 5 2 6 7 3 1
