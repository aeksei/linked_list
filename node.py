from typing import Any


class Node:
    def __init__(self, value: Any, next_=None, prev=None):
        """
        Создаем новый узел для двусвязного списка

        :param value:
        :param next_: node class Node
        :param prev: node class Node
        """
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

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {self.next.value}, {self.prev.value})"
