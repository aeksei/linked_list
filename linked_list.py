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

            self.__len += 1

        elif index >= self.__len:  # вставка вне границ
            insert_node.prev = self.__tail
            self.__tail.next = insert_node
            self.__tail = insert_node







if __name__ == '__main__':
    l = LinkedList()
    print(len(l))
