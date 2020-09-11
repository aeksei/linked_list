from typing import Any

from node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def insert(self, index, value):
        insert_node = Node(value)
        if not self.__len:  # пустой список
            self.__head = insert_node
            self.__tail = self.__head
        elif index >= self.__len:  # вставка вне границ
            insert_node.prev = self.__tail
            self.__tail.next = insert_node
            self.__tail = insert_node

        self.__len += 1

    def append(self, value: Any) -> None:
        """
        Append Node to tail of LinkedList

        :param value:
        :return: None
        """
        append_node = Node(value)
        if not self.__len:  # пустой список
            self.__head = append_node
            self.__tail = self.__head
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...

    def remove(self, value):
        ...

    def delete(self, index):
        ...


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)

