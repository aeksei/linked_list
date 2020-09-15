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
        self.__next = next_  # class Node
        self.__prev = prev
        self.value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if not isinstance(next_, Node):
            raise TypeError

        self.__next = next_

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        if not isinstance(prev, Node):
            raise TypeError
        self.__prev = prev

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val
        self.notify()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {self.next.value}, {self.prev.value})"
