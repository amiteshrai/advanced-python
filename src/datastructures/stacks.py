""" Stack (LIFO) Implementation In Python """


class Stack:
    """ Stack Implementation Class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = list()

    def push(self, item) -> None:
        """
        Add an item to the stack
        Arguments:
            item {[type]} -- [description]
        """
        self.data.append(item)

    def pop(self) -> object:
        """
        Remove and return the last element from the stack
        Returns:
            [type] -- [description]
        """
        return None if not self.data else self.data.pop()

    def peek(self) -> object:
        """
        Return the last element from the stack
        Returns:
            [type] -- [description]
        """
        return None if not self.data else self.data[len(self.data) - 1]

    def __str__(self) -> str:
        """
        String representation of the elements
        Returns:
            [type] -- [description]
        """
        return str(self.data)

    @property
    def size(self) -> int:
        """
        Return the number of elements present in the stack.
        Returns:
            [type] -- [description]
        """
        return len(self.data)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.size)

    stack.push(12)
    stack.push(1)
    print(stack)
    print(stack.size)

    print(stack.peek())
    print(stack.pop())
    print(stack)
