""" Binary Tree Implementation In Python """


class BinaryTree:
    """ Binary Tree Class """

    def __init__(self, data, left=None, right=None):
        super().__init__()
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:  # Duplicate
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = BinaryTree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = BinaryTree(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
