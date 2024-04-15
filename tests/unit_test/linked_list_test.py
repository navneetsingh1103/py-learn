import unittest

from ds.linked_list import LinkedList
from ds.node import Node

class LinkedlistTest(unittest.TestCase):
    def test_reverse_iterative(self):
        linked_list = LinkedList()
        linked_list.append("A")
        linked_list.append("B")
        linked_list.append("C")
        linked_list.append("D")
        linked_list.reverse_iterative()
        self.assertEqual(linked_list.head.data, "D")
        self.assertEqual(linked_list.head.next.data, "C")
        self.assertEqual(linked_list.head.next.next.data, "B")
        self.assertEqual(linked_list.head.next.next.next.data, "A")

    def test_node_swap(self):
        linked_list = LinkedList()
        linked_list.append("A")
        linked_list.append("B")
        linked_list.append("C")
        linked_list.append("D")
        linked_list.node_swap("B", "D")
        self.assertEqual(linked_list.linked_list_data(), ["A", "D", "C", "B"])

    def test_reverse_recursive(self):
        linked_list = LinkedList()
        linked_list.append("A")
        linked_list.append("B")
        linked_list.append("C")
        linked_list.append("D")
        linked_list.reverse_recursive()
        self.assertListEqual(linked_list.linked_list_data(), ["D", "C", "B", "A"])

    def test_merge_sort_list(self):
        linked_list_01 = LinkedList()
        linked_list_01.append(1)
        linked_list_01.append(5)
        linked_list_01.append(7)
        linked_list_01.append(9)
        linked_list_01.append(10)

        linked_list_02 = LinkedList()
        linked_list_02.append(2)
        linked_list_02.append(3)
        linked_list_02.append(4)
        linked_list_02.append(6)
        linked_list_02.append(8)

        linked_list_01.merge_sort_list(linked_list_02)
        self.assertListEqual(linked_list_01.linked_list_data(), [1,2,3,4,5,6,7,8,9,10])

    def test_remove_duplicate(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(6)
        linked_list.append(1)
        linked_list.append(4)
        linked_list.append(2)
        linked_list.append(2)
        linked_list.append(4)

        linked_list.remove_duplicates()
        self.assertListEqual(linked_list.linked_list_data(), [1,6,4,2])

    def test_get_nth_from_last(self):
        linked_list = LinkedList()
        linked_list.append("A")
        linked_list.append("B")
        linked_list.append("C")
        linked_list.append("D")
        nth_data = linked_list.get_nth_from_last(2)
        self.assertEqual(nth_data, "C")

    def test_rotate(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.rotate(3)
        self.assertListEqual(linked_list.linked_list_data(), [4,5,1,2,3])

if __name__ == '__main__':
    unittest.main()
