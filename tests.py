import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()

    def test_insert_empty_list(self):
        self.list_.insert(0, 5)

        self.assertEqual(len(self.list_), 1)
        self.assertEqual(self.list_._LinkedList__head.value, 5)
        self.assertEqual(self.list_._LinkedList__tail.value, 5)


if __name__ == '__main__':
    unittest.main()
