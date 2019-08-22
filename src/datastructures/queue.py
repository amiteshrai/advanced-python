""" Queue (FIFO) Implementation In Python """


class Queue:
    """ Queue """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__data = list()

    def enque(self, item) -> None:
        self.__data.append(item)

    def deque(self) -> object:
        item = None
        if self.size > 0:
            item = self.__data[0]
            self.__data = self.__data[1:]
        return item

    def peek(self) -> object:
        return None if self.size == 0 else self.__data[0]

    def poll(self) -> object:
        return self.deque()

    @property
    def size(self) -> int:
        return len(self.__data)

    def __str__(self):
        return str(self.__data)


if __name__ == "__main__":
    queue = Queue()
    queue.enque(1)
    queue.enque(11)
    queue.enque(21)
    queue.enque(31)
    queue.enque(41)
    print(queue)
    print(queue.size)

    print(queue.deque())
    print(queue)
    print(queue.size)

    print(queue.poll())
    print(queue)
    print(queue.size)

    print(queue.peek())
    print(queue)
    print(queue.size)
