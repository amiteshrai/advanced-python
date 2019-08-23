""" Linked List Implementation In Python """


class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        super().__init__()
        self.value = value
        self.next = next_node
        self.previous = previous_node

    def __str__(self):
        return "{}{}{}".format("(", self.value, ")")


class LinkedList(object):
    """ Linked List Class """

    def __init__(self):
        super().__init__()
        self.root = None
        self.size = 0

    def add(self, item):
        new_node = Node(item, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, item):
        root_node = self.root
        previous_node = None
        is_removed = False
        while root_node is not None:
            if root_node.value == item:
                if previous_node is not None:  # data is in the next node
                    previous_node.next = root_node.next
                else:  # data is in the root node
                    self.root = root_node.next_node
                self.size -= 1
                is_removed = True
                break
            else:
                previous_node = root_node
                root_node = root_node.next
        return is_removed

    def find(self, item):
        root_node = self.root
        value = None
        while root_node is not None:
            if root_node.value == item:
                value = item
                break
            else:
                root_node = root_node.next

        return value

    def print(self):
        root_node = self.root
        while root_node is not None:
            print(root_node, end="->")
            root_node = root_node.next
            if root_node is None:
                print(None)


if __name__ == "__main__":
    data = LinkedList()
    data.add(11)
    data.add(22)
    data.add(33)
    data.add(44)
    data.add(55)

    data.print()

    print(data.remove(99))
    print(data.remove(11))
    print(data.find(22))

    data.print()
