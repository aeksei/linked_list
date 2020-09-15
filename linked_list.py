from node import Node
from driver import IStructureDriver
from observed import Object


class LinkedList:
    def __init__(self, driver: IStructureDriver = None):
        self.driver = driver
        self._head = None
        self._tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def insert(self, index, value):
        insert_node = Node(value)
        if not self.__len:  # пустой список
            self._head = insert_node
            self._tail = self._head

            self.__len += 1

        elif index >= self.__len:  # вставка вне границ
            insert_node.prev = self._tail
            self._tail.next = insert_node
            self._tail = insert_node

    def append(self, value):
        append_node = Node(value)
        if not self.__len:  # пустой список
            self._head = append_node
            self._tail = self._head
        else:
            append_node.prev = self._tail
            self._tail.next = append_node
            self._tail = append_node

        self.__len += 1

    def __iter__(self):
        current_node = self._head
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.next

    def write(self):
        self.driver.write([value for value in self])


class ObservedLinkedList(LinkedList, Object):
    def __init__(self, driver: IStructureDriver = None):
        super().__init__(driver)

    def update(self):
        self.write()

    def append(self, value):
        super().append(value)
        self._tail.add_object(self)
        self._tail.notify()


if __name__ == '__main__':
    l = LinkedList()
    print(len(l))
