import unittest

from src.ds import LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = LinkedList()
        linked_list.append("A")
        linked_list.append("B")
        linked_list.append("C")
        linked_list.append("D")
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
