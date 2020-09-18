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
        if not self.__len:  # пустой список
            self._head = Node(value)
            self._tail = self._head

        elif index >= self.__len:  # вставка вне границ
            self.append(value)

        elif index == 0:
            insert_node = Node(value)
            self.__insert(insert_node, None, self._head)
            self._head = insert_node

        elif index == (self.__len - 1):
            insert_node = Node(value)
            self.__insert(insert_node, self._tail, None)
            self._tail = insert_node
        else:


        self.__len += 1

    def __insert(self, insert_node: Node, left_node: Node = None, right_node: Node = None):
        insert_node.prev = left_node
        insert_node.next = right_node

        if left_node is not None:
            left_node.next = insert_node
        if right_node is not None:
            right_node.next = insert_node

        return insert_node

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

    def __setitem__(self, key, value):
        current_node = self._head
        for _ in range(key):
            current_node = current_node.next

        current_node.value = value  # LinkedList[10]

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
