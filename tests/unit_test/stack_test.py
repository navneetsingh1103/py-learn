import unittest

from ds.stack import Stack

class StackTestCase(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.push("D")
        self.assertEqual(stack.pop(), "D")
        self.assertEqual(stack.peek(), "C")


if __name__ == '__main__':
    unittest.main()
