import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_append(self):
        # добавление в пустой список
        self.linked_list.append(1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 1)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 1)
        self.assertEqual(len(self.linked_list), 1)

        # добавление в не пустой список
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__head.value, 1)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 2)
        self.assertEqual(len(self.linked_list), 2)

    def test_iter(self):
        values = [1, 2]

        for value in values:
            self.linked_list.append(value)

        for true_value, linked_value in zip(values, self.linked_list):
            self.assertEqual(true_value, linked_value)

        for index, linked_value in self.linked_list:
            self.assertEqual(values[index], linked_value)
