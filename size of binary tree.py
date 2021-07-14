def size_(self, node):
      if node is None:
        return 0
      return 1 + self.size_(node.right)+self.size_(node.left)

