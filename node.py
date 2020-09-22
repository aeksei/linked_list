import sys
from weakref import ref

from typing import Any, Sequence
from observed import Subject


class Node(Subject):
    def __init__(self, value: Any, next_=None, prev=None, objects: Sequence = None):
        """
        Создаем новый узел для двусвязного списка

        :param value:
        :param next_: node class Node
        :param prev: node class Node
        """
        super().__init__(objects)
        self.next = next_  # class Node
        self.prev = prev
        self.value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if not isinstance(next_, (Node, type(None))):
            raise TypeError

        self.__next = next_

    @property
    def prev(self):
        return self.__prev() if self.__prev is not None else None

    @prev.setter
    def prev(self, prev):
        if not isinstance(prev, (Node, type(None))):
            raise TypeError
        self.__prev = ref(prev) if prev is not None else None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val
        self.notify()

    def __repr__(self):

        return f"{self.__class__.__name__}({self.value}, " \
               f"{self.next.value if self.next is not None else None}, " \
               f"{self.prev.value if self.prev is not None else None})"

    def __del__(self):
        print(f"Нода {repr(self)} удалена")

if __name__ == '__main__':
    first = Node(5)
    second = Node(10, prev=first)
    first.next = second

    print("first", sys.getrefcount(first) - 1)
    print("second", sys.getrefcount(second) - 1)

    print(second.prev)
    del first
    print("second after del", sys.getrefcount(second) - 1)
    print(second.prev)









